import requests
from ocr_c1 import kirim_ocr

GAMBAR = "scan_c1/sirekap-1105072002001-2.jpg"
URL = ("https://uji-sirekap-obj-data.kpu.go.id"
       "/json-public-prod/pemilu/hhcw/ppwp/11/1105/"
       "110507/1105072002/1105072002001.json")
hasil = kirim_ocr(GAMBAR)
respon = requests.get(URL, timeout=30)
respon.raise_for_status()
chart = respon.json()["chart"]
for nomor, kode in [("01", "100025"), ("02", "100026"),
                    ("03", "100027")]:
    ai = hasil[f"suara_{nomor}"]
    pembanding = chart.get(kode)
    print(nomor, "AI:", ai, "Sirekap:", pembanding)
    if ai is None or pembanding is None:
        print("  BELUM LENGKAP: periksa foto.")
    elif ai != pembanding:
        print("  BERBEDA: periksa angka dan terbilang.")
    else:
        print("  Cocok; periksa identitas secara manual.")
