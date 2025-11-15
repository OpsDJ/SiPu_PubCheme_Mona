import logging
import json
import time
import requests


headers = {
    'User-Agent': 'Mozilla/5.0'
}
def request_with_retry(url, params=None, retries=3, sleep_sec=2):
    proxies = {"http": None, "https": None}

    for attempt in range(1, retries + 1):
        try:
            logging.info(f"[请求] URL={url}, params={params}, 尝试 {attempt}/{retries}")

            resp = requests.get(url, headers=headers, params=params, proxies=proxies, timeout=10)
            resp.raise_for_status()

            logging.info("[请求成功]")
            return json.loads(resp.text)

        except Exception as e:
            logging.warning(f"[请求失败] 第 {attempt} 次：{e}")
            if attempt < retries:
                time.sleep(sleep_sec)
            else:
                logging.error("[请求失败] 已达到最大重试次数")

def parse_mona_data(id):
    url = f"https://mona.fiehnlab.ucdavis.edu/rest/spectra/{id}"

    data = request_with_retry(url)
    if not data:
        return None

    spectrum_value = data.get("spectrum")
    if not spectrum_value:
        logging.warning(f"ID={id} 无 spectrum 字段")
        return None

    spectrum_pairs = []
    for pair in spectrum_value.split():
        mz, intensity = pair.split(":")
        spectrum_pairs.append((float(mz), float(intensity)))

    mz_values = [p[0] for p in spectrum_pairs]
    intensity_values = [p[1] for p in spectrum_pairs]

    collision_energy = None
    precursor_mz = None
    precursor_type = None

    for meta in data.get("metaData", []):
        if meta.get("name") == "collision energy":
            collision_energy = meta.get("value")
        elif meta.get("name") == "precursor m/z":
            precursor_mz = meta.get("value")
        elif meta.get("name") == "precursor type":
            precursor_type = meta.get("value")

    return [mz_values, intensity_values, precursor_mz, collision_energy, precursor_type]
