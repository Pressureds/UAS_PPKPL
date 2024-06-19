from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inisialisasi driver Chrome
driver = webdriver.Chrome()

try:
    # Buka website
    driver.get("https://play.pokemonshowdown.com/")

    # Tunggu halaman selesai dimuat
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Tunggu tombol "Choose name" dapat diklik
    choose_name_button = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.NAME, "login"))
    )

    # Klik tombol "Choose name" untuk membuka form popup
    choose_name_button.click()

    # Tunggu form popup terlihat
    popup_form = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-popup form"))
    )

    # Masukkan nama pengguna yang diinginkan
    username_input = popup_form.find_element(By.NAME, "username")
    username_input.send_keys("Stressed Mind")

    # Submit form
    submit_button = popup_form.find_element(By.CSS_SELECTOR, ".buttonbar button[type='submit']")
    submit_button.click()

    # Tunggu nama pengguna berhasil disubmit
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".username"), "Stressed Mind")
    )

finally:
    driver.quit()
