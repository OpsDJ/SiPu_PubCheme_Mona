import logging

from .FindElementPubcheme import *


def parese_pubchem_detail(data):
    """
    解析PubChem数据库返回的LC-MS详细数据，提取特定仪器类型的数据

    该函数从PubChem返回的复杂JSON数据中提取Accession ID、MoNA ID、碰撞能量、
    保留时间、前体离子m/z和仪器类型等信息，并筛选出仅包含QTOF仪器类型的数据

    Args:
        data (dict): PubChem数据库返回的LC-MS详细信息JSON数据

    Returns:
        tuple: 包含四个列表的元组
            - ids (list): Accession ID和MoNA ID的合并列表
            - collision_energy (list): 碰撞能量值列表
            - retention_time (list): 保留时间值列表
            - precursor_mz (list): 前体离子m/z值列表
    """

    # 提取各种所需信息
    acc_ids = find_all_acc_ids(data)
    mona_ids = find_all_mona_ids(data)
    ids = acc_ids + mona_ids
    collision_energy = find_all_cenergy(data)
    retention_time = find_all_rt(data)
    precursor_mz = find_all_pm(data)
    instrument_type = find_all_instrument_type(data)

    # 查找所有不包含QTOF(不区分大小写)的元素位置，并删除这些位置的所有相关数据
    remove_indices = []
    for idx, inst_type in enumerate(instrument_type):
        if 'QTOF' not in inst_type.upper():
            remove_indices.append(idx)

    # 从后往前删除，避免索引变化影响
    for idx in reversed(remove_indices):
        logging.info(f"删除位置 {idx} 的元素: {instrument_type[idx]}")
        del instrument_type[idx]
        if idx < len(ids):
            del ids[idx]
        if idx < len(collision_energy):
            del collision_energy[idx]
        if idx < len(retention_time):
            del retention_time[idx]
        if idx < len(precursor_mz):
            del precursor_mz[idx]
    # if not remove_indices:
    #     print("所有仪器类型都包含QTOF")
    # else:
    #     print(f"共删除 {len(remove_indices)} 个不包含QTOF的元素")

    return ids, collision_energy, retention_time, precursor_mz
