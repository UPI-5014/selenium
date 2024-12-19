from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.freecrm.com/en")
#driver .maximize_window()
time.sleep(15)
actual_title = driver.title
expect_title = "Cogmento Free CRM with AI Customer Relationship Management"
if actual_title==expect_title:
    print("Title is verified......well done python")
else:
    print("Title is not verified.....very bad my boy")