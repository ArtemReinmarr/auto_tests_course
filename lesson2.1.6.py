from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    radio_button_people = browser.find_element(By.CSS_SELECTOR, "#peopleRule")
    checked = radio_button_people.get_attribute("checked")
    if checked is not None:
        print("Radio button People rule is not checked")
    time.sleep(12)
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    disabled = submit_button.get_attribute("disabled")
    if disabled != "true":
        print("Submit button is not disabled after 9 seconds")
    
finally:
    browser.quit()
    
    