import requests
import time
from pathlib import Path

# ====== KONFIGURASI ======
FOLDER = Path("scan_c1")
DAFTAR = {
    "c1-plano.jpeg":
        "https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
        "static/datasets/C1-plano-original.jpeg",
    "c1-pilpres-1.jpg":
        "https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
        "static/contoh-pilpres-2019/1.JPG",
    "c1-pilgub-1.jpg":
        "https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
        "static/contoh-pilgub/1.jpeg",
}
# =========================

FOLDER.mkdir(exist_ok=True)
for nama, url in DAFTAR.items():
    tujuan = FOLDER / nama
    if tujuan.exists():                  # idempoten: tidak mengunduh ulang
        print("sudah ada, lewati:", nama)
        continue
    print("mengunduh:", url)
    respon = requests.get(url, timeout=30,
                          headers={"User-Agent": "mk37-kelas/1.0"})
    respon.raise_for_status()
    tujuan.write_bytes(respon.content)
    print("  tersimpan:", tujuan, f"({len(respon.content) // 1024} KB)")
    time.sleep(1)                        # sopan: beri jeda antar unduhan
print("Selesai. Isi folder scan_c1:")
for f in sorted(FOLDER.iterdir()):
    print(" -", f.name)
