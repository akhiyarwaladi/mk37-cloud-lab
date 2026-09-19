from ocr_c1 import simulasi
from simpan_rds import siapkan_tabel, simpan

siapkan_tabel()             # CREATE TABLE dulu
hasil = simulasi()  # ganti dengan kirim_ocr(gambar)
simpan("c1-plano.jpeg", hasil, model="simulasi")
