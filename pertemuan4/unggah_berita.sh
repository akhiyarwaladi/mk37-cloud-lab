# Unggah koleksi berita (JSON + gambar) lalu verifikasi jumlahnya
aws s3 sync ./berita/ s3://mk37-namaanda-angkaunik/berita/
echo "JSON lokal : $(ls berita/*.json | wc -l) berkas"
echo "Gambar S3  : $(aws s3 ls s3://mk37-namaanda-angkaunik/berita/img/ | wc -l) objek"
