from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from load_cookies import CookiesSaved
import datetime
import time

class MessageSender:

    def __init__(self, Cookies, debugging=True):
        # self.email = email
        # self.password = password
        self.cookies = Cookies
        self.debugging = debugging
        self.script_dir = Path(__file__).resolve().parent
        # self.driver_path = self.script_dir.joinpath("chromedriver.exe")
        # self.service = Service(self.driver_path)
        self.debugging = debugging
        self.count = 0
        self.message = ""
    
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
        driver.get("https://tw.amazingtalker.com")
        return driver 
        
    
    def notfClick(self):
        try:
            driver = self.initializeDriver()
            while True: 
                try: 
                    wait = WebDriverWait(driver, 20)
                    notification = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, ".at-notification.at-notification-student-recommend.right")
                        )
                    )
                    notification.click()
                    time.sleep(1.5)
                    print("Notification clicked at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    pop_up = wait.until(
                        EC.visibility_of_element_located(By.ID, 'input-995')
                    )
                    send = wait.until(
                        EC.element_to_be_clickable(By.CSS_SELECTOR, 'contact-ticket')
                    )
                    send.click()
                    self.count += 1
                    
                except Exception as e:
                    self.message = "Notification not found. Checking again at:"
                    print(self.message, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
                # minutes = 5
                time.sleep(25)

        except Exception as e:
            print("An error occurred:", e)
        
    def testerClick(self):
        try:
            driver = self.initializeDriver()
            while True:
                try:
                    wait = WebDriverWait(driver, 20)
                    tester = wait.until(
                        EC.element_to_be_clickable(By.CSS_SELECTOR, ".at-notification.at-notification__current-message.right")
                    )
                    tester.click()
                    time.sleep(2)
                except Exception as e:
                    print("tester not clicked, error: ", e)
                time.sleep(25)
        except Exception as e:
            print("An error occurred: ", e)
    def tester_message_send(self):
        try:
            driver = self.initializeDriver()
            wait = WebDriverWait(driver, 20)
            tester_input = wait.until(
                EC.visibility_of_element_located(By.ID, 'input-891')
            )
            if tester_input:
                tester_input.send_keys("Hi Elen!")
                send_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button_g0a8W")))
                send_btn.click()
                print("Test Message sent successfully!!!!!!!!!!!!!")
        except Exception as e:
            print(e)

    # def showContactedStu(self):
    #     ## Student Name
