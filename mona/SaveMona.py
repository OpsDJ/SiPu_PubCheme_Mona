import logging
import os
import re
import csv

def get_id_path_map(base_path):
    """递归遍历目录，建立 id -> 文件夹路径映射"""
    id_path = {}
    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            if "_" in d:
                try:
                    folder_id = int(d.split("_")[0])
                    id_path[folder_id] = os.path.join(root, d)
                except ValueError:
                    continue
    logging.info(f"目录扫描完成，共识别 {len(id_path)} 个 ID 映射")
    return id_path


def get_sheet_info_by_id(root_dir, cat_id):
    """输入 cat_id，返回对应的 CSV 文件路径和名称（使用原 sheet_name 命名）"""
    id_path_map = get_id_path_map(root_dir)
    save_path = id_path_map.get(cat_id)

    if not save_path:
        logging.warning(f"未找到 ID={cat_id} 的分类路径")
        return None, None

    # 原 sheet_name
    current_folder = os.path.basename(save_path)
    sheet_name = "".join(re.findall(r'[\u4e00-\u9fff]+', current_folder)) or current_folder

    # CSV 文件放在上一层目录
    parent_folder = os.path.dirname(save_path)
    csv_file = os.path.join(parent_folder, f"{sheet_name}.csv")
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    logging.info(f"生成 CSV 路径: {csv_file} | 名称: {sheet_name}")
    return csv_file, sheet_name


def save_mona_data_basic(file_path, data):
    """保存 MONA 数据到 CSV 文件"""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)

            # 空行分隔
            writer.writerow([])
            writer.writerow([])

            # 数据头
            writer.writerow(["MONA数据库"])
            writer.writerow(["mz", "intensity"])

            mz_values, intensity_values, precursor_mz, collision_energy, precursor_type = data

            # 写入 mz/intensity
            for mz, inten in zip(mz_values, intensity_values):
                writer.writerow([mz, inten])

            writer.writerow([])

            # 其他信息
            if precursor_mz:
                writer.writerow(["Precursor m/z", precursor_mz])
            if collision_energy:
                writer.writerow(["Collision energy", collision_energy])
            if precursor_type:
                writer.writerow(["Precursor type", precursor_type])

    except Exception as e:
        logging.error(f"保存 CSV 失败：{e}")


if __name__ == '__main__':
    root_dir = r"./../CompoundLibrary"
    test_id = 54
    print(get_sheet_info_by_id(root_dir, test_id))
