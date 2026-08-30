import json
import os
import sys
import pymysql

# ====== KONFIGURASI (environment variable) ======
RDS_HOST = os.environ.get("RDS_HOST", "")
RDS_PORT = int(os.environ.get("RDS_PORT", "3306"))
RDS_USER = os.environ.get("RDS_USER", "admin")
RDS_PASSWORD = os.environ.get("RDS_PASSWORD", "")
RDS_DB = os.environ.get("RDS_DB", "mk37c1")
# ================================================

BUAT_TABEL = """CREATE TABLE IF NOT EXISTS hasil_ocr (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_berkas VARCHAR(255) NOT NULL UNIQUE,
    tps VARCHAR(50),
    jumlah_sah INT,
    jumlah_tidak_sah INT,
    detail JSON,
    model VARCHAR(100),
    waktu_ocr DATETIME)"""

def sambung():
    return pymysql.connect(host=RDS_HOST, port=RDS_PORT,
                           user=RDS_USER, password=RDS_PASSWORD,
                           database=RDS_DB)

def siapkan_tabel():
    kn = sambung()
    try:
        with kn.cursor() as ks:
            ks.execute(BUAT_TABEL)
        kn.commit()
    finally:
        kn.close()
    print("tabel hasil_ocr siap di", RDS_DB)

def simpan(nama_berkas, hasil, model):
    """Simpan satu hasil OCR; nama berkas sama -> baris diperbarui."""
    sql = """INSERT INTO hasil_ocr
             (nama_berkas, tps, jumlah_sah, jumlah_tidak_sah, detail,
              model, waktu_ocr)
             VALUES (%s, %s, %s, %s, %s, %s, NOW())
             ON DUPLICATE KEY UPDATE tps=VALUES(tps),
             jumlah_sah=VALUES(jumlah_sah),
             jumlah_tidak_sah=VALUES(jumlah_tidak_sah),
             detail=VALUES(detail), model=VALUES(model), waktu_ocr=NOW()"""
    nilai = (nama_berkas, hasil.get("tps"),
             hasil.get("jumlah_sah", 0), hasil.get("jumlah_tidak_sah", 0),
             json.dumps(hasil, ensure_ascii=False), model)
    kn = sambung()
    try:
        with kn.cursor() as ks:
            ks.execute(sql, nilai)
        kn.commit()
    finally:
        kn.close()
    print("tersimpan di RDS:", nama_berkas)

if __name__ == "__main__":
    if "--dry" in sys.argv:              # uji tanpa database
        print("DRY - SQL yang akan dijalankan:\n", BUAT_TABEL)
        sys.exit()
    if not RDS_HOST or not RDS_PASSWORD:
        sys.exit("Atur RDS_HOST dan RDS_PASSWORD dulu.")
    siapkan_tabel()
