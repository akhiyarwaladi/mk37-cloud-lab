import json
import re
import time
from pathlib import Path

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ====== KONFIGURASI ======
KANAL = {
    "news": "https://news.detik.com/",
    "sepakbola": "https://sport.detik.com/sepakbola",
    "seleb": "https://hot.detik.com/",
}
BATAS_ARTIKEL = 3
FOLDER = Path("berita")
FOLDER_IMG = FOLDER / "img"
POLA_ID = re.compile(r"/d-(\d+)")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
# =========================

def buka():
    """Buka peramban headless dengan batas waktu muat 40 detik."""
    opsi = Options()
    opsi.page_load_strategy = "eager"
    opsi.add_argument("--headless")
    opsi.add_argument("--no-sandbox")
    opsi.add_argument("--disable-dev-shm-usage")
    opsi.add_argument("--window-size=1280,800")
    opsi.add_argument(f"--user-agent={UA}")
    d = webdriver.Chrome(options=opsi)
    d.set_page_load_timeout(40)
    return d

def daftar_artikel(d, url):
    """Ambil URL artikel satu kanal (daftar kosong bila kanal macet)."""
    try:
        d.get(url)
        WebDriverWait(d, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/d-"]')))
    except Exception as e:
        print(f"  [!] kanal macet ({type(e).__name__}), dilewati")
        return []
    return d.execute_script("""return [...new Set(
      [...document.querySelectorAll('a[href*="/d-"]')]
        .filter(a => a.href.startsWith(arguments[0]))
        .map(a => a.href))].slice(0, arguments[1]);""", url, BATAS_ARTIKEL)

def baca_artikel(d, kanal, url):
    """Ambil judul, gambar utama, dan isi satu artikel (None bila gagal).

    Halaman berita nyata kadang macet (iklan berat): kegagalan apa pun
    Dilewati dan dihitung, bukan menghentikan seluruh perayapan."""
    try:
        d.get(url)
        time.sleep(1)
        d.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        judul = d.execute_script("return document.querySelector('h1').innerText").strip()
        gambar = d.execute_script("var i=document.querySelector('.detail__media img'); return i ? i.src : ''")
        paragraf = d.execute_script(
            "return [...document.querySelectorAll('.detail__body-text p')]"
            ".map(p => p.innerText.trim()).filter(t => t.length > 0)")
    except Exception as e:
        print(f"  [!] lewati (macet: {type(e).__name__}): {url[:70]}")
        return None
    if not judul or not paragraf:
        print(f"  [!] lewati (kosong): {url[:70]}")
        return None
    nama_img = ""
    if gambar:
        nama_img = f"{kanal}-{POLA_ID.search(url).group(1)}.jpg"
        foto = requests.get(gambar, headers={"User-Agent": UA}, timeout=15)
        foto.raise_for_status()
        (FOLDER_IMG / nama_img).write_bytes(foto.content)
    return {"kanal": kanal, "judul": judul, "url": url, "gambar": gambar,
            "nama_img": nama_img, "paragraf": len(paragraf), "isi": "\n\n".join(paragraf)}

if __name__ == "__main__":
    FOLDER_IMG.mkdir(parents=True, exist_ok=True)
    d = buka()
    semua, lewat = [], 0
    for nama, url in KANAL.items():
        dapat = 0
        for link in daftar_artikel(d, url):
            artikel = baca_artikel(d, nama, link)
            if artikel is None:
                lewat += 1
                continue
            semua.append(artikel)
            dapat += 1
        print(f"Kanal {nama:10s}: {dapat} berita")
    d.quit()
    (FOLDER / "berita.json").write_text(
        json.dumps(semua, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Total          : {len(semua)} berita (lewat: {lewat})")
    print(f"JSON           : berita.json")
    print(f"Folder gambar  : img/ ({len(list(FOLDER_IMG.glob('*.jpg')))} berkas)")
