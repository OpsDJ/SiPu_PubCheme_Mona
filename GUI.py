import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from sipu import GetDetailsInfo, SaveData, GetBasicInfo
from pucheme import GetPubcheme
from mona import GetMonaInfo
from CreateFilePath import *

root_dir = r"./CompoundLibrary"


# ====================== 日志配置 ======================
def setup_logger():
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
        return [line.strip() for line in f.readlines()]


def clean_illegal_chars(value):
    if isinstance(value, str):
        return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', '', value)
    return value


# ====================== 修改后的爬取函数 ======================
def get_sipu_data(cat_id, unique_id, stop_flag, pause_flag):
    if stop_flag:
        logging.info(f"[停止] cat_id={cat_id}, unique_id={unique_id}")
        return None, None
    pause_flag.wait()
    try:
        chemical_data = GetDetailsInfo.get_detail_url(unique_id)
        pause_flag.wait()
        if stop_flag:
            logging.info(f"[停止] cat_id={cat_id}, unique_id={unique_id}")
            return None, None
        chemical_data = {k: clean_illegal_chars(v) for k, v in chemical_data.items()}
        SaveData.save_chemical_data(root_dir, cat_id, chemical_data, image_filename=f'{unique_id}.jpg')
        return chemical_data.get("CAS号"), chemical_data.get("英文名")
    except Exception as e:
        logging.error(f"[失败] cat_id={cat_id}, unique_id={unique_id}, 错误: {e}", exc_info=True)
        return None, None


def get_pucheme_data(cas_num, cat_id, stop_flag, pause_flag):
    save_path, sheet_name = GetPubcheme.save_chemical_data(root_dir, cat_id)
    if stop_flag: return
    pause_flag.wait()
    try:
        GetPubcheme.get_pubcheme_data_by_cas(cas_num, save_path, sheet_name)
    except Exception as ex:
        logging.error(f"程序异常: {ex}", exc_info=True)
    logging.info("=== PubChem 数据抓取完成 ===")


def get_mona_data(structure_name, cat_id, stop_flag, pause_flag):
    if stop_flag: return
    pause_flag.wait()
    GetMonaInfo.search_mona(structure_name, root_dir=root_dir, cat_id=cat_id)


# ====================== GUI 界面 ======================
class ChemicalScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("化学数据爬取工具")
        self.root.geometry("800x500")

        self.stop_flag = False
        self.pause_flag = threading.Event()
        self.pause_flag.set()

        frame_top = tk.Frame(root)
        frame_top.pack(pady=10)
        tk.Label(frame_top, text="输入分类ID (cat_id, 用逗号分隔)：").pack(side=tk.LEFT)
        self.cat_id_var = tk.StringVar()
        self.cat_id_entry = tk.Entry(frame_top, textvariable=self.cat_id_var, width=50)
        self.cat_id_entry.pack(side=tk.LEFT, padx=5)
        self.cat_id_var.set("54,55,56,57")  # 默认值

        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)
        self.start_btn = tk.Button(frame_btn, text="开始", command=self.start_scraping)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        self.stop_btn = tk.Button(frame_btn, text="停止", command=self.stop_scraping)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        self.pause_btn = tk.Button(frame_btn, text="暂停", command=self.toggle_pause)
        self.pause_btn.pack(side=tk.LEFT, padx=5)

        self.log_text = scrolledtext.ScrolledText(root, width=100, height=25, state='disabled')
        self.log_text.pack(pady=10)

        self.setup_gui_logger()

    def setup_gui_logger(self):
        class TextHandler(logging.Handler):
            def __init__(self, text_widget):
                super().__init__()
                self.text_widget = text_widget

            def emit(self, record):
                msg = self.format(record)
                self.text_widget.configure(state='normal')
                self.text_widget.insert(tk.END, msg + '\n')
                self.text_widget.configure(state='disabled')
                self.text_widget.see(tk.END)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        text_handler = TextHandler(self.log_text)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        text_handler.setFormatter(formatter)
        logger.addHandler(text_handler)

    def start_scraping(self):
        self.stop_flag = False
        self.pause_flag.set()
        # 清空日志
        self.log_text.configure(state='normal')
        self.log_text.delete('1.0', tk.END)
        self.log_text.configure(state='disabled')

        try:
            cat_id_list = [int(i.strip()) for i in self.cat_id_var.get().split(",") if i.strip().isdigit()]
        except Exception:
            messagebox.showerror("错误", "分类ID输入不正确，请输入逗号分隔的数字")
            return

        def run():
            for cat_id in cat_id_list:
                for unique_id in get_unique_id_list(cat_id):
                    # 每步都检查停止标志
                    if self.stop_flag:
                        logging.info("爬取已停止")
                        return

                    # 每步都等待暂停/继续
                    self.pause_flag.wait()
                    if not self.pause_flag.is_set():
                        logging.info("爬取已暂停")
                        self.pause_flag.wait()  # 阻塞直到继续
                        logging.info("爬取已继续")

                    cas_num, eng_name = get_sipu_data(cat_id, unique_id, self.stop_flag, self.pause_flag)
                    if self.stop_flag or cas_num is None:
                        logging.info("爬取已停止")
                        return

                    get_pucheme_data(cas_num, cat_id, self.stop_flag, self.pause_flag)
                    get_mona_data(eng_name, cat_id, self.stop_flag, self.pause_flag)

            logging.info("爬取线程结束")

        threading.Thread(target=run, daemon=True).start()

    def stop_scraping(self):
        self.stop_flag = True
        self.pause_flag.set()
        logging.info("正在停止爬取...")

    def toggle_pause(self):
        if self.pause_flag.is_set():
            self.pause_flag.clear()
            self.pause_btn.config(text="继续")
            logging.info("爬取已暂停")
        else:
            self.pause_flag.set()
            self.pause_btn.config(text="暂停")
            logging.info("爬取已继续")


# ====================== 程序入口 ======================
if __name__ == "__main__":
    setup_logger()
    logging.info("=== 程序启动 ===")
    create_folders(data, root_dir)
    logging.info("文件夹结构已全部创建完成！")
    logging.info("正在获取思普数据库的基本信息..")
    GetBasicInfo.start()
    logging.info("获取思普数据库的基本信息完成！..")
    root = tk.Tk()
    gui = ChemicalScraperGUI(root)
    root.mainloop()
