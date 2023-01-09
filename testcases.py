
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()

# options.headless = True

webpageUrl = 'http://localhost:5000/'
 
# inherit TestCase Class and create a new test class
class PythonOrgSearch(unittest.TestCase):
 
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
 
    def test_emptyInput(self):
       
        driver = self.driver
        # get webpage
        driver.get(webpageUrl+"login")
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(4)
        text = driver.find_element(By.CSS_SELECTOR, "#loginMessage").text
        self.assertEqual(text, "Invalid credentials")

    def test_register(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get(webpageUrl+"register")
 
        # locate element using name
        driver.find_element(By.NAME, "name").send_keys("")
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
        #get the text of the error message
        text = driver.find_element(By.CSS_SELECTOR, "#registerMessage").text
        self.assertEqual(text, "User validation failed: name: Path `name` is required., email: Path `email` is required., password: Path `password` is required.")

    def test_EMPTYREG(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get(webpageUrl+"register")
 
        # locate element using name
        driver.find_element(By.NAME, "name").send_keys("Yumna")
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
        #get the text of the error message
        text = driver.find_element(By.CSS_SELECTOR, "#registerMessage").text
        self.assertEqual(text, "User validation failed: email: Path `email` is required., password: Path `password` is required.")
    
    def test_credentials(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get(webpageUrl+"login")
        driver.find_element(By.NAME, "email").send_keys("test@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
       
        text = driver.find_element(By.CSS_SELECTOR, "#maincontent").text
        self.assertEqual(text, "WELCOME TO HOMEPAGE")
    
    def test_loginPage(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get(webpageUrl+"register")
 
        #click the button
        driver.find_element(By.CSS_SELECTOR, "a").click()
        #wait for 4 seconds
        time.sleep(4)

        text = driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertEqual(text, "Sign in")

    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()
