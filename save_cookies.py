import os
from pathlib import Path
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



class Cookies:

    def __init__(self, email, password, debugging=True):   
        # load_dotenv()
        # self.email = os.getenv('EMAIL')
        # self.password = os.getenv('PASSWORD')
        self.email = email
        self.password = password
        self.debugging = debugging
        self.script_dir = Path(__file__).resolve().parent

    def setChromeOption(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-software-rasterizer')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-setuid-sandbox')
        chrome_options.add_argument('--remote-debugging-port=9222')
        return chrome_options


    def initializeDriver(self):
        chrome_options = self.setChromeOption()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://tw.amazingtalker.com/login")
        return driver

    def SaveCookies(self, driver):
        try: 
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
                email_input.send_keys(self.email)
                password_input.send_keys(self.password)
                loginBtn = driver.find_element(By.CSS_SELECTOR, "[data-testid='login-button']")
                loginBtn.click()

                time.sleep(2)
                print("After Login")

            if not self.debugging:
                driver.quit()
        except Exception as e: 
            print("An error occured: ", e)
            driver.quit()

        cookies = driver.get_cookies()
        pickle.dump(cookies, open("cookies.pkl", "wb"))
# driver_path = script_dir.joinpath("chromedriver.exe")
# service = Service(driver_path)
