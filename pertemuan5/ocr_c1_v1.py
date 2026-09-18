import os
import sys
import requests

# ====== KONFIGURASI (environment variable) ======
BASE_URL = os.environ.get("OPENCODE_BASE_URL", "")
API_KEY = os.environ.get("OPENCODE_API_KEY", "")
MODEL = os.environ.get("OPENCODE_MODEL", "xiaomi-mimo-2.5")
# ================================================

if not BASE_URL or not API_KEY:
    sys.exit("Atur OPENCODE_BASE_URL dan OPENCODE_API_KEY dulu.")

respon = requests.post(
    f"{BASE_URL}/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={"model": MODEL,
          "messages": [{"role": "user",
                        "content": "Balas dengan satu kata: siap"}]},
    timeout=60)
respon.raise_for_status()
balasan = respon.json()["choices"][0]["message"]["content"]
print("model menjawab:", balasan.strip())
