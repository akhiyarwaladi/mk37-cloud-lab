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
print("Judul tab :", d.title)
print("Kartu buku:", len(d.find_elements(By.CSS_SELECTOR, "article.product_pod")))
d.quit()
