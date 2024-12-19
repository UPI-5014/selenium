from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/")
#driver .maximize_window()
time.sleep(15)
actual_title = driver.title
expect_title ="Electronics, Cars, Fashion, Collectibles & More | eBay"
if actual_title==expect_title:
    print("Title is successful......well done python")
else:
    print("Title is not  sucessfully.....very god my boy")