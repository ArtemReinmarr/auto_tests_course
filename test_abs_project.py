import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    def test_page1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("mymail@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(2)
        res = browser.find_element(By.CSS_SELECTOR, "h1")
        self.assertEqual(res.text, "Congratulations! You have successfully registered!", f"Registration Error")
        time.sleep(3)
        browser.quit()
        

    def test_page2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("mymail@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(2)
        res = browser.find_element(By.CSS_SELECTOR, "h1")
        self.assertEqual(res.text, "Congratulations! You have successfully registered!", f"Registration Error")
        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()