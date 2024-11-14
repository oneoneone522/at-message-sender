from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time

class MessageSender:

    def __init__(self, email, password, debugging=True):
        self.email = email
        self.password = password
        self.debugging = debugging
        self.script_dir = Path(__file__).resolve().parent
        self.driver_path = self.script_dir.joinpath("chromedriver.exe")
        self.service = Service(self.driver_path)
        self.debugging = debugging
        self.count = 0
        self.message = ""
    
    def initialize_driver(self):
        chrome_options = Options()
        if self.debugging:
            chrome_options.add_experimental_option("detach",True)
        else:
            chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=self.service, options=chrome_options)
        return driver
    
    def getCount(self):
        return self.count
    
    def getMessage(self):
        return self.message
    
    
    def notfClick(self):
        try:
            driver = self.initialize_driver()
            while True: 
                try: 
                    wait = WebDriverWait(driver, 20)
                    notification = wait.until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, ".at-notification.at-notification-student-recommend.right")
                        )
                    )
                    if notification:
                        notification.click()
                        time.sleep(1.5)
                        print("Notification clicked at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        pop_up = wait.until(
                            EC.visibility_of_element_located(By.ID, 'input-995')
                        )
                        send = wait.until(
                            EC.visibility_of_element_located(By.ID, 'contact-ticket')
                        )
                        send.click()
                        self.count += 1
                except Exception as e:
                    self.message = "Notification not found. Checking again at:"
                    print(self.message, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
                minutes = 5
                time.sleep(minutes *60)

        except Exception as e:
            print("An error occurred:", e)
        
    # def showContactedStu(self):
    #     ## Student Name
