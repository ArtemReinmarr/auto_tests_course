from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    browser.switch_to.alert.accept()
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(int(input_value)))
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(10)
    browser.quit()
