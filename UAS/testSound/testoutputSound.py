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

    # Tunggu button "Sound" dapat diklik
    sound_button = wait.until(EC.element_to_be_clickable((By.NAME, "openSounds")))

    # Klik button "Sound"
    sound_button.click()

    # Tunggu pop-up muncul
    popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ps-popup")))

    # Atur volume efek menjadi 30 dengan JavaScript
    effect_volume_input = popup.find_element(By.NAME, "effectvolume")
    driver.execute_script("arguments[0].value = arguments[1]", effect_volume_input, 30)

    # Atur volume musik menjadi 80 dengan JavaScript
    music_volume_input = popup.find_element(By.NAME, "musicvolume")
    driver.execute_script("arguments[0].value = arguments[1]", music_volume_input, 80)

    # Centang kotak "Mute sounds" jika belum dicentang
    mute_checkbox = popup.find_element(By.NAME, "muted")
    if not mute_checkbox.is_selected():
        mute_checkbox.click()

finally:
    driver.quit()
