from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as WAIT
from selenium.webdriver.support import expected_conditions as EC


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://cloud.google.com/'
        self.fake_mail_url = 'https://yopmail.com/ru/email-generator'

    def open(self):
        self.driver.get(self.base_url)

    def switch_window(self, window_number):
        handles = self.driver.window_handles
        return self.driver.switch_to.window(handles[window_number])

    def open_new_window(self):
        self.driver.execute_script("window.open('');")

    def open_fake_mail(self):
        self.driver.get(self.fake_mail_url)

    def switch_frame(self, locator, timeout=10):
        return WAIT(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def element_is_click(self, locator, timeout=10) -> WebElement:
        return WAIT(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator, timeout=10) -> WebElement:
        return WAIT(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_text(self, locator, timeout=10):
        element = WAIT(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_title_page(self, title_text, timeout=10):
        return WAIT(self.driver, timeout).until(EC.title_contains(title_text))

    def get_url(self, url_contains, timeout=10):
        return WAIT(self.driver, timeout).until(EC.url_contains(url_contains))
