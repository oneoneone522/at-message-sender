import os
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

debugging = True
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

script_dir = Path(__file__).resolve().parent
# driver_path = script_dir.joinpath("chromedriver.exe")

# service = Service(driver_path)
chrome_options = Options()

chrome_options.add_argument('--headless')  # Run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://tw.amazingtalker.com/login")

try: 
    # loginBtn = driver.find_element(By.CSS_SELECTOR, "is-hidden-touch at-navbar-item_A06ro")
    # loginBtn.click()
    wait = WebDriverWait(driver,3)
    email_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID, 'input-70')
        )
    )
    password_input = wait.until(
        EC.visibility_of_element_located(
            (By.ID,'input-74')
        )
    )
    if email_input and password_input:
        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        loginBtn = driver.find_element(By.CSS_SELECTOR, "[data-testid='login-button']")
        loginBtn.click()

        time.sleep(2)
        print("After Login")

    if not debugging:
        driver.quit()
except Exception as e: 
    print("An error occured: ", e)
    driver.quit()

cookies = driver.get_cookies()
pickle.dump(cookies, open("cookies.pkl", "wb"))
