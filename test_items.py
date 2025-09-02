import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

def test_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(button) > 0, f"Button not found"

if __name__ == "__main__":
    pytest.main()