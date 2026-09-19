import pymysql

# ====== KONFIGURASI (RDS Anda, Langkah 3) ======
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
               " jumlah_tidak_sah, model FROM hasil_ocr")
    for baris in ks.fetchall():
        print(baris)
kn.close()
