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
WILAYAH = "https://uji-sirekap-obj-data.kpu.go.id/json-public-prod/wilayah/pemilu/ppwp"
DATA = "https://uji-sirekap-obj-data.kpu.go.id/json-public-prod/pemilu"
FOLDER = Path("scan_c1")
def ambil_json(url):
    respon = requests.get(url, timeout=30,
                          headers={"User-Agent": "mk37-kelas/1.0"})
    respon.raise_for_status()
    return respon.json()
runtun = [PROV, KAB, KEC, KEL, TPS]
for i, kode in enumerate(runtun):   # tiap kode harus ada di induknya
    induk = "/".join(runtun[:i]) if i else "0"
    anak = ambil_json(f"{WILAYAH}/{induk}.json")
    assert any(str(x["kode"]) == kode for x in anak)
    print(f"tingkat {i + 1}: {kode} OK")
info = ambil_json(f"{DATA}/hhcw/ppwp/{PROV}/{KAB}/{KEC}/{KEL}/{TPS}.json")
print("suara (chart):", info.get("chart"))
FOLDER.mkdir(exist_ok=True)
for j, url in enumerate(info.get("images", []), 1):
    tujuan = FOLDER / f"sirekap-{TPS}-{j}.jpg"
    if tujuan.exists():
        print("sudah ada, lewati:", tujuan.name)
        continue
    binar = requests.get(url, timeout=60,
                         headers={"User-Agent": "mk37-kelas/1.0"}).content
    tujuan.write_bytes(binar)
    print("tersimpan:", tujuan, f"({len(binar) // 1024} KB)")
    time.sleep(1)
