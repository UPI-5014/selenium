from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://www.opencart.com/index.php?route=common/home")
driver.maximize_window()
time.sleep(6)
driver.find_element(By.ID,'input-emai').send_keys("ambatiupendhar1567@gmai.com")
driver.find_element(By.NAME,'input-password').send_keys("Lasmaiah@5014")
time.sleep(8)