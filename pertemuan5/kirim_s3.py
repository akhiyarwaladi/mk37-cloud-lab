import boto3
from pathlib import Path

# ====== KONFIGURASI (kunci kelas, Pertemuan 4) ======
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = (""
                         "")
S3_REGION = "ap-southeast-1"
NAMA_BUCKET = ""
KODE_TPS = "1105072002001"  # TPS foto Sirekap Anda
# ==================================================

s3 = boto3.client("s3", region_name=S3_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
FOLDER = Path("scan_c1")
FOLDER.mkdir(exist_ok=True)

# Foto Sirekap dari Langkah 1: arsipkan ke prefix kode TPS.
foto_tps = sorted(FOLDER.glob(f"sirekap-{KODE_TPS}-*.jpg"))
if not foto_tps:
    raise SystemExit("Jalankan unduh_sirekap.py dulu.")
for foto in foto_tps:
    kunci = f"c1/sirekap/{KODE_TPS}/{foto.name}"
    s3.upload_file(str(foto), NAMA_BUCKET, kunci)
    print("langsung terunggah:", kunci)

sejajar = s3.list_objects_v2(
    Bucket=NAMA_BUCKET, Prefix=f"c1/sirekap/{KODE_TPS}/")
print("verifikasi:", sejajar["KeyCount"], "objek TPS")
for objek in sejajar.get("Contents", []):
    print(" ", objek["Key"], f"({objek['Size']} B)")
