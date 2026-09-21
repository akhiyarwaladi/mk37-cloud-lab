import requests
import time
from pathlib import Path

# ====== KONFIGURASI: kode wilayah TPS target ======
PROV = "11"            # Aceh
KAB = "1105"           # Aceh Barat
KEC = "110507"         # Arongan Lambalek
KEL = "1105072002"     # Alue Bagok
TPS = "1105072002001"  # TPS 001
# ==================================================
BASIS = ("https://uji-sirekap-obj-data.kpu.go.id"
         "/json-public-prod")
WILAYAH = BASIS + "/wilayah/pemilu/ppwp"
DATA = BASIS + "/pemilu"
FOLDER = Path("scan_c1")
KEPALA = {"User-Agent": "mk37-kelas/1.0"}

def ambil_json(url):
    respon = requests.get(url, timeout=30, headers=KEPALA)
    respon.raise_for_status()
    return respon.json()

runtun = [PROV, KAB, KEC, KEL, TPS]
for i, kode in enumerate(runtun):   # kode ada di induknya
    induk = "/".join(runtun[:i]) if i else "0"
    anak = ambil_json(f"{WILAYAH}/{induk}.json")
    ketemu = any(str(x["kode"]) == kode for x in anak)
    assert ketemu, f"kode {kode} tidak ditemukan di induknya"
    print(f"tingkat {i + 1}: {kode} OK")
info = ambil_json(f"{DATA}/hhcw/ppwp/{PROV}/{KAB}"
                  f"/{KEC}/{KEL}/{TPS}.json")
print("suara (chart):", info.get("chart"))
FOLDER.mkdir(exist_ok=True)
for j, url in enumerate(info.get("images", []), 1):
    tujuan = FOLDER / f"sirekap-{TPS}-{j}.jpg"
    if tujuan.exists():
        print("sudah ada, lewati:", tujuan.name)
        continue
    unduhan = requests.get(url, timeout=60, headers=KEPALA)
    unduhan.raise_for_status()
    tujuan.write_bytes(unduhan.content)
    ukuran = len(unduhan.content) // 1024
    print("tersimpan:", tujuan, f"({ukuran} KB)")
    time.sleep(1)  # sopan pada sumber KPU
