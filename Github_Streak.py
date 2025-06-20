from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent
import requests
import os
#############################################################
Email=os.environ.get('EMAIL')
Pass=os.environ.get('PASS')
bot_token = os.environ.get('TOKEN')
chat_id = os.environ.get('ID')
#############################################################

ua = UserAgent()
user_agent = ua.random
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--headless=new")  # Use the new headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_page_load_timeout(60)

driver.get("https://github.com")
time.sleep(2)
method, path = (By.XPATH, "//*[contains(@class, 'HeaderMenu-link--sign-in')]")
signin =driver.find_element(method, path)
signin.click()
time.sleep(2)
user=driver.find_element("xpath", '//*[@id="login_field"]')
user.send_keys(Email)
password=driver.find_element("xpath", '//*[@id="password"]')
password.send_keys(Pass)
time.sleep(1)

signin_button = driver.find_element(By.XPATH, '//*[@class="btn btn-primary btn-block js-sign-in-button"]')
signin_button.click()

time.sleep(1)
driver.get("https://camo.githubusercontent.com/3ed56242bf3c7f0bde3be83493f9943cc4c2d62cb3cd55c6e92af80f925e91f9/68747470733a2f2f73747265616b2d73746174732e64656d6f6c61622e636f6d3f757365723d4d6f68616d65644d6f687930267468656d653d746f6b796f6e69676874")
time.sleep(2)
texts = driver.find_elements(By.TAG_NAME, 'text')

message = ("Error")

for i,t in enumerate(texts):
    if i==5:
        message = (f"The Current Login Streak Is:{t.text}")
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {
'chat_id': chat_id,
'text': message
}
response = requests.post(url, data=payload)
time.sleep(5)
driver.quit()

