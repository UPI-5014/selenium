import time
from selenium import webdriver
import unittest
from POM Login_page.py

class LoginTest(unittest.TestCase):
    def test_validLogin(self):
        baseURL=("https://auth.hollandandbarrett.com/u/login")
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        time.sleep(5)

        lp = Loginpage(driver)
        lp.login(email:"208r1a05i2cse@gmail.com"password:"Lasmaiah@5014")
        actual_title=driver.title
        expect_title="sign in - to your account, for the best experience"
        if actual_title == expect_title:
            print("Login is Successful.......well done python")
        else:
            print("Login unsuccessfull......very good my boy!")