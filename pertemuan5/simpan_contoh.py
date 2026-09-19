from ocr_c1 import simulasi
from simpan_rds import siapkan_tabel, simpan

siapkan_tabel()             # CREATE TABLE dulu: database + tabel siap
hasil = simulasi()          # ganti dengan kirim_ocr("scan_c1/c1-plano.jpeg")
simpan("c1-plano.jpeg", hasil, model="simulasi")
