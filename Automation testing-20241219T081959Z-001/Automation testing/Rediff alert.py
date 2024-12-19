from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
time.sleep(6)
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()
time.sleep(4)
driver.switch_to.alert.accept()
result =driver.find_element(By.ID,'result').text
print("value of attribute is:"+ result)
assert "you clicked: ok",result