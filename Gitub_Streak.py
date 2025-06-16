from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent
import requests
import os
#############################################################
Email=os.environ.get('EMAIL')
Pass=os.environ.get('PASS')
#############################################################

ua = UserAgent()
user_agent = ua.random
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(f"user-agent={user_agent}")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://github.com/")
signin=driver.find_element("xpath", '//*[@class="HeaderMenu-link HeaderMenu-link--sign-in HeaderMenu-button flex-shrink-0 no-underline d-none d-lg-inline-flex border border-lg-0 rounded rounded-lg-0 px-2 py-1"]') 
signin.click()

user=driver.find_element("xpath", '//*[@id="login_field"]')
user.send_keys(Email)
password=driver.find_element("xpath", '//*[@id="password"]')
password.send_keys(Pass)
time.sleep(1)
signin1=driver.find_element("xpath", '//*[@class="btn btn-primary btn-block js-sign-in-button"]') 
signin1.click()



driver.get("https://camo.githubusercontent.com/f709f1852ab978e56d4c6fa3a598216d3cb0b3923519ac0e8762712ff67335f1/68747470733a2f2f6769746875622d726561646d652d73747265616b2d73746174732e6865726f6b756170702e636f6d2f3f757365723d4d6f68616d65644d6f687930267468656d653d746f6b796f6e69676874")
time.sleep(2)

from selenium.webdriver.common.by import By

texts = driver.find_elements(By.TAG_NAME, 'text')

for i,t in enumerate(texts):
    if i==5: 
        print("The Current Login Streak Is:", t.text)

time.sleep(5)
driver.quit()