from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://auth.hollandandbarrett.com/u/login")
time.sleep(2)

driver.find_element(By.ID,"username" ).send_keys("208r1a05i2cse@gmail.com")
driver.save_screenshot(".//username screenshot.png")
driver.find_element(By.NAME, "password").send_keys("Lasmaiah@5014")
driver.save_screenshot(".//password screenshot.png")
driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/form/div[2]/button" ).click()
driver.save_screenshot(".//clicked on signin screenshot.png")
time.sleep(2)
