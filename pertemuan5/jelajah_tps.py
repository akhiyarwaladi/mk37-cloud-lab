import requests

BASIS = ("https://uji-sirekap-obj-data.kpu.go.id"
         "/json-public-prod")
WILAYAH = BASIS + "/wilayah/pemilu/ppwp"
KEPALA = {"User-Agent": "mk37-kelas/1.0"}
KEL = "1105072002"     # Alue Bagok

def ambil_json(url):
    respon = requests.get(url, timeout=30, headers=KEPALA)
    respon.raise_for_status()
    return respon.json()

daftar = ambil_json(f"{WILAYAH}/11/1105/110507/"
                    f"{KEL}.json")
for t in daftar:
    print(t["kode"], t["nama"])
