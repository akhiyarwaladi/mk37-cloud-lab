# 1. Uji identitas dan koneksi
aws sts get-caller-identity

# 2. Daftar bucket
aws s3 ls

# 3. Unggah berkas dari instans ke bucket
echo "Laporan cuaca dari EC2 - $(date)" > laporan.txt
aws s3 cp laporan.txt s3://mk37-namaanda-angkaunik/laporan/ec2-laporan.txt

# 4. Lihat isi bucket (dan prefix)
aws s3 ls s3://mk37-namaanda-angkaunik/
aws s3 ls s3://mk37-namaanda-angkaunik/laporan/

# 5. Unduh kembali ke instans
aws s3 cp s3://mk37-namaanda-angkaunik/laporan/ec2-laporan.txt ./cek-balik.txt

# 6. Sinkronisasi folder (mirip rsync)
aws s3 sync ./data/ s3://mk37-namaanda-angkaunik/data/

# 7. Hapus objek
aws s3 rm s3://mk37-namaanda-angkaunik/laporan/ec2-laporan.txt
