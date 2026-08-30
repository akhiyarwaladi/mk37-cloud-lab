import requests

# ====== KONFIGURASI ======
API_KEY = "ISI_API_KEY_ANDA"   # isi dengan API key Anda (Langkah 6 modul)
KOTA    = "Jambi,ID"                            # ganti sesuai kebutuhan
# =========================
URL = "https://api.openweathermap.org/data/2.5/weather"

def ambil_cuaca(kota=KOTA):
    """Mengambil data cuaca terkini dari OpenWeatherMap API."""
    params = {
        "q":     kota,        # format: NamaKota,KodeNegara
        "appid": API_KEY,     # kredensial API
        "units": "metric",    # suhu dalam derajat Celsius
        "lang":  "id",        # deskripsi dalam Bahasa Indonesia
    }
    respon = requests.get(URL, params=params, timeout=10)
    respon.raise_for_status()  # galat jika status bukan 2xx
    return respon.json()

if __name__ == "__main__":
    data = ambil_cuaca()
    print(f"Kota       : {data['name']}, {data['sys']['country']}")
    print(f"Kondisi    : {data['weather'][0]['description']}")
    print(f"Suhu       : {data['main']['temp']} C")
    print(f"Terasa     : {data['main']['feels_like']} C")
    print(f"Kelembaban : {data['main']['humidity']} %")
    print(f"Angin      : {data['wind']['speed']} m/s")
