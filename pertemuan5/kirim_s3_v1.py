import boto3

# ====== KONFIGURASI (kunci IAM Anda, Pertemuan 4) ======
AWS_ACCESS_KEY_ID = "AKIAXXXXXXXXXXXXXXXX"  # Access key ID
AWS_SECRET_ACCESS_KEY = "ISI_SECRET_KEY_ANDA"  # Secret access key
S3_REGION = "ap-southeast-1"
NAMA_BUCKET = "mk37-namaanda-angkaunik"  # nama bucket Anda
# ==================================================

s3 = boto3.client("s3", region_name=S3_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
s3.head_bucket(Bucket=NAMA_BUCKET)
print("kredensial benar; bucket", NAMA_BUCKET, "terjangkau")
