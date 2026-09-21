from pathlib import Path
from ocr_c1 import kirim_ocr, MODEL
from simpan_rds import siapkan_tabel, simpan

GAMBAR = Path("scan_c1/sirekap-1105072002001-2.jpg")
siapkan_tabel()
hasil = kirim_ocr(GAMBAR)
simpan(GAMBAR.name, hasil, model=MODEL)
