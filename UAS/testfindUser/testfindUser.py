from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi driver Chrome
driver = webdriver.Chrome()

try:
    # Buka website
    driver.get("https://play.pokemonshowdown.com/")
    wait = WebDriverWait(driver, 10)

    # Tunggu halaman selesai dimuat
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Klik tombol "Find a user"
    find_user_button = wait.until(EC.element_to_be_clickable((By.NAME, "finduser")))
    find_user_button.click()

    # Tunggu pop-up muncul
    popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ps-popup")))

    # Isi username yang ingin dicari
    username_input = popup.find_element(By.NAME, "data")
    username_input.send_keys("pro")

    # Klik tombol submit "Open"
    submit_button = popup.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Tunggu popup user detail muncul
    user_details_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.userdetails")))

    # Klik nama user untuk melihat detail user
    user_link = user_details_popup.find_element(By.TAG_NAME, "a")
    user_link.click()

finally:
    driver.quit()
