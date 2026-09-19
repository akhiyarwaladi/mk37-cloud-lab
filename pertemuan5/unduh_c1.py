import requests
import time
from pathlib import Path

# ====== KONFIGURASI ======
FOLDER = Path("scan_c1")
DASAR = ("https://raw.githubusercontent.com"
         "/kawalc1/kawalc1/master")
DAFTAR = {
    "c1-plano.jpeg":
        DASAR + "/static/datasets/C1-plano-original.jpeg",
    "c1-pilpres-1.jpg":
        DASAR + "/static/contoh-pilpres-2019/1.JPG",
    "c1-pilgub-1.jpg":
        DASAR + "/static/contoh-pilgub/1.jpeg",
}
# =========================

KEPALA = {"User-Agent": "mk37-kelas/1.0"}  # identitas sopan
FOLDER.mkdir(exist_ok=True)
for nama, url in DAFTAR.items():
    tujuan = FOLDER / nama
    if tujuan.exists():      # idempoten: lewati bila sudah ada
        print("sudah ada, lewati:", nama)
        continue
    print("mengunduh:", url)
    respon = requests.get(url, timeout=30, headers=KEPALA)
    respon.raise_for_status()
    tujuan.write_bytes(respon.content)
    ukuran = len(respon.content) // 1024
    print("  tersimpan:", tujuan, f"({ukuran} KB)")
    time.sleep(1)  # sopan: jeda antar unduhan
print("Selesai. Isi folder scan_c1:")
for f in sorted(FOLDER.iterdir()):
    print(" -", f.name)
