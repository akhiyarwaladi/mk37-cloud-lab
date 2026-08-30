from pathlib import Path
from ocr_c1 import kirim_ocr
from simpan_rds import simpan

for gambar in sorted(Path("scan_c1").iterdir()):
    print("memproses:", gambar.name)
    hasil = kirim_ocr(gambar)
    simpan(gambar.name, hasil, model="ocr-ai")
