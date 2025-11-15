import sys
import os
import re
import logging
import pandas as pd

# ===================== 日志配置 =====================
# log_dir = "log"
# os.makedirs(log_dir, exist_ok=True)
# log_file = os.path.join(log_dir, "logs.log")
# # logging.basicConfig(
# #     filename=log_file,
# #     level=logging.INFO,
# #     format="%(asctime)s [%(levelname)s] %(message)s",
# #     encoding="utf-8"
# # )


def resource_path(relative_path):
    """获取资源文件的绝对路径，兼容打包后的 exe"""
    if getattr(sys, 'frozen', False):  # PyInstaller 打包后
        base_path = sys._MEIPASS
    else:  # 脚本运行时
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)



# ===================== 建立 id -> 文件夹路径映射 =====================
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
    return id_path


# ===================== 查询函数 =====================
def get_sheet_info_by_id(root_dir, cat_id):
    """
    输入 cat_id，返回对应的文件夹路径和 Excel sheet 名
    """
    id_path_map = get_id_path_map(root_dir)
    save_path = id_path_map.get(cat_id)

    if not save_path:
        logging.warning(f"未找到 ID 为 {cat_id} 的分类路径")
        return None, None

    current_folder = os.path.basename(save_path)
    sheet_name = "".join(re.findall(r'[\u4e00-\u9fff]+', current_folder)) or current_folder

    return save_path, sheet_name


# ===================== 保存数据函数 =====================
def save_chemical_data(root_dir, cat_id, chemical_data, image_filename=None):
    """
    每个 sheet（分类）保存为单独的 CSV 文件
    """
    path, sheet_name = get_sheet_info_by_id(root_dir, cat_id)
    if not path:
        return

    parent_folder = os.path.dirname(path)
    grandparent_folder = os.path.dirname(parent_folder)

    # 原来 Excel 文件名逻辑保留，但用于决定 CSV 所在目录
    if os.path.normpath(grandparent_folder) == os.path.normpath(root_dir):
        excel_name = "".join(re.findall(r'[\u4e00-\u9fff]+', os.path.basename(path))) or os.path.basename(path)
        base_dir = path
    else:
        parent_folder_name = os.path.basename(parent_folder)
        excel_name = "".join(re.findall(r'[\u4e00-\u9fff]+', parent_folder_name)) or parent_folder_name
        base_dir = parent_folder

    # CSV 文件名直接使用 sheet 名（= 分类名）
    csv_file = os.path.join(base_dir, f"{sheet_name}.csv")
    csv_file = os.path.normpath(csv_file)
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    # ----- 生成 CSV 行（第一行带图片路径） -----
    rows = []
    first_row = True

    for k, v in chemical_data.items():
        if first_row:
            rows.append([k, v, image_filename])  # “原来图片行 → 第一行”
            first_row = False
        else:
            rows.append([k, v, ""])

    df = pd.DataFrame(rows, columns=['属性', '值', '图片路径'])

    # ----- 追加写入 CSV -----
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False, encoding="utf-8-sig")
    else:
        df.to_csv(csv_file, mode='w', header=True, index=False, encoding="utf-8-sig")

    logging.info(f"CSV 文件已保存：{csv_file}")


# ===================== 使用示例 =====================
if __name__ == "__main__":
    root_dir = r"./../CompoundLibrary"
    cat_id = 54
    chemical_data = {
        '分子式': 'C20H30O',
        '分子量': 286.45,
        'CAS号': '123-45-6'
    }
    save_chemical_data(root_dir, cat_id, chemical_data, image_filename='CN000070.jpg')
    # print(f"日志已记录到: {log_file}")
