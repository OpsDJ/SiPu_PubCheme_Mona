from .ParseMona import *
from .SaveMona import *
import os
import csv
import logging

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def mark_no_mona(file_path):
    """标记 MONA 无数据，保存到 CSV"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([])
            writer.writerow([])
            writer.writerow(["MONA数据库"])
            writer.writerow(["暂无数据"])
            writer.writerow([])
            writer.writerow([])
        # print("✅ 保存成功")
    except Exception as e:
        print(f"❌ 保存失败: {e}")


def search_mona(name, root_dir, cat_id):
    base_url = "https://mona.fiehnlab.ucdavis.edu/rest/spectra/search"
    file_path, sheet_name = get_sheet_info_by_id(root_dir, cat_id)

    query = (
        f"exists(compound.names.name~'{name}') "
        "and exists((metaData.name:'ms level' and metaData.value:'MS2'))"
    )

    logging.info(f"开始获取 MONA 数据，目标化合物名称：{name}")

    valid_data_found = False

    try:
        for page in range(4):

            params = {
                "endpoint": "search",
                "query": query,
                "size": 10,
                "page": page
            }

            data = request_with_retry(base_url, params=params)

            # ---------- 第一页失败：立即返回并标记 ----------
            if page == 0 and not data:
                logging.error("第一页数据获取失败，终止后续页面请求")
                return   # 必须：避免后续代码报错

            if not data:
                logging.error(f"第 {page} 页数据获取失败，跳过")
                continue

            ids = [item.get("id") for item in data if item.get("id")]

            # ---------- 提取 instrument type ----------
            instrument_types = []
            for item in data:
                for meta in item.get("metaData", []):
                    if meta.get('name') == 'instrument type':
                        instrument_types.append(meta.get('value'))
                        break

            logging.info(f"原始 instrument types 数量：{len(instrument_types)}")

            # ---------- 过滤 QTOF ----------
            filtered_ids = [
                idv for idv, inst in zip(ids, instrument_types)
                if "qtof" in inst.lower()
            ]

            logging.info(f"过滤后剩余数量：{len(filtered_ids)}")

            if len(filtered_ids) == 0:
                logging.warning(f"第 {page} 页无 QTOF 数据")
                continue

            valid_data_found = True

            # ---------- 获取详细数据 ----------
            for spectrum_id in filtered_ids:
                logging.info(f"开始获取 ID = {spectrum_id} 的详细数据")

                row = parse_mona_data(spectrum_id)
                if row:
                    save_mona_data_basic(file_path, row)
                    logging.info(f"成功保存 ID={spectrum_id} 的数据")
                else:
                    logging.warning(f"ID={spectrum_id} 数据解析失败")

    finally:
        # ---------- 安全：只在未找到数据时标记 ----------
        if not valid_data_found:
            logging.warning("MONA 数据获取失败或无 QTOF 数据，将标记为暂无数据")
            mark_no_mona(file_path)
            logging.info("已写入 '暂无数据' 标记到 CSV")

        logging.info("====== MONA 数据获取完毕 ======")


