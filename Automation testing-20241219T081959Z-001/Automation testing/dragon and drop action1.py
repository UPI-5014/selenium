from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium .webdriver.common.by import By
#Open the website.driver.common.by import By
import time
baseUrl ="https://admin:admin@the-internet.herokuapp.com/drag_and_drop"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.save_screenshot(".//baseUrl screenshot.png")
time.sleep(3)
fromElement =driver.find_element(By.ID,"column-a")
toElement =driver.find_element(By.ID,"column-b")
time.sleep(5)
try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement,toElement).perform()
    time.sleep(8)
    actions.drag_and_drop(toElement,fromElement).perform()
    print("Drag And Drop Element Successful")
except:
    print("Drag And Drop failed an Element")