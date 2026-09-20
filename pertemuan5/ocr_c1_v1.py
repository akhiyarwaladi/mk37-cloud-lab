import sys
import requests

# ====== KONFIGURASI ======
BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = ""
MODEL = "inclusionai/ling-3.0-flash-vl:free"
# ========================

if not API_KEY:
    sys.exit("Isi API_KEY pada blok KONFIGURASI dulu.")

respon = requests.post(
    f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"model": MODEL,
          "messages": [{"role": "user",
                        "content": "Balas satu kata: siap"}],
          "max_tokens": 2500,
          "reasoning": {"enabled": False}},
    timeout=60)
respon.raise_for_status()
balasan = respon.json()["choices"][0]["message"]["content"]
print("model menjawab:", balasan.strip())
