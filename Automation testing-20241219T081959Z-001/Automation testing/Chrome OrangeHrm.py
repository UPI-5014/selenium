from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver .maximize_window()
time.sleep(8)
actual_title = driver.title
expect_title = "OrangeHRM"
if actual_title==expect_title:
    print("Title is verified successful......well done python")
else:
    print("Title is not verified  sucessfully.....very god my boy")

