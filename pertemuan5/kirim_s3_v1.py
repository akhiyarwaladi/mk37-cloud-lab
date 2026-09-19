import boto3

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
s3.head_bucket(Bucket=NAMA_BUCKET)
print("kredensial benar; bucket", NAMA_BUCKET, "terjangkau")
