import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action="store", default="en", help="Choose language: en or ru")
'''
@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
'''
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument('--incognito')
    options.add_experimental_option('prefs', {'intl.accept.languages': user_language})
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()