import time
from fileinput import filename

from selenium import webdriver
from selenium.webdriver.common.by import By
import Xmlfile

driver=webdriver.Chrome()
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()
time.sleep(5)

path="C:\\PyTest\PyTest Learning\selenium practice\Book1.xlsx"
rows=Xmlfile.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    username=Xmlfile.readData(path,'Sheet1',r,1)
    password = Xmlfile.readData(path, "Sheet1",r,2)

    driver.find_element(By.ID,'email').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="login"]').click()
    time.sleep(5)

    driver.find_element(By.XPATH, '// *[ @ id = "dropdownMenu1"] / img').click()
    driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div[1]/div/div/ul/li[3]/a').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '// *[ @ id = "navbar-inverse-collapse"] / div / div / a').click()


    if driver.title=="Home Page":
        print("test is passed")
        Xmlfile.writeData(path,"Sheet1",r,3,"Passed")
    else:
        print("test is failed")
        Xmlfile.writeData(path, "Sheet1", r, 3, "Failed")