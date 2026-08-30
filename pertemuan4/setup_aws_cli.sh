#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 4 - Langkah 3: Siapkan AWS CLI di Instans EC2
# Jalankan berurutan dari sesi SSH instans Pertemuan 3.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 3.1: SSH ke instans (cek IP terbaru di Console) ----
ssh -i ~/Downloads/mk37-keypair-namaanda.pem ubuntu@18.139.xx.xx

# ---- Langkah 3.2: Cara resmi AWS - unduh, ekstrak, pasang CLI v2 ----
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
sudo apt install -y unzip
unzip awscliv2.zip
sudo ./aws/install
aws --version

# ---- Langkah 3.3: alternatif - pasang lewat snap ----
sudo snap install aws-cli --classic
aws --version

# ---- Langkah 3.4: konfigurasikan kredensial ----
aws configure

