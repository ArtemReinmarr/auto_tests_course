from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    browser = webdriver.Chrome()
    browser.get(link)
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(input_value))
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()
finally:
    time.sleep(10)
    browser.quit()