import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
import json
import time
import math
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.fixture(scope="class")
def cred():
    with open("cred.json", "r", encoding="utf-8") as file:
        conf = json.load(file)
        return conf
    
@pytest.fixture(scope="function")
def answ():
    answer = math.log(int(time.time()))
    return answer

links = ["236895"]

@pytest.mark.parametrize('link', links)
class TestLogin:
    def test_auth(self, browser, cred, link, answ):
        lin = f"https://stepik.org/lesson/{link}/step/1"   
        browser.get(lin)
        WebDriverWait(browser, 15).until(ex.visibility_of_element_located((By.CSS_SELECTOR, "#ember479")))
        browser.find_element(By.CSS_SELECTOR, "#ember479").click()
        windows = browser.window_handles
        browser.switch_to.window(windows[-1])
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(cred["login"])
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(cred["password"])
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader ").click()
        WebDriverWait(browser, 5).until(ex.invisibility_of_element_located((By.CSS_SELECTOR, "[role='alert']")))
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']").send_keys(str(answ))
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        WebDriverWait(browser, 5).until(ex.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        WebDriverWait(browser, 2).until(ex.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!"))
        browser.quit()
