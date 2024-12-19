from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://demo.opencart.com/index.php?")
#driver .maximize_window()
time.sleep(1)
actual_title = driver.title
expect_title = "OpenCart - Open Source Shopping Cart Solution"
if actual_title==expect_title:
    print("Title is verified successful......well done python")
else:
    print("Title is not verified sucessfully.....very good my boy")