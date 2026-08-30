import base64
import json
import os
import sys
from pathlib import Path
import requests

# ====== KONFIGURASI (environment variable) ======
BASE_URL = os.environ.get("OPENCODE_BASE_URL", "")
API_KEY = os.environ.get("OPENCODE_API_KEY", "")
MODEL = os.environ.get("OPENCODE_MODEL", "xiaomi-mimo-2.5")
# ================================================

PROMPT = """Baca formulir C1 pada gambar ini dan ekstrak angkanya.
Jawab HANYA JSON valid tanpa penjelasan tambahan, dengan bentuk:
{"nama_formulir": "...", "tps": "...", "jumlah_sah": 0,
 "jumlah_tidak_sah": 0, "catatan": "..."}
Isi 0 bila ada angka yang tidak terbaca."""

def kirim_ocr(path_gambar):
    """Kirim satu gambar C1, kembalikan hasil ekstraksi sebagai dict."""
    if not BASE_URL or not API_KEY:
        sys.exit("Atur OPENCODE_BASE_URL dan OPENCODE_API_KEY dulu, "
                 "atau jalankan dengan --simulasi.")
    path = Path(path_gambar)
    if not path.exists():
        sys.exit(f"Berkas {path_gambar} tidak ada; jalankan unduh_c1.py dulu.")
    data = base64.b64encode(path.read_bytes()).decode()
    isi = {
        "model": MODEL,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT},
            {"type": "image_url", "image_url":
                {"url": f"data:image/jpeg;base64,{data}"}},
        ]}],
        "max_tokens": 500,
    }
    respon = requests.post(
        f"{BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json=isi, timeout=120)
    respon.raise_for_status()
    teks = respon.json()["choices"][0]["message"]["content"].strip()
    teks = teks.removeprefix("```json").removesuffix("```").strip()
    return json.loads(teks)

def simulasi():
    """Jawaban tiruan tanpa jaringan, untuk menguji pipeline."""
    return {"nama_formulir": "C1 Plano (simulasi)", "tps": "036",
            "jumlah_sah": 203, "jumlah_tidak_sah": 8,
            "catatan": "hasil tiruan untuk uji pipeline"}

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    gambar = arg if arg and not arg.startswith("--") else "scan_c1/c1-plano.jpeg"
    hasil = simulasi() if "--simulasi" in sys.argv else kirim_ocr(gambar)
    print(json.dumps(hasil, ensure_ascii=False, indent=2))
