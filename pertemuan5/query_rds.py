import os
import pymysql

kn = pymysql.connect(host=os.environ["RDS_HOST"],
                     port=int(os.environ.get("RDS_PORT", "3306")),
                     user=os.environ.get("RDS_USER", "admin"),
                     password=os.environ["RDS_PASSWORD"],
                     database=os.environ.get("RDS_DB", "mk37c1"))
with kn.cursor() as ks:
    ks.execute("SELECT nama_berkas, tps, jumlah_sah, jumlah_tidak_sah, "
               "model FROM hasil_ocr")
    for baris in ks.fetchall():
        print(baris)
kn.close()
