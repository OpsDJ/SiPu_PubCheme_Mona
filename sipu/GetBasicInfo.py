import os
import time
import logging

import requests
from urllib.parse import urljoin
from tqdm import tqdm

headers = {"User-Agent": "Mozilla/5.0"}
proxies = {"http": None, "https": None}

# 根目录（你的文件夹所在位置）
root_dir = r"./../CompoundLibrary"

# 配置常量
CONFIG = {
    "MAX_RETRIES": 3,
    "REQUEST_TIMEOUT": 10,
    "RETRY_DELAY": 2,
    "IMAGE_RETRY_DELAY": 2,
    "PAGE_LIMIT": 100
}

# 设置日志配置
log_file = os.path.join("log", f"collection_{time.strftime('%Y%m%d_%H%M%S')}.log")
os.makedirs("log", exist_ok=True)  # 确保日志目录存在
# 设置日志配置
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    force=True
)


# 递归收集所有 id 文件夹路径
def get_id_path_map(base_path):
    id_path = {}
    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            if "_" in d:
                try:
                    folder_id = int(d.split("_")[0])
                    id_path[folder_id] = os.path.join(root, d)
                except ValueError:
                    continue
    return id_path


# 建立 id→文件夹路径映射
id_path_map = get_id_path_map(root_dir)
logging.info(f"找到 {len(id_path_map)} 个分类文件夹。")


# 获取化合物列表
def get_list_page(cat_id, page):
    url = f"https://www.push-herbchem.com/api/Product/GettCompoundsPage/12/{page}/{cat_id}"

    # 添加重试逻辑
    max_retries = CONFIG["MAX_RETRIES"]
    for attempt in range(max_retries):
        try:
            res = requests.get(url, headers=headers, proxies=proxies, timeout=CONFIG["REQUEST_TIMEOUT"])
            res.raise_for_status()  # 检查HTTP错误
            data_list = res.json().get("Data", [])
            break  # 成功获取数据，跳出重试循环
        except requests.exceptions.RequestException as e:
            error_msg = f"请求失败 分类{cat_id} 页码{page} (尝试 {attempt + 1}/{max_retries}): {e}"
            logging.error(error_msg)
            if attempt == max_retries - 1:  # 最后一次尝试失败
                return [], []
            time.sleep(CONFIG["RETRY_DELAY"])  # 等待后重试
        except ValueError as e:  # JSON解析错误
            error_msg = f"JSON解析失败 分类{cat_id} 页码{page} (尝试 {attempt + 1}/{max_retries}): {e}"
            logging.error(error_msg)
            if attempt == max_retries - 1:  # 最后一次尝试失败
                return [], []
            time.sleep(CONFIG["RETRY_DELAY"])  # 等待后重试

    cat_list, image_url = [], []
    for d in data_list:
        cat_list.append(str(d.get("CatalogNumber")))
        image_url.append(urljoin("https://www.push-herbchem.com", d.get("ImgUrl")))
    return cat_list, image_url


# 下载图片
def download_image(img_url, save_folder):
    max_retries = CONFIG["MAX_RETRIES"]
    for attempt in range(max_retries):
        try:
            # 确保保存目录存在
            os.makedirs(save_folder, exist_ok=True)

            res = requests.get(img_url, headers=headers, proxies=proxies, timeout=CONFIG["REQUEST_TIMEOUT"])
            if res.status_code == 200:
                img_name = img_url.split("/")[-1]
                save_path = os.path.join(f"{save_folder}/img", img_name)
                with open(save_path, "wb") as f:
                    f.write(res.content)
                return img_name
            else:
                error_msg = f"下载失败 {img_url}: HTTP {res.status_code}"
                logging.error(error_msg)
        except Exception as e:
            error_msg = f"下载失败 {img_url} (尝试 {attempt + 1}/{max_retries}): {e}"
            logging.error(error_msg)
            if attempt < max_retries - 1:
                time.sleep(CONFIG["IMAGE_RETRY_DELAY"])  # 等待后重试
    return None


# 处理单个分类
def process_category(cat_id):
    if cat_id not in id_path_map:
        logging.info(f"分类 {cat_id} 没有对应文件夹，跳过")

        return

    save_path = id_path_map[cat_id]
    id_file = os.path.join(f"{save_path}/id", "compound_ids.txt")
    logging.info(f"正在处理分类 {cat_id} → {save_path}")

    # 添加统计变量
    total_compounds = 0
    total_images = 0
    failed_images = 0

    for page in tqdm(range(1, CONFIG["PAGE_LIMIT"]), desc=f"分类 {cat_id} 页码"):
        cat_list, img_list = get_list_page(cat_id, page)
        if not cat_list:
            break

        total_compounds += len(cat_list)

        with open(id_file, "a", encoding="utf-8") as f:
            for cid, img_url in zip(cat_list, img_list):
                f.write(cid + "\n")
                if download_image(img_url, save_path):
                    total_images += 1
                else:
                    failed_images += 1

    logging.info(f"分类 {cat_id} 完成: 化合物 {total_compounds} 个，图片 {total_images} 张，失败 {failed_images} 张")

def start():
    # 示例：选择要爬取的分类 ID（你可以改为任何已存在的ID）
    for cat_id in [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                   29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 7, 8, 9, 10, 11, 12, 13]:
        process_category(cat_id)
    logging.info("数据已保存到现有分类文件夹中！")

if __name__ == '__main__':
    start()
