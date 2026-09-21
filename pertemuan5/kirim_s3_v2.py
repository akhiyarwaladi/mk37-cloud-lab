import boto3
import sys
from pathlib import Path

# ====== KONFIGURASI (kunci kelas, Pertemuan 4) ======
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = (""
                         "")
S3_REGION = "ap-southeast-1"
NAMA_BUCKET = ""
# ==================================================

s3 = boto3.client("s3", region_name=S3_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
NAMA = "sirekap-1105072002001-2.jpg"
GAMBAR = Path("scan_c1") / NAMA
if not GAMBAR.exists():
    sys.exit("Berkas tidak ada; jalankan unduh_sirekap.py dulu.")

KUNCI = f"c1/sirekap/1105072002001/{NAMA}"
s3.upload_file(str(GAMBAR), NAMA_BUCKET, KUNCI)
ukuran = s3.head_object(Bucket=NAMA_BUCKET, Key=KUNCI)["ContentLength"]
print("terunggah:", KUNCI, f"({ukuran // 1024} KB)")
