import os
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
class MessageSender:
    
    debugging = True
    load_dotenv()
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    email = ""
    password = ""
    debugging = True

    script_dir = Path(__file__).resolve().parent
    driver_path = script_dir.joinpath("chromedriver.exe")
    service = Service(driver_path)
    


    def __init__(self, email, password, driver_path, service, debugging):
        self.email = email
        self.password = password
        self.driver_path = driver_path
        self.service = service
        self.debugging = debugging
    
    def setService(self):
        self.service = Service(self.driver_path)
        return self.service
    
    def initialize_driver(self):
        chrome_options = Options()
        if self.debugging:
            chrome_options.add_experimental_option("detach",True)
        else:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=self.service, options=chrome_options)
        return driver
    
    def login(self):
        self.driver.get("https://tw.amazingtalker.com/login")
        try: 
            # loginBtn = driver.find_element(By.CSS_SELECTOR, "is-hidden-touch at-navbar-item_A06ro")
            # loginBtn.click()
            wait = WebDriverWait(self.driver,3)
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
                password_input.send_keys(self.email)
                loginBtn = self.driver.find_element(By.CSS_SELECTOR, "[data-testid='login-button']")
                loginBtn.click()

                time.sleep(2)

            if not self.debugging:
                self.driver.quit()
        except Exception as e: 
            print("An error occured: ", e)
            self.driver.quit()

        
        
        