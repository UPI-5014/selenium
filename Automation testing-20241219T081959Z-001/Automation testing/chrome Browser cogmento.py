from selenium import webdriver
from selenium.webdriver.common.by import By
import time
baseUrl ="https://ui.cogmento.com/?lang=en"
driver=webdriver.chrome()
driver.maximize_window()
driver.get(baseUrl)
title=driver.title
print("Title of the page is:"+ title)
currentUrl=driver.current_url
print("Current Url of the page is:" + currentUrl)
driver.refresh()
print("Browser refresh 1st time")
driver.get(driver.current_url)
print("Browser refreshed 2nd time")
driver.get("https://www.prokabaddi.com/")
currentUrl=driver.current_url
print("Current url of the web page is:" + currentUrl)
driver.back()
print("Go on step back in browser history")
currentUrl=driver.current_url
pageSource = driver.page_source
print(pageSource.encode("utf-8"))
driver.quit()
