import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
       driver = webdriver.Chrome()
       driver.get("https://www.linkedin.com")
       TitleOfBrowser = driver.title
       self.assertTrue(TitleOfBrowser == "Google")


 if __name__ == "__main__":
     unittest.main()