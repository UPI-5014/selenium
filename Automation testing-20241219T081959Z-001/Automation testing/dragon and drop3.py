from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
#Open the website.
baseUrl ="https://testautomationpractice.blogspot.com/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,1500);")
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,-1000);")
driver.implicitly_wait(6)
fromElement =driver.find_element(By.ID,"draggable")
toElement =driver.find_element(By.ID,"droppable")
driver.implicitly_wait(5)
try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement,toElement).perform()
    time.sleep(8)
    actions.drag_and_drop(toElement,fromElement).perform()
    print("Drag And Drop Element Successful")
except:
    print("Drag And Drop failed an Element")