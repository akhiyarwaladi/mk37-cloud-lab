from ocr_c1 import simulasi
from simpan_rds import siapkan_tabel, simpan

siapkan_tabel()             # CREATE TABLE dulu
hasil = simulasi()  # ganti dengan kirim_ocr(gambar)
simpan("sirekap-1105072002001-2.jpg", hasil,
       model="simulasi")
