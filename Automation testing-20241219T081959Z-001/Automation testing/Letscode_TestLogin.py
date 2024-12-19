import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LetLoginPage():

    def __init__(self,driver):
        self.driver=driver

#locators

    _email_field="email"
    _password_field="password"
    _login_button="//button[@id='login']"
