from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def startBot(username, password, url):
    path = "C:\\Users\\hp\\Downloads\\chromedriver.exe"

    service = Service(path)
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    time.sleep(2)

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button").click()


# Driver Code
username = "testuser"
password = "testpass"
url = "https://example.com/login"

startBot(username, password, url)
