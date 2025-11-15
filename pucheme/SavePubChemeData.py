import os
import re
import csv
import logging

# ===================== 目录与 sheet_name =====================
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
    """输入 cat_id，返回对应的文件夹路径和 sheet 名"""
    id_path_map = get_id_path_map(root_dir)
    save_path = id_path_map.get(cat_id)
    if not save_path:
        logging.warning(f"未找到 ID={cat_id} 的分类路径")
        return None, None
    current_folder = os.path.basename(save_path)
    sheet_name = "".join(re.findall(r'[\u4e00-\u9fff]+', current_folder)) or current_folder
    return save_path, sheet_name

# ===================== CSV 文件路径 =====================
def save_chemical_data(root_dir, cat_id):
    """生成 CSV 文件路径，文件名使用 sheet_name，放在分类文件夹的上一级目录"""
    path, sheet_name = get_sheet_info_by_id(root_dir, cat_id)
    if not path:
        return None, None

    parent_folder = os.path.dirname(path)  # 分类文件夹的上一级
    csv_file = os.path.join(parent_folder, f"{sheet_name}.csv")
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    return csv_file, sheet_name

# ===================== CSV 写入函数 =====================
def save_to_csv_pubcheme_append(csv_file, data):
    """追加写入 PubChem KV 信息"""
    kv_data = [
        ["", ""],
        ["", ""],
        ["pubchem数据库", ""],
        ["id", data[0]],
        ["Collision Energy", data[1]],
        ["Retention Time", data[2]],
        ["Precursor m/z", data[3]],
        ["", ""],
        ["", ""],
    ]
    with open(csv_file, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(kv_data)

def save_to_csv_pubcheme_spectrum(csv_file, mz_values, intensity_values):
    """追加写入谱峰数据 (mz, intensity)"""
    min_length = min(len(mz_values), len(intensity_values))
    spectrum_data = [["", ""], ["", ""], ["mz", "intensity"]]
    for i in range(min_length):
        spectrum_data.append([mz_values[i], intensity_values[i]])
    with open(csv_file, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(spectrum_data)

# ===================== 调试入口 =====================
if __name__ == "__main__":
    root_dir = r"./../CompoundLibrary"
    test_id = 54

    csv_file, sheet_name = save_chemical_data(root_dir, test_id)
    print(f"CSV 路径: {csv_file}, 文件名(sheet_name): {sheet_name}")

    # 测试写入 KV
    pubchem_data = ["12345", "10eV", "5.2", "286.45"]
    save_to_csv_pubcheme_append(csv_file, pubchem_data)

    # 测试写入谱峰
    mz = [100, 150, 200]
    intensity = [1000, 500, 200]
    save_to_csv_pubcheme_spectrum(csv_file, mz, intensity)
