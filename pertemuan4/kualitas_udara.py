import requests

# ====== KONFIGURASI ======
URL_UDARA = "https://air-quality-api.open-meteo.com/v1/air-quality"
LAT, LON  = -1.61, 103.61   # Kota Jambi
# =========================

def ambil_udara(lat=LAT, lon=LON):
    """Mengambil PM2.5, PM10, dan CO terkini dari Open-Meteo."""
    params = {
        "latitude":  lat,
        "longitude": lon,
        "current":   "pm2_5,pm10,carbon_monoxide",
        "timezone":  "Asia/Jakarta",
    }
    respon = requests.get(URL_UDARA, params=params, timeout=10)
    respon.raise_for_status()
    return respon.json()["current"]

def kategori_ispu(pm25):
    """Perkiraan kategori ISPU dari PM2.5 jam-an (PermenLHK 14/2020);
ISPU resmi memakai rata-rata 24 jam."""
    if pm25 <= 15.5:
        return "Baik"
    elif pm25 <= 55.4:
        return "Sedang"
    elif pm25 <= 150.4:
        return "Tidak Sehat"
    elif pm25 <= 250.4:
        return "Sangat Tidak Sehat"
    return "Berbahaya"

if __name__ == "__main__":
    udara = ambil_udara()
    pm25  = udara["pm2_5"]
    print(f"PM2.5 : {pm25} ug/m3")
    print(f"PM10  : {udara['pm10']} ug/m3")
    print(f"CO    : {udara['carbon_monoxide']} ug/m3")
    print(f"Kategori ISPU : {kategori_ispu(pm25)}")
