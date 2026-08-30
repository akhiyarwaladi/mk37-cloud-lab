from ocr_c1 import kirim_ocr, simulasi
from simpan_rds import simpan

hasil = simulasi()          # ganti dengan kirim_ocr("scan_c1/c1-plano.jpeg")
simpan("c1-plano.jpeg", hasil, model="simulasi")
