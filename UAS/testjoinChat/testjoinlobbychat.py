from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inisialisasi webdriver
driver = webdriver.Chrome()
driver.get("https://play.pokemonshowdown.com/")

try:
    # Tunggu link "lobby" muncul dan klik
    lobby_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/lobby']"))
    )
    lobby_link.click()
    print("Successfully clicked on lobby link")
    time.sleep(5)

    # Tunggu button 'Join chat' muncul dan klik
    join_chat_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="room-lobby"]/div[3]/form/button'))
    )
    join_chat_button.click()
    print("Successfully clicked on 'Join chat' button")

    # Tunggu pop up input username muncul
    username_input = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ps-popup input[name='username']"))
    )

    # Input username
    username = "SSStressed MindSS"
    username_input.send_keys(username)

    # Klik button 'Choose name'
    choose_name_button = driver.find_element(By.CSS_SELECTOR, "div.ps-popup button[type='submit']")
    choose_name_button.click()
    print("Successfully clicked on 'Choose name' button")
    time.sleep(5)

    # Mencari textarea untuk input pesan dengan XPath
    chatbox = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="room-lobby"]/div[3]/form/textarea[2]'))
    )
    print("Found chatbox for message input")

    # Input pesan dan kirim pesan
    message = "Hello, this is an automated message!"  # Ganti dengan pesan yang diinginkan
    chatbox.send_keys(message)
    chatbox.send_keys(Keys.RETURN)
    print("Successfully sent message in chat")
    time.sleep(5)

# Pengecekan untuk error
except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
