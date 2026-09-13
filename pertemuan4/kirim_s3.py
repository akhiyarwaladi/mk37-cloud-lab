import json

import boto3
from pathlib import Path

# ====== KONFIGURASI ======
BUCKET = "mk37-namaanda-angkaunik"  # ganti dengan nama bucket Anda
# =========================

s3 = boto3.client("s3", region_name="ap-southeast-1")
sampul = sorted(Path("sampul").glob("*.jpg"))[0]
s3.upload_file(str(sampul), BUCKET, f"coba-boto3/{sampul.name}")
s3.put_object(Bucket=BUCKET, Key="coba-boto3/ringkasan.json",
              Body=json.dumps({"sampul": sampul.name}, ensure_ascii=False),
              ContentType="application/json")
print("Terkirim:", sampul.name)
