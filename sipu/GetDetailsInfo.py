import os
import re
import time
import requests
import logging
from bs4 import BeautifulSoup

# ========== 日志配置 ==========
# log_dir = "log"
# os.makedirs(log_dir, exist_ok=True)
# log_file = os.path.join(log_dir, "logs.log")
# 
# logging.basicConfig(
#     filename=log_file,
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     encoding="utf-8"
# )

headers = {"User-Agent": "Mozilla/5.0"}


# ========== 工具函数 ==========
def clean_text(value):
    """清洗非法或不可见字符"""
    if isinstance(value, str):
        return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', '', value.strip())
    return value


def request_with_retry(url, headers=None, proxies=None, max_retries=3, delay=2, timeout=10):
    """带重试机制的请求"""
    for attempt in range(1, max_retries + 1):
        try:
            res = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
            res.raise_for_status()
            logging.info(f"开始请求抓取化合物: {url}")
            logging.info(f"请求成功: {url} (状态码: {res.status_code})")
            return res
        except Exception as e:
            if attempt < max_retries:
                logging.warning(f"请求失败 (第{attempt}次): {url} | 错误: {e} | {delay}s后重试...")
                time.sleep(delay)
            else:
                logging.error(f"请求最终失败 (共重试{max_retries}次): {url} | 错误: {e}")
                return None


# ========== 主函数 ==========
def get_detail_url(id):
    """
    根据化合物编号获取详细信息并记录日志
    """
    url = f"https://www.push-herbchem.com/ps_dantiDetail.aspx?cNumber={id}"
    proxies = {"http": None, "https": None}

    # 使用带重试的请求
    res = request_with_retry(url, headers=headers, proxies=proxies)
    if res is None:
        logging.error(f"[{id}] 请求多次失败，跳过此化合物。")
        return {}

    html_content = res.text
    full_soup = BeautifulSoup(html_content, 'html.parser')
    target_divs = full_soup.find_all('div', class_='dantidiv')

    if target_divs:
        simplified_html = ''.join([str(div) for div in target_divs[:2]])
        soup = BeautifulSoup(simplified_html, 'html.parser')
    else:
        soup = full_soup

    try:
        chemical_data = {
            "CAS号": clean_text(soup.find('strong', class_='w4').find_next('span').text),
            "分子式": clean_text(soup.find('span', id='span_Formula').text),
            "分子量": clean_text(
                soup.find('strong', string='【分子量】')
                .find_parent('span').next_sibling.strip()
            ) if soup.find('strong', string='【分子量】') else "",
            "存储条件": clean_text(
                soup.find('strong', string='【存储条件】')
                .find_parent('div').contents[-1].strip()
            ) if soup.find('strong', string='【存储条件】') else "",
            "结构类型": clean_text(
                soup.find('strong', string='【结构类型】').find_next('span').text
            ),
            "删除CAS": clean_text(
                soup.find('strong', class_='w5').find_next('span').text
            ),
            "中文名": clean_text(
                soup.find('strong', class_='w3', string='【中文名】').find_next('span').get('title', '')
            ),
            "英文名": clean_text(
                soup.find('strong', class_='w3', string='【英文名】').find_next('span').get('title', '')
            ),
            "中文副名": clean_text(
                soup.find('strong', string='【中文副名】').find_next('span').text
            ),
            "英文副名": clean_text(
                soup.find('strong', string='【英文副名】').find_next('span').text
            ),
            "溶解性": clean_text(
                soup.find('strong', string='【溶解性】').find_next('span').text
            ),
            "标准收录": clean_text(
                soup.find('strong', string='【标准收录】').find_next('span').text
            )
        }

        logging.info(f"[{id}] 数据提取成功: {chemical_data.get('CAS号', '未知化合物')}")
        return chemical_data

    except Exception as e:
        logging.exception(f"[{id}] 数据解析失败: {e}")
        return {}


# ========== 调试入口 ==========
if __name__ == '__main__':
    result = get_detail_url("CN000083")
