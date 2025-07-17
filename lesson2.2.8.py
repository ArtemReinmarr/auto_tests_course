from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "11.txt")
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']").send_keys("my@mail.com")
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(10)
    browser.quit()