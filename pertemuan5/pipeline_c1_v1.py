from pathlib import Path
import sys
from ocr_c1 import simulasi
from simpan_rds import (siapkan_tabel, simpan,
                        RDS_HOST, RDS_PASSWORD)

# Cron menjalankan skrip dari folder rumah, maka path di-anchor
# ke lokasi berkas, sama seperti pelajaran waktu_logger.py:
FOLDER = Path(__file__).resolve().parent / "scan_c1"

if not RDS_HOST or not RDS_PASSWORD:
    sys.exit("Isi RDS_HOST dan RDS_PASSWORD "
             "pada simpan_rds.py dulu.")
if not FOLDER.exists():
    sys.exit("Folder scan_c1 tidak ada; jalankan unduh_sirekap.py dulu.")

siapkan_tabel()             # CREATE TABLE dulu
for gambar in sorted(FOLDER.glob("sirekap-*.jpg")):
    print("memproses:", gambar.name)
    simpan(gambar.name, simulasi(), model="simulasi")
