import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle

class CookiesSaved:

    def __init__(self, cookies, debugging = True):
        self.cookies = cookies
        self.script_dir = Path(__file__).resolve().parent
        self.debugging = debugging
    
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
    
    def getCookies(self, driver):
        self.cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in self.cookies:
            cookie['domian'] = ".google.com"
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                pass
        time.sleep(5)
        return self.cookies

# driver_path = script_dir.joinpath("chromedriver.exe")
# service = Service(driver_path)




