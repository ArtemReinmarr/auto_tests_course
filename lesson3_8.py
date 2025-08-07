import json
import time
import math
import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def wrong_results():
    return []

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def auth():
    with open("cred.json", "r", encoding="utf-8") as file: 
        creds = json.load(file)
        return creds

@pytest.fixture(scope="function")
def answer():
    res = math.log(int(time.time()))
    return res

links = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


def test_auth(browser, auth):
    link = f"https://stepik.org/lesson/{links[0]}/step/1"
    browser.get(link)
    WebDriverWait(browser, 15).until(ex.visibility_of_element_located((By.CSS_SELECTOR, "#ember479")))
    browser.find_element(By.CSS_SELECTOR, "#ember479").click()
    browser.switch_to.window(browser.window_handles[-1])
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(auth["login"])
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(auth["password"])
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
    try:
        browser.find_element(By.CSS_SELECTOR, "[role='alert']")
        print("Login fail")
    except:
        print("Login successfull")

@pytest.mark.parametrize('page', links)
def test_send_answer(browser,page, answer, wrong_results):
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)
    try:
        WebDriverWait(browser, 10).until(ex.visibility_of_element_located((By.CSS_SELECTOR, ".again-btn")))
        browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
    except:
        print("No again button")
    WebDriverWait(browser, 10).until(ex.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']")))
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']").send_keys(str(answer))
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    print("push")
    result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    if result != "Correct!":
        wrong_results.append(result)
    assert result == "Correct!", f"{result}"

def test_print(wrong_results):
    print("".join(wrong_results))
            

if __name__ == "__main__":
    pytest.main()


