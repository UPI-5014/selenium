from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.hollandandbarrett.com/")

time.sleep(5)
#vitamins and supplements
edit_box=(driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[4]/a").click())
time.sleep(5)

edit_box=(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[3]/a/button").click())
time.sleep(5)

edit_box=(driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/div[1]/a[4]/div[2]").click())
time.sleep(5)

edit_box = (driver.find_element(By.XPATH, "/html/body/div[2]/div[10]/div/div/div/div[3]/a[1]/div/div[3]/div[2]/button").click())
time.sleep(5)
#vegan
driver.get("https://www.hollandandbarrett.com/")
time.sleep(5)

edit_box=(driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/a").click())
time.sleep(5)

edit_box=(driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[7]/a/button").click())
time.sleep(5)

edit_box=(driver.find_element(By.XPATH,"/html/body/div[2]/div[10]/div/div/div/div[3]/a[1]/div/div[3]/div[2]/button").click())
time.sleep(5)
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,-1000);")
driver.save_screenshot(".//Both the products are added to the basket.png")