import base64
import json
import sys
from pathlib import Path
import requests

# ====== KONFIGURASI ======
BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = ""
MODEL = "inclusionai/ling-3.0-flash-vl:free"
# ========================

PROMPT = """Baca satu halaman formulir Pilpres 2024.
Jawab HANYA JSON dengan semua kolom berikut:
nama_formulir, tps, suara_01, suara_02, suara_03,
jumlah_sah, jumlah_tidak_sah, catatan.
tps hanya nomor TPS, bukan kecamatan/desa.
Suara 01 = Anies-Muhaimin, 02 = Prabowo-Gibran,
03 = Ganjar-Mahfud. Cocokkan angka dengan terbilang.
X pengisi kosong; NIHIL berarti 0.
Kolom tidak terlihat/tidak terbaca pada foto: null.
jumlah_sah hanya disalin jika tercetak pada foto.
Jangan mengisi jumlah_sah dari penjumlahan sendiri.
Nilai suara harus integer atau null, bukan string.
Jangan menebak. Catat keterbatasan pada catatan."""

def kirim_ocr(path_gambar):
    """Kirim gambar C1 dan kembalikan dictionary."""
    if not API_KEY:
        sys.exit("Isi API_KEY pada blok KONFIGURASI dulu, "
                 "atau jalankan dengan --simulasi.")
    path = Path(path_gambar)
    if not path.exists():
        sys.exit(f"Berkas {path_gambar} tidak ada; "
                 "jalankan unduh_sirekap_v2.py dulu.")
    data = base64.b64encode(path.read_bytes()).decode()
    isi = {
        "model": MODEL,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT},
            {"type": "image_url", "image_url":
                {"url": f"data:image/jpeg;base64,{data}"}},
        ]}],
        "max_tokens": 2500,
        "reasoning": {"enabled": False},
    }
    respon = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json=isi, timeout=120)
    respon.raise_for_status()
    jawaban = respon.json()["choices"][0]
    teks = jawaban["message"].get("content")
    if jawaban.get("finish_reason") == "length" or not teks:
        raise ValueError("Jawaban terpotong/kosong; "
                         "cek max_tokens atau ganti model.")
    teks = teks.strip().removeprefix("```json")
    teks = teks.removeprefix("```").removesuffix("```").strip()
    hasil = json.loads(teks)
    kolom = ("nama_formulir", "tps", "suara_01", "suara_02",
             "suara_03", "jumlah_sah", "jumlah_tidak_sah",
             "catatan")
    if not isinstance(hasil, dict) or any(
            k not in hasil for k in kolom):
        raise ValueError("JSON harus berisi delapan kolom.")
    for k in ("suara_01", "suara_02", "suara_03",
              "jumlah_sah", "jumlah_tidak_sah"):
        n = hasil[k]
        if isinstance(n, str) and n.strip().isdecimal():
            n = int(n)
            hasil[k] = n
        if n is not None and (type(n) is not int or n < 0):
            raise ValueError(f"{k} harus integer >= 0/null.")
    return hasil

def simulasi():
    """Jawaban tiruan tanpa jaringan, untuk menguji pipeline."""
    return {"nama_formulir": "C.HASIL-PPWP (simulasi)",
            "tps": "001", "suara_01": 121,
            "suara_02": 15, "suara_03": 0,
            "jumlah_sah": None, "jumlah_tidak_sah": None,
            "catatan": "hasil tiruan untuk uji pipeline"}

if __name__ == "__main__":
    gambar = "scan_c1/sirekap-1105072002001-2.jpg"
    if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        gambar = sys.argv[1]
    if "--simulasi" in sys.argv:
        hasil = simulasi()
    else:
        hasil = kirim_ocr(gambar)
    print(json.dumps(hasil, ensure_ascii=False, indent=2))
