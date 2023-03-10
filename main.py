from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()
chrome_driver_path = "C:\Development\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

start_date = date(2023, 3, 1)
TODAY = date.today()
three_gap = []
total = 8
three_mon_timedelta = datetime.timedelta(days=3 * 365/12)
for i in range(total):
    date = start_date + three_mon_timedelta * i
    three_gap.append(date)

for i in three_gap:
    if i == TODAY:
        driver.get("https://login.yahoo.com/?.intl=in&.lang=en-IN&src=ym&activity=mail-direct&pspid=159600001&done=https%3A%2F%2Fin.mail.yahoo.com%2Fd&add=1")
        time.sleep(20)

        EMAIL = os.getenv("EMAIL")
        PASSWORD = os.getenv("PASSWORD")

        email = driver.find_element(By.NAME, "username")
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(10)

        password = driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)

        compose = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a')
        compose.click()
        time.sleep(10)

        to_mail = driver.find_element(By.XPATH, '//*[@id="message-to-field"]')
        to_mail.send_keys(EMAIL)
        time.sleep(2)

        subject = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div/div/div[1]/div[3]/div/div/input')
        subject.send_keys('Salary raise')
        time.sleep(2)

        body = driver.find_element(By.XPATH, '//*[@id="editor-container"]/div[1]')
        body.send_keys("Respected Sir/Mam,\n\n\t With the fast-evolving technologies, "
                       "the quality and skills of an employee improve accordingly."
                       " The need to stay updated demands long working hours which in  "
                       "turn makes me think about my current pay. So, I kindly ask you to look "
                       "into the various roles I play and I wish for a salary raise of 25%.Thank you."
                       "\n\nYours respectfully,\nSSV")
        time.sleep(10)

        send = driver.find_element(By.XPATH, '//*[@id="mail-app-component"]/div/div/div/div[2]/div[2]/div/button')
        send.click()
        time.sleep(30)

        profile = driver.find_element(By.ID, "ybarAccountMenu")
        profile.click()
        time.sleep(2)

        sign_out = driver.find_element(By.ID, 'profile-signout-link')
        sign_out.click()

driver.quit()

