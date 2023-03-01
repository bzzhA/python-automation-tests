import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os


allure_report_dir = "allure/reports"
for file_name in os.listdir(allure_report_dir):
    if file_name.endswith(".json"):
        os.remove(os.path.join(allure_report_dir, file_name))

allure_report_dir = "allure/reports"
for file_name in os.listdir(allure_report_dir):
    if file_name.endswith(".png"):
        os.remove(os.path.join(allure_report_dir, file_name))

# def pytest_exception_interact(node, call, report):
#     if report.failed:
#         driver = node.funcargs.get('firefox_driver' and 'chrome_driver')
#         time.sleep(3)
#         allure.attach(driver.get_screenshot_as_png(), name='Screenshot error',
#         attachment_type=allure.attachment_type.PNG)

def pytest_exception_interact(node, call, report):
    if report.failed:
        firefox_driver = node.funcargs.get('firefox_driver')
        chrome_driver = node.funcargs.get('chrome_driver')
        if firefox_driver is not None:
            driver = firefox_driver
        elif chrome_driver is not None:
            driver = chrome_driver
        else:
            return
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(), name='Screenshot error',
                      attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope='session')
def chrome_driver():
    options_google_browser = ChromeOptions()
    options_google_browser.add_argument('--headless')
    options_google_browser.add_argument('--disable-gpu')
    options_google_browser.add_argument('--disable-dev-shm-usage')
    options_google_browser.add_argument('--window-size=1920,1080')
    # driver = webdriver.Chrome(options=options_google_browser)
    driver = webdriver.Remote(options=options_google_browser, command_executor='http://localhost:4444/wd/hub')
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def firefox_driver():
    options_mozilla_browser = FirefoxOptions()
    options_mozilla_browser.add_argument('--headless')
    options_mozilla_browser.add_argument('--disable-gpu')
    options_mozilla_browser.add_argument('--disable-dev-shm-usage')
    # options_mozilla_browser.add_argument('--window-size=1920,1080')
    # driver = webdriver.Firefox(options=options_mozilla_browser)
    driver = webdriver.Remote(options=options_mozilla_browser, command_executor='http://localhost:4444/wd/hub')
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(scope="session", params=["chrome", "firefox"])
# def driver(request):
#     if request.param == "chrome":
#         options_google_browser = ChromeOptions()
#         options_google_browser.add_argument('--headless')
#         options_google_browser.add_argument('--disable-gpu')
#         options_google_browser.add_argument('--disable-dev-shm-usage')
#         options_google_browser.add_argument('--window-size=1920,1080')
#         driver = webdriver.Remote(options=options_google_browser, command_executor='http://localhost:4444/wd/hub')
#     elif request.param == "firefox":
#         options_mozilla_browser = FirefoxOptions()
#         options_mozilla_browser.add_argument('--headless')
#         options_mozilla_browser.add_argument('--disable-gpu')
#         options_mozilla_browser.add_argument('--disable-dev-shm-usage')
#         # options_mozilla_browser.add_argument('--window-size=1920,1080')
#         driver = webdriver.Remote(options=options_mozilla_browser, command_executor='http://localhost:4444/wd/hub')
#         driver.maximize_window()
#     else:
#         raise ValueError("Invalid browser name")
#     request.addfinalizer(driver.quit)
#     return driver

# @pytest.fixture(scope="session", params=["chrome", "firefox"])
# def driver(request):
#     if request.param == "chrome":
#         options_google_browser = ChromeOptions()
#         options_google_browser.add_argument('--headless')
#         options_google_browser.add_argument('--disable-gpu')
#         options_google_browser.add_argument('--disable-dev-shm-usage')
#         options_google_browser.add_argument('--window-size=1920,1080')
#         driver = webdriver.Chrome(options=options_google_browser)
#     elif request.param == "firefox":
#         options_mozilla_browser = FirefoxOptions()
#         options_mozilla_browser.add_argument('--headless')
#         options_mozilla_browser.add_argument('--disable-gpu')
#         options_mozilla_browser.add_argument('--disable-dev-shm-usage')
#         # options_mozilla_browser.add_argument('--window-size=1920,1080')
#         driver = webdriver.Firefox(options=options_mozilla_browser)
#         driver.maximize_window()
#     else:
#         raise ValueError("Invalid browser name")
#     request.addfinalizer(driver.quit)
#     return driver
