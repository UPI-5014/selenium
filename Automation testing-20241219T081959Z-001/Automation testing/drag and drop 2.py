from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
#Open the website.
baseUrl ="https://jqueryui.com/slider/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)
driver.switch_to.frame(0)
element=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default ui-state-focus ui-state-hover']")
try:
    actions=ActionChains(driver)
    actions.drag_and_drop_by_offset(element,"400","0").perform()
    print("slidingElement successful")
except:
    print("sliding failed on element")