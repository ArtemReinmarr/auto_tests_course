from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_value_text = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_value = x_value_text.text
    input_field = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input_field.send_keys(calc(x_value))
    check_robot = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check_robot.click()
    radio_robot_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule") 
    radio_robot_button.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
    
    