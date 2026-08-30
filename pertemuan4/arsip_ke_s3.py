import subprocess

BUCKET = "mk37-namaanda-angkaunik"   # ganti dengan nama bucket Anda

def arsip_ke_s3(data):
    """Menyimpan ringkasan cuaca sebagai objek di bucket S3."""
    import json, datetime
    stempel = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    key = f"cuaca/{stempel}-{data['name'].lower()}.json"
    subprocess.run(
        ["aws", "s3", "cp", "-", f"s3://{BUCKET}/{key}"],
        input=json.dumps(data, ensure_ascii=False),
        text=True, check=True)
    print("Laporan diarsipkan ke s3://", BUCKET, "/", key)
