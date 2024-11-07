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

    script_dir = Path(__file__).resolve().parent
    driver_path = script_dir.joinpath("chromedriver.exe")
    # service = Service(driver_path)
    


    def __init__(self, email, password, driver_path, service, debugging = True):
        self.email = email
        self.password = password
        self.driver_path = driver_path
        self.service = service
    
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

        
        
        