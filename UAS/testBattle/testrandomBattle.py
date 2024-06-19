from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi driver Chrome
driver = webdriver.Chrome()

try:
    # Buka website
    driver.get("https://play.pokemonshowdown.com/")
    wait = WebDriverWait(driver, 20)

    # Klik button "Battle!" pertama
    battle_button_first = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="room-"]/div/div[1]/div[2]/div[1]/form/p[5]/button')))
    battle_button_first.click()
    print("Mengklik tombol Battle pertama.")
    time.sleep(5)

    # Verifikasi apakah pop-up muncul
    try:
        username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/form/p[1]/label/input")))
        username_input.send_keys("WorkPleaseHope")
        print("Memasukkan username.")
    except TimeoutException:
        print("Pop-up untuk memasukkan username tidak muncul.")
        raise

    # Klik button "Choose name"
    choose_name_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/form/p[2]/button[1]")
    choose_name_button.click()
    print("Mengklik tombol Choose name.")
    time.sleep(5)

    # Klik button "Battle!" kedua kali
    battle_button_second = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="room-"]/div/div[1]/div[2]/div[1]/form/p[5]/button')))
    battle_button_second.click()
    print("Mengklik button Battle kedua.")

    # Tunggu diarahkan ke halaman battle
    try:
        choose_move_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="room-battle-gen9randombattle-2146198739"]/div[5]/div/div[2]/div[2]/button[1]')))
        print("Button Choose move ditemukan.")
        choose_move_button.click()
        print("Mengklik tombol Choose move.")
    except TimeoutException:
        print("Gagal menjalankan aksi.")
        raise
    time.sleep(5)

    # Klik button dengan ikon x untuk keluar battle
    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div[2]/div/ul[2]/li/button')))
    close_button.click()
    print("Mengklik button close.")
    time.sleep(2)

    # Klik button "Forfeit"
    forfeit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/form/p[3]/button[1]")))
    forfeit_button.click()
    print("Mengklik button forfeit.")

except TimeoutException as e:
    print(f"Error: {e}")

finally:
    driver.quit()
