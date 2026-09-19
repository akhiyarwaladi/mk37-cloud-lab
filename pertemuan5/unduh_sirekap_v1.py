import requests

# ====== KONFIGURASI ======
TPS = "1105072002001"  # TPS 001 Alue Bagok
# =========================
BASIS = ("https://uji-sirekap-obj-data.kpu.go.id"
         "/json-public-prod")
KEPALA = {"User-Agent": "mk37-kelas/1.0"}

def ambil_json(url):
    respon = requests.get(url, timeout=30, headers=KEPALA)
    respon.raise_for_status()
    return respon.json()

prov = ambil_json(f"{BASIS}/wilayah/pemilu/ppwp/0.json")
print("provinsi:", len(prov), "| contoh:", prov[0]["nama"])
tps = ambil_json(f"{BASIS}/pemilu/hhcw/ppwp/11/1105/110507/"
                 f"1105072002/{TPS}.json")
print("chart:", tps.get("chart"))
print("foto:", len(tps.get("images", [])))
