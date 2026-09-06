import requests
from pathlib import Path

# ====== KONFIGURASI ======
URL = ("https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
       "static/datasets/C1-plano-original.jpeg")
# =========================

FOLDER = Path("scan_c1")
FOLDER.mkdir(exist_ok=True)
tujuan = FOLDER / "c1-plano.jpeg"
respon = requests.get(URL, timeout=30,
                      headers={"User-Agent": "mk37-kelas/1.0"})
respon.raise_for_status()
tujuan.write_bytes(respon.content)
print("tersimpan:", tujuan, f"({len(respon.content) // 1024} KB)")
