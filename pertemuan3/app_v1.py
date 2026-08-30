import requests

# ====== KONFIGURASI ======
API_KEY = "ISI_API_KEY_ANDA"   # isi dengan API key Anda (Langkah 6 modul)
KOTA    = "Jambi,ID"                            # ganti sesuai kebutuhan
# =========================
URL = "https://api.openweathermap.org/data/2.5/weather"

data = requests.get(URL, params={"q": KOTA, "appid": API_KEY,
                                 "units": "metric"}).json()
print("Suhu sekarang:", data["main"]["temp"], "C")
