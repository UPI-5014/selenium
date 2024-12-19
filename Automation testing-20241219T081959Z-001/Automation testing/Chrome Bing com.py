from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.bing.com/")
#driver .maximize_window()
time.sleep(10)
actual_title = driver.title
expect_title ="Bing"
if actual_title==expect_title:
    print("Title is verified  successful......well done python")
else:
    print("Title is not verified Successful.....very god my boy")