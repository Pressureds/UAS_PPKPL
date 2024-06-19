from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi webdriver
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
    print("Tombol 'Choose name' ditemukan.")

    # Klik tombol "Choose name" untuk membuka form popup
    choose_name_button.click()

    # Tunggu form popup muncul
    popup_form = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-popup form"))
    )
    print("Form popup terlihat.")

    # Input nama pengguna yang diinginkan
    username_input = popup_form.find_element(By.NAME, "username")
    username_input.send_keys("SSStressed MindS")

    # Submit form
    submit_button = popup_form.find_element(By.CSS_SELECTOR, ".buttonbar button[type='submit']")
    submit_button.click()

    # Tunggu form popup hilang
    WebDriverWait(driver, 50).until(
        EC.invisibility_of_element(popup_form)
    )
    print("Form popup disubmit dan ditutup.")
    time.sleep(2)

    # Temukan elemen userbar yang berisi nama pengguna
    userbar = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".userbar"))
    )

    # Temukan elemen nama pengguna di dalam userbar
    username_element = userbar.find_element(By.CSS_SELECTOR, ".username .usernametext")

    # Scroll ke elemen nama pengguna
    driver.execute_script("arguments[0].scrollIntoView(true);", username_element)
    time.sleep(1)  # Beri waktu agar proses scroll selesai

    # Klik elemen nama pengguna menggunakan JavaScript
    driver.execute_script("arguments[0].click();", username_element)
    print("Elemen nama pengguna diklik.")

    # Tunggu popup detail pengguna terlihat
    user_details_popup = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-popup"))
    )
    print("Popup detail pengguna terlihat.")

    # Dapatkan tombol "Change name" dan klik
    change_name_button = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.NAME, "login"))
    )
    change_name_button.click()
    print("Tombol 'Change name' diklik.")

    # Tunggu form popup ubah nama terlihat
    change_name_popup = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-popup form"))
    )
    print("Form popup ubah nama terlihat.")

    # Input nama pengguna baru
    new_username_input = change_name_popup.find_element(By.NAME, "username")
    new_username_input.send_keys("NNNHereTestAuto")

    # Submit form ubah nama
    submit_button = change_name_popup.find_element(By.CSS_SELECTOR, ".buttonbar button[type='submit']")
    submit_button.click()

    # Tunggu popup menghilang
    WebDriverWait(driver, 50).until(
        EC.invisibility_of_element(change_name_popup)
    )
    print("Form ubah nama disubmit dan ditutup.")

    # Tunggu nama pengguna baru terlihat dan dapat diklik
    new_username_element = WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "NNNHereTestAuto"))
    )
    new_username_element.click()
    print("Nama pengguna baru terlihat dan dapat diklik.")

    # Tunggu popup detail pengguna terlihat
    user_details_popup = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-popup"))
    )
    print("Popup detail pengguna terlihat.")

    # Klik tombol "Log out"
    logout_button = user_details_popup.find_element(By.NAME, "logout")
    logout_button.click()
    print("Tombol 'Log out' diklik.")

    WebDriverWait(driver, 50).until(
        EC.element_to_be_clickable((By.NAME, "login"))
    )
    print("Berhasil logout.")

finally:
    driver.quit()
