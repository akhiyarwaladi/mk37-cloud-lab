import requests
from pathlib import Path

# ====== KONFIGURASI ======
TPS = "1105072002001"  # TPS 001 Alue Bagok
# =========================
BASIS = ("https://uji-sirekap-obj-data.kpu.go.id"
         "/json-public-prod")
FOLDER = Path("scan_c1")
KEPALA = {"User-Agent": "mk37-kelas/1.0"}
FOLDER.mkdir(exist_ok=True)

def ambil_json(url):
    respon = requests.get(url, timeout=30, headers=KEPALA)
    respon.raise_for_status()
    return respon.json()

tps = ambil_json(f"{BASIS}/pemilu/hhcw/ppwp/11/1105/110507/"
                 f"1105072002/{TPS}.json")
url_foto = tps["images"][1]  # indeks 1 = foto kedua
print("foto suara calon:", url_foto)
unduhan = requests.get(url_foto, timeout=60, headers=KEPALA)
tujuan = FOLDER / f"sirekap-{TPS}-2.jpg"
unduhan.raise_for_status()
tujuan.write_bytes(unduhan.content)
ukuran = len(unduhan.content) // 1024
print("tersimpan:", tujuan, f"({ukuran} KB)")
