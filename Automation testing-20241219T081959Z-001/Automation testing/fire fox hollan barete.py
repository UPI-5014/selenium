
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver .maximize_window()
driver.minimize_window()
time.sleep(15)
actual_title = driver.title
expect_title = "Holland and Barrett"
if actual_title==expect_title:
    print("verified is successful......well done python")
else:
    print("verified is not  sucessfully.....very god my boy")

