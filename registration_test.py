from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration(self):
        url = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(url)

        try:
            # Используем уникальные селекторы: по placeholder'у
            input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
            input3.send_keys("test@example.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            # Проверяем текст успешной регистрации
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(3)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
