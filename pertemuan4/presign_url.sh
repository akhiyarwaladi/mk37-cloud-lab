# Tautan valid 10 menit (600 detik) untuk satu sampul galeri
KEY=$(aws s3 ls s3://mk37-namaanda-angkaunik/galeri-buku/ | head -n 1 | awk '{print $4}')
aws s3 presign s3://mk37-namaanda-angkaunik/galeri-buku/$KEY --expires-in 600
