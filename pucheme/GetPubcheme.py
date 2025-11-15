from .GetBasic import *
from .ParsePuchemeData import *
from .SavePubChemeData import *
from .Donload import *

# ================= 日志系统 =================
# def setup_logger():
#     log_dir = "log"
#     os.makedirs(log_dir, exist_ok=True)
#     log_file = os.path.join(log_dir, f"pubchem_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
#
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s [%(levelname)s] %(message)s",
#         handlers=[
#             logging.FileHandler(log_file, encoding="utf-8"),
#             logging.StreamHandler()
#         ]
#     )
#     logging.info(f"日志系统启动，日志文件：{log_file}")


# ================= CSV 保存替代 =================
def mark_no_pubchem(file_path, sheet_name):
    """
    如果没有数据，用 CSV 记录 '暂无数据'，保持原逻辑接口不变
    """
    csv_file = os.path.join(os.path.dirname(file_path), f"{sheet_name}.csv")
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    try:
        with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([])
            writer.writerow([])
            writer.writerow(["PubChem数据库"])
            writer.writerow(["暂无数据"])
            writer.writerow([])
            writer.writerow([])
        logging.info(f"标记无数据 CSV 已保存: {csv_file}")
    except Exception as e:
        logging.error(f"保存无数据 CSV 失败: {e}")


# ================= 核心函数 =================
def get_pubcheme_data_by_cas(cas_number, save_path, sheet_name):
    logging.info(f"开始处理 CAS号: {cas_number}")

    cid = search_pubchem_by_cas(cas_number)
    # 下载 SDF 文件
    download_sdf_by_cid(cid, cas_number, save_path)
    if not cid:
        logging.warning(f"未找到CAS号 {cas_number} 对应的化合物")
        mark_no_pubchem(save_path, sheet_name)
        return False

    data = search_pubchem_detail_by_cid(str(cid))
    ids, collision_energy, retention_time, precursor_mz = parese_pubchem_detail(data)

    if len(ids) == 0:
        logging.warning(f"CAS号 {cas_number} 在PubChem中找到CID={cid}，但未找到4.2条目数据")
        mark_no_pubchem(save_path, sheet_name)
        return False

    for a, b, c, d in zip(ids, collision_energy, retention_time, precursor_mz):
        result = get_spectrum_info(a)
        if result is not None:
            mz_values, intensity_values = result
            # 保存基本信息
            save_to_csv_pubcheme_append(save_path, [a, b, c, d])
            # 保存详细谱峰信息
            save_to_csv_pubcheme_spectrum(save_path, mz_values, intensity_values)
            logging.info(f"成功保存PubChem数据库 ID={a} 的数据")
        else:
            logging.warning(f"跳过ID {a}，未找到相关质谱数据")


# ================= 调试入口 =================
if __name__ == '__main__':
    # setup_logger()

    root_dir = r"./../CompoundLibrary"
    save_path, sheet_name = save_chemical_data(root_dir, 55)

    try:
        get_pubcheme_data_by_cas("19895-95-5", save_path, sheet_name)
    except Exception as e:
        logging.error(f"程序异常: {e}", exc_info=True)

    logging.info("=== PubChem 数据抓取完成 ===")
