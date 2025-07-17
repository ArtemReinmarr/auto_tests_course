from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
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
    
    assert res.text == "Congratulations! You have successfully registered!", f"Registration Error"

finally:
    time.sleep(15)
    browser.quit()
