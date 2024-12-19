from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(6)
driver.find_element(By.ID,'username').send_keys("208r1a05i2cse@gmail.com")
driver.find_element(By.NAME,'password').send_keys("Lasmaiah@5014")
time.sleep(8)
