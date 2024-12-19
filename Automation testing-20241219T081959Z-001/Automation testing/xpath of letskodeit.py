from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()


driver.get("https://www.letskodeit.com/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "email")
edit_box.send_keys("208r1a05i2cse@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("Lasmaiah@5014")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element(By.ID, "email").send_keys("208r1a05i2cse@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Lasmaiah@5014")
driver.find_element("By.XPATH, value://*[@id="login"]).click()
time.sleep(5)