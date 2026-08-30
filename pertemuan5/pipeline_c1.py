from pathlib import Path
import sys
from ocr_c1 import kirim_ocr
from simpan_rds import simpan

# Cron menjalankan skrip dari folder rumah, maka path di-anchor
# ke lokasi berkas, sama seperti pelajaran waktu_logger.py:
FOLDER = Path(__file__).resolve().parent / "scan_c1"

if not FOLDER.exists():
    sys.exit("Folder scan_c1 tidak ada; jalankan unduh_c1.py dulu.")

berhasil = 0
for gambar in sorted(FOLDER.iterdir()):
    print("memproses:", gambar.name)
    try:
        hasil = kirim_ocr(gambar)
        simpan(gambar.name, hasil, model="ocr-ai")
        berhasil += 1
    except Exception as galat:
        print("  gagal, lanjut berikutnya:", galat)
print(f"Selesai: {berhasil} formulir tersimpan.")
