from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()


driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "log_email")
edit_box.send_keys("208r1a05i2cse@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "log_password")
edit_box.send_keys("Lasmaiah@5014")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)