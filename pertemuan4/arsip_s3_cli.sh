# Coba pola intinya dulu: kirim teks lewat stdin (tanda -), tanpa berkas
echo "tes arsip" | aws s3 cp - s3://mk37-namaanda-angkaunik/coba/tes.txt
aws s3 ls s3://mk37-namaanda-angkaunik/coba/
