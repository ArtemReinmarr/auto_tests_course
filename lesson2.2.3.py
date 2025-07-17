from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    su = str(num1 + num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(su)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
finally:
    time.sleep(10)
    browser.quit()
