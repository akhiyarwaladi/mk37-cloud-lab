#!/usr/bin/env bash
# ============================================================
# MK37 Pertemuan 5 - Arsip Scan C1 ke Amazon S3
# Ganti nama bucket dengan bucket milik Anda.
# Kode identik dengan modul PDF; kredensial diganti placeholder.
# ============================================================

# ---- Langkah 2: arsipkan scan ke S3 dan verifikasi ----
aws s3 cp scan_c1/ s3://mk37-namaanda-angkaunik/c1/ --recursive
aws s3 ls s3://mk37-namaanda-angkaunik/c1/

