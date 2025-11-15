from datetime import datetime
from sipu import GetDetailsInfo, SaveData
from pucheme import GetPubcheme
from mona import GetMonaInfo
from CreateFilePath import *
root_dir = r"./CompoundLibrary"


# ====================== 日志配置 ======================
def setup_logger():
    """初始化日志记录"""
    log_dir = os.path.join("logs")
    os.makedirs(log_dir, exist_ok=True)
    log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")
    log_path = os.path.join(log_dir, log_filename)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        encoding='utf-8'
    )

    # 同时在控制台输出
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    logging.getLogger().addHandler(console)


# ====================== 工具函数 ======================
def get_unique_id_list(cat_id):
    id_path_map = SaveData.get_id_path_map(root_dir)
    save_path = id_path_map.get(cat_id)
    main_path = os.path.join(save_path, "id", "compound_ids.txt")
    with open(main_path, "r", encoding="utf-8") as f:
        unique_id_list = [line.strip() for line in f.readlines()]
    return unique_id_list


def clean_illegal_chars(value):
    """去除 Excel 不支持的非法字符"""
    if isinstance(value, str):
        return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', '', value)
    return value


# ====================== 主逻辑函数 ======================
def get_sipu_data(cat_id, unique_id):
    try:
        chemical_data = GetDetailsInfo.get_detail_url(unique_id)
        chemical_data = {k: clean_illegal_chars(v) for k, v in chemical_data.items()}
        SaveData.save_chemical_data(root_dir, cat_id, chemical_data, image_filename=f'{unique_id}.jpg')
        return chemical_data.get("CAS号"), chemical_data.get("英文名")
    except Exception as e:
        logging.error(f"[失败] cat_id={cat_id}, unique_id={unique_id}, 错误: {e}", exc_info=True)


def get_pucheme_data(cas_num, cat_id):
    save_path, sheet_name = GetPubcheme.save_chemical_data(root_dir, cat_id)

    try:
        GetPubcheme.get_pubcheme_data_by_cas(cas_num, save_path, sheet_name)
    except Exception as ex:
        logging.error(f"程序异常: {ex}", exc_info=True)

    logging.info("=== PubChem 数据抓取完成 ===")


def get_mona_data(structure_name, cat_id):
    GetMonaInfo.search_mona(structure_name, root_dir=root_dir, cat_id=cat_id)

# 已完成 54
def start():
    cat_id_list = [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 7, 8, 9, 10, 11, 12, 13]
    for cat_id in cat_id_list:
        unique_id_list = get_unique_id_list(cat_id)
        for unique_id in unique_id_list:
            logging.info(f"爬取思普数据库-----> cat_id={cat_id}, unique_id={unique_id}")
            cas_num, eng_name = get_sipu_data(cat_id=cat_id, unique_id=unique_id)
            logging.info(f"爬取思普数据库完成！-----> cat_id={cat_id}, unique_id={unique_id}")
            logging.info(f"爬取PubCheme数据库-----> cas_num={cas_num}, cat_id={cat_id}")
            get_pucheme_data(cas_num, cat_id)
            logging.info(f"爬取PubCheme数据库完成！-----> cas_num={cas_num}, cat_id={cat_id}")
            get_mona_data(eng_name, cat_id)
        break


if __name__ == '__main__':
    setup_logger()
    logging.info("=== 程序启动 ===")
    create_folders(data, root_dir)
    logging.info("文件夹结构已全部创建完成！")
    try:
        start()
    except Exception as e:
        logging.critical(f"程序崩溃: {e}", exc_info=True)
    logging.info("=== 程序结束 ===")
