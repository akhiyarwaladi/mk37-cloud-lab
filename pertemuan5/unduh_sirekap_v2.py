import requests
from pathlib import Path

# ====== KONFIGURASI ======
TPS = "1105072002001"  # TPS 001 Alue Bagok (kode memuat hierarkinya)
# =========================
BASIS = "https://uji-sirekap-obj-data.kpu.go.id/json-public-prod"
FOLDER = Path("scan_c1")
FOLDER.mkdir(exist_ok=True)

def ambil_json(url):
    respon = requests.get(url, timeout=30,
                          headers={"User-Agent": "mk37-kelas/1.0"})
    respon.raise_for_status()
    return respon.json()

tps = ambil_json(f"{BASIS}/pemilu/hhcw/ppwp/11/1105/110507/"
                 f"1105072002/{TPS}.json")
url_foto = tps["images"][0]
print("foto pertama:", url_foto)
binar = requests.get(url_foto, timeout=60,
                     headers={"User-Agent": "mk37-kelas/1.0"}).content
tujuan = FOLDER / f"sirekap-{TPS}-1.jpg"
tujuan.write_bytes(binar)
print("tersimpan:", tujuan, f"({len(binar) // 1024} KB)")
