import os

save_path = r"./CompoundLibrary\0_结构类型化合物库\2_Isoprenoids (异戊烯类化合物)\14_Terpenoids (萜类化合物)\倍半萜类.csv"
download_path = os.path.dirname(save_path)
doc_folder = os.path.join(download_path, "doc")

# 打印绝对路径
doc_folder_abs = os.path.abspath(doc_folder)
print(f"绝对路径：{doc_folder_abs}")

# 创建文件夹
os.makedirs(doc_folder_abs, exist_ok=True)
