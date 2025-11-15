import json
import time
import socket
import logging
import requests
from datetime import datetime

# ==================== 日志配置 ====================
# def setup_logger():
#     log_dir = os.path.join("logs")
#     os.makedirs(log_dir, exist_ok=True)
#
#     log_file = os.path.join(log_dir, f"pubchem_mona_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
#
#     logging.basicConfig(
#         filename=log_file,
#         level=logging.INFO,
#         format="%(asctime)s [%(levelname)s] %(message)s",
#         encoding="utf-8"
#     )
#
#     console = logging.StreamHandler()
#     console.setLevel(logging.INFO)
#     console.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
#     logging.getLogger().addHandler(console)
#
#     logging.info(f"日志初始化完成: {log_file}")
#     return log_file


# ==================== 通用工具函数 ====================
def is_port_open(host="127.0.0.1", port=7897, timeout=1):
    """检测代理端口是否开启"""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def request_with_retry(url, params=None, headers=None, proxies=None, timeout=20, max_retries=3):
    """
    带重试机制的HTTP请求函数
    """
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, params=params, headers=headers, proxies=proxies, timeout=timeout)
            response.raise_for_status()
            logging.info(f"请求成功 [{response.status_code}] → {url}")
            return response
        except Exception as e:
            wait_time = 1
            logging.warning(f"第 {attempt}/{max_retries} 次请求失败: {e} → {url}，{wait_time}s后重试")
            time.sleep(wait_time)
    logging.error(f"❌ 多次重试仍失败: {url}")
    return None


# ==================== 主请求函数 ====================
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


def get_proxies():
    if is_port_open("127.0.0.1", 7897):
        logging.info("检测到本地代理 (Clash) 运行中，使用代理访问。")
        return {"http": "http://127.0.0.1:7897", "https": "http://127.0.0.1:7897"}
    else:
        logging.warning("未检测到代理，使用直连模式。")
        return {"http": None, "https": None}


def search_pubchem_by_cas(cas_number):
    """通过CAS号在PubChem数据库中搜索化合物信息"""
    url = "https://pubchem.ncbi.nlm.nih.gov/sdq/sdqagent.cgi"
    query = {
        "select": "*",
        "collection": "compound",
        "order": ["relevancescore,desc"],
        "start": 1,
        "limit": 10,
        "where": {"ands": [{"*": cas_number}]},
        "width": 1000000,
        "listids": 0
    }

    proxies = get_proxies()
    response = request_with_retry(
        url,
        params={"infmt": "json", "outfmt": "json", "query": json.dumps(query)},
        headers=headers,
        proxies=proxies
    )

    if not response:
        return None

    try:
        data = response.json()
        rows = data["SDQOutputSet"][0].get("rows", [])
        if not rows:
            logging.info(f"未在 PubChem 中找到 CAS={cas_number} 的记录。")
            return None
        cid = rows[0].get("cid", "")
        logging.info(f"PubChem 查询成功，CAS={cas_number}, CID={cid}")
        return cid
    except Exception as e:
        logging.error(f"解析 PubChem 响应失败: {e}")
        return False


def search_pubchem_detail_by_cid(cid):
    """根据CID获取PubChem LC-MS详细信息"""
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON/?heading=LC+MS"
    proxies = get_proxies()

    response = request_with_retry(url, headers=headers, proxies=proxies)
    if not response:
        return None

    try:
        return response.json()
    except Exception as e:
        logging.error(f"解析 PubChem LC-MS JSON 失败: {e}")
        return None


def get_mona_spectrum(id):
    """从MoNA数据库获取指定ID的质谱数据"""
    url = f"https://mona.fiehnlab.ucdavis.edu/rest/spectra/{id}"
    proxies = get_proxies()

    response = request_with_retry(url, headers=headers, proxies=proxies)
    if not response:
        return None, None

    try:
        data = response.json()
        data_string = data.get("spectrum", "")
        pairs = data_string.split()
        mz_values, intensity_values = [], []
        for pair in pairs:
            mz, intensity = pair.split(":")
            mz_values.append(float(mz))
            intensity_values.append(float(intensity))
        logging.info(f"成功解析 MoNA 数据: {id} ({len(mz_values)} peaks)")
        return mz_values, intensity_values
    except Exception as e:
        logging.error(f"解析 MoNA 数据失败: {e}")
        return None, None


def get_spectrum_info(id):
    """从MassBank数据库获取质谱数据，若失败则回退到MoNA"""
    url = f"https://massbank.eu/MassBank-api/records/{id}"
    proxies = get_proxies()

    response = request_with_retry(url, headers=headers, proxies=proxies)
    if not response:
        logging.warning(f"MassBank 请求失败，尝试从 MoNA 获取数据: {id}")
        return get_mona_spectrum(id)

    try:
        if 'sql: no rows in result set' in response.text:
            logging.info(f"MassBank中无结果，尝试MoNA: {id}")
            return get_mona_spectrum(id)

        data = response.json()
        values = data["peak"]["peak"]["values"]
        mz_values = [item['mz'] for item in values]
        intensity_values = [item['intensity'] for item in values]
        logging.info(f"成功从 MassBank 获取数据: {id} ({len(mz_values)} peaks)")
        return mz_values, intensity_values
    except Exception as e:
        logging.error(f"解析 MassBank JSON 失败: {e}")
        return get_mona_spectrum(id)


# ==================== 主程序入口 ====================
if __name__ == '__main__':
    # log_file = setup_logger()
    logging.info("=== 程序启动 ===")

    cas = "57420-46-9"
    cid = search_pubchem_by_cas(cas)
    if cid:
        data = search_pubchem_detail_by_cid(cid)
        logging.info(f"LC-MS 详情字段: {list(data.keys())[:5] if data else '无数据'}")

    mz, inten = get_spectrum_info("MSBNK00001")
    if mz:
        logging.info(f"谱峰数量: {len(mz)}")

    logging.info("=== 程序结束 ===")
