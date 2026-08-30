import requests

# ====== KONFIGURASI ======
URL_UDARA = "https://air-quality-api.open-meteo.com/v1/air-quality"
LAT, LON  = -1.61, 103.61   # Kota Jambi
# =========================

params = {
    "latitude":  LAT,
    "longitude": LON,
    "current":   "pm2_5,pm10,carbon_monoxide",
    "timezone":  "Asia/Jakarta",
}
respon = requests.get(URL_UDARA, params=params, timeout=10)
respon.raise_for_status()
print(respon.json()["current"])
