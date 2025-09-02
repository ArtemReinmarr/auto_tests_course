import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
import json
import time
import math

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)
    yield browser
    browser.quit()

@pytest.fixture(scope="session")
def cred():
    with open("cred.json", "r", encoding="utf-8") as file:
        conf = json.load(file)
        return conf

class TestLogin:
    def test_auth(self, browser, cred):
        WebDriverWait(browser, 15).until(ex.visibility_of_element_located((By.CSS_SELECTOR, "#ember479")))
        browser.find_element(By.CSS_SELECTOR, "#ember479").click()
        windows = browser.window_handles
        browser.switch_to.window(windows[-1])
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(cred["login"])
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(cred["password"])
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader ").click()
        WebDriverWait(browser, 2).until(ex.invisibility_of_element_located((By.CSS_SELECTOR, "[role='alert']")))
        
       