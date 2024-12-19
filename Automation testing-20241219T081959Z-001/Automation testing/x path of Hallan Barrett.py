from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Holland & Barrett login page
driver.get("https://auth.hollandandbarrett.com/u/login")

# Maximize the browser window
driver.maximize_window()
time.sleep(5)

edit_box = driver.find_element(By.ID, "username")
edit_box.send_keys("208r1a05i2cse@gmail.com")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)

edit_box = driver.find_element(By.NAME, "password")
edit_box.send_keys("Lasmaiah@5014")
edit_box.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("208r1a05i2cse@gmail.com")
driver.find_element(By.NAME, "password").send_keys("Lasmaiah@5014")
driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/form/div[2]/button").click()
time.sleep(5)
