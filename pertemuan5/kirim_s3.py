import boto3
import time
from pathlib import Path
import requests

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

# Tiap entri: (nama, URL sumber, kunci S3). Unduh bila perlu,
# lalu LANGSUNG unggah; loop tidak menunggu unduhan lain.
DAFTAR = [
    ("c1-plano.jpeg",
     "https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
     "static/datasets/C1-plano-original.jpeg", "c1/kawalc1/c1-plano.jpeg"),
    ("c1-pilpres-1.jpg",
     "https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
     "static/contoh-pilpres-2019/1.JPG", "c1/kawalc1/c1-pilpres-1.jpg"),
    ("c1-pilgub-1.jpg",
     "https://raw.githubusercontent.com/kawalc1/kawalc1/master/"
     "static/contoh-pilgub/1.jpeg", "c1/kawalc1/c1-pilgub-1.jpg"),
]

for nama, url, kunci in DAFTAR:
    tujuan = FOLDER / nama
    if not tujuan.exists():
        respon = requests.get(url, timeout=30,
                              headers={"User-Agent": "mk37-kelas/1.0"})
        respon.raise_for_status()
        tujuan.write_bytes(respon.content)
        print("terunduh:", nama)
        time.sleep(1)                    # sopan pada sumber publik
    s3.upload_file(str(tujuan), NAMA_BUCKET, kunci)
    print("langsung terunggah:", kunci)

for foto in sorted(FOLDER.glob("sirekap-*.jpg")):
    kunci = f"c1/sirekap/{KODE_TPS}/{foto.name}"
    s3.upload_file(str(foto), NAMA_BUCKET, kunci)
    print("langsung terunggah:", kunci)

sejajar = s3.list_objects_v2(Bucket=NAMA_BUCKET, Prefix="c1/")
print(f"verifikasi: {sejajar['KeyCount']} objek pada prefix c1/")
for objek in sejajar.get("Contents", []):
    print(" ", objek["Key"], f"({objek['Size']} B)")
