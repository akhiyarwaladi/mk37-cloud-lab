# Unggah galeri dan bukti ke dua prefix, lalu verifikasi jumlahnya
aws s3 sync ./sampul/ s3://mk37-namaanda-angkaunik/galeri-buku/
aws s3 sync ./bukti/ s3://mk37-namaanda-angkaunik/galeri-bukti/
echo "Sampul lokal : $(ls sampul/*.jpg | wc -l) berkas"
echo "Sampul di S3  : $(aws s3 ls s3://mk37-namaanda-angkaunik/galeri-buku/ | wc -l) objek"
