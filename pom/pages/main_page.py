from base.base import Base
from pom.locators.main_page import MainPageLocators
from data.machine import MachineData
from selenium.webdriver.common.keys import Keys


class MainPage(Base):
    main_locator = MainPageLocators
    machine = MachineData

    def click_input_and_paste_text(self):
        self.element_is_visible(self.main_locator.INPUT_MAIN_PAGE).click()
        self.element_is_visible(self.main_locator.INPUT_MAIN_PAGE).send_keys('Google Cloud Pricing Calculator')
        self.element_is_visible(self.main_locator.INPUT_MAIN_PAGE).send_keys(Keys.RETURN)

    def check_main_page_title(self):
        return self.get_title_page(self.machine.MAIN_PAGE_TITLE)
