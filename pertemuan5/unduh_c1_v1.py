import requests
from pathlib import Path

# ====== KONFIGURASI ======
DASAR = ("https://raw.githubusercontent.com"
         "/kawalc1/kawalc1/master")
URL = DASAR + "/static/datasets/C1-plano-original.jpeg"
# =========================

KEPALA = {"User-Agent": "mk37-kelas/1.0"}  # identitas sopan

FOLDER = Path("scan_c1")
FOLDER.mkdir(exist_ok=True)
tujuan = FOLDER / "c1-plano.jpeg"
respon = requests.get(URL, timeout=30, headers=KEPALA)
respon.raise_for_status()
tujuan.write_bytes(respon.content)
ukuran = len(respon.content) // 1024
print("tersimpan:", tujuan, f"({ukuran} KB)")
