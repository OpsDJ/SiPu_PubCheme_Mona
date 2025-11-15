import logging

import requests
import os


def download_sdf_by_cid(cid, cas, save_path):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF"
    r = requests.get(url, proxies={"http": "http://127.0.0.1:7897", "https": "http://127.0.0.1:7897"})
    download_path = os.path.dirname(save_path)
    doc_folder = os.path.join(download_path, "doc")

    # 打印绝对路径
    doc_folder_abs = os.path.abspath(doc_folder)
    # 创建文件夹
    os.makedirs(doc_folder_abs, exist_ok=True)

    save_path = doc_folder + f"/cas_{cas}.sdf"
    if r.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(r.content)
        logging.info(f"CAS: {cas} ======>SDF 下载完成")
    else:
        logging.error("SDF下载失败", r.status_code, r.text)
