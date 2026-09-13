import time
from pathlib import Path

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ====== KONFIGURASI ======
URL_KATALOG = "http://books.toscrape.com/"
HALAMAN = 2                # 2 halaman x 20 buku = 40 sampul
FOLDER_SAMPUL = Path("sampul")
FOLDER_BUKTI = Path("bukti")
# =========================

def buka_peramban():
    """Membuka Chrome tanpa tampilan (headless) di EC2."""
    opsi = Options()
    opsi.add_argument("--headless")
    opsi.add_argument("--no-sandbox")
    opsi.add_argument("--disable-dev-shm-usage")
    opsi.add_argument("--window-size=1280,800")
    return webdriver.Chrome(options=opsi)

def unduh(url, tujuan):
    respon = requests.get(url, headers={"User-Agent": "MK37-Praktikum/1.0"}, timeout=15)
    respon.raise_for_status()
    tujuan.write_bytes(respon.content)

if __name__ == "__main__":
    FOLDER_SAMPUL.mkdir(exist_ok=True)
    FOLDER_BUKTI.mkdir(exist_ok=True)
    d = buka_peramban()
    d.get(URL_KATALOG)
    total = baru = 0
    for h in range(1, HALAMAN + 1):
        if h > 1:
            d.find_element(By.CSS_SELECTOR, "li.next a").click()
            time.sleep(1)
        d.save_screenshot(str(FOLDER_BUKTI / f"halaman{h}.png"))
        for kartu in d.find_elements(By.CSS_SELECTOR, "article.product_pod"):
            img = kartu.find_element(By.CSS_SELECTOR, "div.image_container img")
            tujuan = FOLDER_SAMPUL / Path(img.get_attribute("src")).name
            total += 1
            if tujuan.exists():
                continue
            unduh(img.get_attribute("src"), tujuan)
            baru += 1
    d.quit()
    print(f"Buku ditemukan : {total}")
    print(f"Diunduh baru   : {baru}")
    print(f"Folder sampul   : {FOLDER_SAMPUL}/ ({len(list(FOLDER_SAMPUL.glob('*.jpg')))} berkas)")
    print(f"Folder bukti    : {FOLDER_BUKTI}/ ({len(list(FOLDER_BUKTI.glob('*.png')))} berkas)")
