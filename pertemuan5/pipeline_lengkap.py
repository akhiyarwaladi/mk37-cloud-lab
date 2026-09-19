import sys
import time
from pathlib import Path
import boto3
import requests
from ocr_c1 import kirim_ocr, simulasi
from simpan_rds import siapkan_tabel, simpan, RDS_HOST, RDS_PASSWORD

# ====== KONFIGURASI (kunci kelas, Pertemuan 4) ======
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = (""
                         "")
S3_REGION = "ap-southeast-1"
NAMA_BUCKET = ""
PROV = "11"            # Aceh
KAB = "1105"           # Aceh Barat
KEC = "110507"         # Arongan Lambalek
KEL = "1105072002"     # Alue Bagok
TPS = "1105072002001"  # TPS 001
# =======================================================

BASIS = ("https://uji-sirekap-obj-data.kpu.go.id"
         "/json-public-prod")
FOLDER = Path(__file__).resolve().parent / "scan_c1"
FOLDER.mkdir(parents=True, exist_ok=True)
S3 = boto3.client("s3", region_name=S3_REGION,
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

KEPALA = {"User-Agent": "mk37-kelas/1.0"}

def ambil_json(url):
    respon = requests.get(url, timeout=30, headers=KEPALA)
    respon.raise_for_status()
    return respon.json()

if not RDS_HOST or not RDS_PASSWORD:
    sys.exit("Isi RDS_HOST dan RDS_PASSWORD "
             "pada simpan_rds.py dulu.")
siapkan_tabel()                      # CREATE TABLE dulu

data = ambil_json(f"{BASIS}/pemilu/hhcw/ppwp/{PROV}/{KAB}"
                  f"/{KEC}/{KEL}/{TPS}.json")
print("suara resmi (chart):", data.get("chart"))

tuntas = 0
for urutan, url_foto in enumerate(data.get("images", []), 1):
    nama = f"sirekap-{TPS}-{urutan}.jpg"
    tujuan = FOLDER / nama
    try:
        if not tujuan.exists():      # 1) unduh bila belum ada
            unduhan = requests.get(url_foto, timeout=60, headers=KEPALA)
            tujuan.write_bytes(unduhan.content)
            print("terunduh:", nama)
            time.sleep(1)            # sopan pada sumber KPU
        kunci_s3 = f"c1/sirekap/{TPS}/{nama}"
        S3.upload_file(str(tujuan), NAMA_BUCKET, kunci_s3)
        print("terarsip:", kunci_s3) # 2) langsung arsip S3
        if "--simulasi" in sys.argv: # 3) ekstraksi AI
            hasil, model = simulasi(), "simulasi"
        else:
            hasil, model = kirim_ocr(tujuan), "ocr-ai"
        simpan(nama, hasil, model)   # 4) simpan RDS
        tuntas += 1
    except Exception as galat:
        print("  gagal, lanjut berikutnya:", galat)
print(f"Pipeline utuh selesai: {tuntas} formulir tuntas.")
