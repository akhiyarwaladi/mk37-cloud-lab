from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ====== KONFIGURASI ======
URL_KATALOG = "http://books.toscrape.com/"
# =========================

opsi = Options()
opsi.add_argument("--headless")
opsi.add_argument("--no-sandbox")
opsi.add_argument("--disable-dev-shm-usage")
opsi.add_argument("--window-size=1280,800")
d = webdriver.Chrome(options=opsi)
d.get(URL_KATALOG)
kartu = d.find_elements(By.CSS_SELECTOR, "article.product_pod")
print(f"Kartu buku di halaman 1: {len(kartu)}")
for k in kartu[:5]:
    img = k.find_element(By.CSS_SELECTOR, "div.image_container img")
    print("-", img.get_attribute("alt"))
    print(" ", img.get_attribute("src"))
d.save_screenshot("bukti_halaman1.png")
print("Bukti tersimpan: bukti_halaman1.png")
d.quit()
