# What this program doing is to help the teacher on an online tutoring platform
#   called "AmazingTalker" to get contact with the automatically matched students

# Amazing talker suggests teacher remain the webpage open so they can be notified 
#   of the student matching and send them introduction message.

# This bot would automate this behavior, sending students message each time they are 
#   matched with the teacher.
import os
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

debugging = True
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

script_dir = Path(__file__).resolve().parent
driver_path = script_dir.joinpath("chromedriver.exe")

service = Service(driver_path)
chrome_options = Options()

if debugging:
    chrome_options.add_experimental_option("detach",True)
else:
    chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service = service, options=chrome_options)

driver.get("https://tw.amazingtalker.com/dashboard/teacher")

try: 
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
                pop_up = wait.until(
                    EC.visibility_of_element_located(By.CSS_SELECTOR, )
                )
        except Exception as e:
            print("Notification not found. Checking again...")
        time.sleep(5)

except Exception as e:
    print("An error occurred:", e)

finally:
    if not debugging:
        driver.quit()    



# try: 
#     email_input = driver.find_element(By.ID, 'input-735')
#     pw_input = driver.find_element(By.ID,'input-739')
#     if email_input and pw_input:
#         email_input.send_keys(EMAIL)
#         pw_input.send_keys(PASSWORD)

#         time.sleep(2)

#     if not debugging:
#         driver.quit()
# except Exception as e: 
#     print("An error occured: ", e)
#     driver.quit()
