import os
import json
import re
import logging

# ========== 日志配置 ==========
# log_dir = "log"
# os.makedirs(log_dir, exist_ok=True)
# log_file = os.path.join(log_dir, "logs.log")
#
# logging.basicConfig(
#     filename=log_file,
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     encoding="utf-8"
# )

# ========== JSON 数据 ==========
json_str = '''[{"id":0,"title":"结构类型化合物库","ParentID":0,"children":[{"id":2,"title":"Isoprenoids (异戊烯类化合物)","ParentID":0,"children":[{"id":14,"title":"Terpenoids (萜类化合物)","ParentID":2,"children":[{"id":54,"title":"Monoterpenoids (单萜类)","ParentID":14,"children":[]},{"id":55,"title":"Sesquiterpenoids (倍半萜类)","ParentID":14,"children":[]},{"id":56,"title":"Diterpenoids (二萜类)","ParentID":14,"children":[]},{"id":57,"title":"Triterpenoids (三萜类)","ParentID":14,"children":[]},{"id":58,"title":"Other Terpenoids (其他萜类化合物)","ParentID":14,"children":[]}]},{"id":15,"title":"Steroids (甾体化合物)","ParentID":2,"children":[{"id":59,"title":"Cardenolides and its Sapogenins (强心苷及其苷元类)","ParentID":15,"children":[]},{"id":60,"title":"Steroid Saponins and its Sapogenins(甾体皂苷及其苷元类）","ParentID":15,"children":[]},{"id":61,"title":"Other Steroids(其他甾体化合物）","ParentID":15,"children":[]}]}]},{"id":3,"title":"Nitrogen-containing Compounds (含氮化合物)","ParentID":0,"children":[{"id":16,"title":"Alkaloids (生物碱类)","ParentID":3,"children":[{"id":62,"title":"Pyrrolines (吡咯类生物碱)","ParentID":16,"children":[]},{"id":63,"title":"Piperidines (哌啶类生物碱)","ParentID":16,"children":[]},{"id":64,"title":"Quinolines/Isoquinolines(喹啉/异喹啉类生物碱）","ParentID":16,"children":[]},{"id":65,"title":"Indoles(吲哚类生物碱）","ParentID":16,"children":[]},{"id":67,"title":"Tropanes(托品烷类生物碱）","ParentID":16,"children":[]},{"id":68,"title":"Other Alkaloids(其他生物碱类)","ParentID":16,"children":[]}]},{"id":17,"title":"Amides (酰胺类)","ParentID":3,"children":[]},{"id":18,"title":"Amines (胺类)","ParentID":3,"children":[]},{"id":19,"title":"Amino Acids/Peptides(氨基酸/肽类)","ParentID":3,"children":[]},{"id":20,"title":"Cyanoglycosides (氰苷类)","ParentID":3,"children":[]},{"id":21,"title":"Nucleosides/Nucleotide (核苷/核苷酸类)","ParentID":3,"children":[]},{"id":22,"title":"Other Nitrogen-containing Compounds(其他含氮化合物)","ParentID":3,"children":[]}]},{"id":4,"title":"Phenylpropanoids(苯丙素类)","ParentID":0,"children":[{"id":23,"title":"Simple Phenylpropanoids(简单苯丙素类)","ParentID":4,"children":[]},{"id":24,"title":"Coumarins (香豆素类)","ParentID":4,"children":[]},{"id":25,"title":"Lignanoids (木脂素类)","ParentID":4,"children":[]},{"id":26,"title":"Other Phenylpropanoids(其他苯丙素类)","ParentID":4,"children":[]}]},{"id":5,"title":"Flavonoids (黄酮类)","ParentID":0,"children":[{"id":27,"title":"Flavanes/Isoflavans/Flavanols(黄烷类/异黄烷类/黄烷醇类) ","ParentID":5,"children":[]},{"id":28,"title":"Flavones/Flavanones (黄酮类/二氢黄酮类)","ParentID":5,"children":[]},{"id":29,"title":"Flavonols/Flavanonols (黄酮醇类/二氢黄酮醇类)","ParentID":5,"children":[]},{"id":30,"title":"Isoflavones/Isoflavanones (异黄酮类/二氢异黄酮类)","ParentID":5,"children":[]},{"id":31,"title":"Chalcones/Dihydrochalcones (查耳酮类/二氢查耳酮类)","ParentID":5,"children":[]},{"id":32,"title":"Aurones (橙酮类)","ParentID":5,"children":[]},{"id":33,"title":"Bisflavones (双黄酮类)","ParentID":5,"children":[]},{"id":34,"title":"Neoflavonoids (新黄酮)","ParentID":5,"children":[]},{"id":35,"title":"Xanthones (呫吨酮类)","ParentID":5,"children":[]},{"id":36,"title":"Anthocyanins (花色素类)","ParentID":5,"children":[]},{"id":37,"title":"Chromones (色原酮类)","ParentID":5,"children":[]},{"id":38,"title":"Other Flavonoids(其他黄酮类)","ParentID":5,"children":[]}]},{"id":6,"title":"Phenolic Compounds (酚类化合物)","ParentID":0,"children":[{"id":39,"title":"Simple Phenolic Compounds (简单酚类化合物)","ParentID":6,"children":[]},{"id":40,"title":"Phenylethanoids(苯乙醇类）","ParentID":6,"children":[]},{"id":41,"title":"Stilbenes(二苯乙烯类）","ParentID":6,"children":[]},{"id":42,"title":"Tannins(鞣质）","ParentID":6,"children":[]},{"id":43,"title":"Other Phenolic Compounds (其他酚类化合物)","ParentID":6,"children":[]}]},{"id":7,"title":"Quinones (醌类)","ParentID":0,"children":[]},{"id":8,"title":"Aliphatic Compounds (脂族化合物)","ParentID":0,"children":[]},{"id":10,"title":"Carbohydrates (糖类)","ParentID":0,"children":[]},{"id":12,"title":"Glucosinolates (芥子油苷类)","ParentID":0,"children":[]},{"id":13,"title":"Other Compounds (其他类型化合物)","ParentID":0,"children":[]}]},{"id":-1,"title":"来源库","ParentID":-1,"children":[]}]'''
data = json.loads(json_str)

# ========== 根目录 ==========
root_dir = r"./CompoundLibrary"


# ========== 工具函数 ==========
def safe_folder_name(name: str) -> str:
    """清理文件夹名称中的非法字符与多余空格"""
    name = name.strip()
    name = re.sub(r'[\\/:*?"<>|]', '／', name)  # 替换 Windows 非法字符
    return name


def create_folders(items, parent_path):
    """递归创建文件夹并记录日志"""
    for item in items:
        folder_name = f"{item['id']}_{item['title']}"
        folder_name = safe_folder_name(folder_name)
        path = os.path.join(parent_path, folder_name)

        try:
            os.makedirs(path, exist_ok=True)
            logging.info(f"创建主文件夹: {path}")
        except Exception as e:
            logging.error(f"创建主文件夹失败: {path} | 错误: {e}")
            continue

        if item.get("children"):
            create_folders(item["children"], path)
        else:
            # 创建 img、id和doc 子文件夹
            for sub_folder in ["img", "id", "doc"]:
                sub_path = os.path.join(path, sub_folder)
                try:
                    os.makedirs(sub_path, exist_ok=True)
                    logging.info(f"创建子文件夹: {sub_path}")
                except Exception as e:
                    logging.error(f"创建子文件夹失败: {sub_path} | 错误: {e}")

if __name__ == '__main__':

    create_folders(data, root_dir)