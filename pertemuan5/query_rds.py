import json
import pymysql

# ====== KONFIGURASI (RDS Anda, Langkah 4) ======
RDS_HOST = ""     # endpoint RDS Anda
RDS_USER = "admin"
RDS_PASSWORD = "" # kata sandi Anda
RDS_DB = "mk37c1"
# =============================================

kn = pymysql.connect(host=RDS_HOST, port=3306,
                     user=RDS_USER,
                     password=RDS_PASSWORD,
                     database=RDS_DB)
with kn.cursor() as ks:
    ks.execute("SELECT nama_berkas, tps, jumlah_sah,"
               " jumlah_tidak_sah, model, detail FROM hasil_ocr")
    for baris in ks.fetchall():
        print("Berkas:", baris[0], "| model:", baris[4])
        hasil = json.loads(baris[5])
        for nomor in ("01", "02", "03"):
            print(nomor, hasil.get(f"suara_{nomor}"))
kn.close()
