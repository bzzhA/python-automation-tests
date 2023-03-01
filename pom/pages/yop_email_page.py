import time

from pom.locators.yop_mail_page import FakeEmailLocators
from base.base import Base


class YopEmailPage(Base):
    yop_mail_locators = FakeEmailLocators

    def copy_fake_email(self):
        self.element_is_visible(self.yop_mail_locators.COPY_BUTTON).click()

    def switch_to_yop_page(self):
        self.switch_window(1)

    def new_window(self):
        self.open_new_window()

    def click_check_post(self):
        self.element_is_visible(self.yop_mail_locators.MESSAGE).click()

    def switch_yop_mail_frame(self):
        self.switch_frame(self.yop_mail_locators.FAKE_MAIL_FRAME)

    def click_refresh(self):
        time.sleep(5)
        self.element_is_visible(self.yop_mail_locators.REFRESH_BUTTON).click()

    def get_price(self):
        return self.get_text(self.yop_mail_locators.TOTAL_ESTIMATE_COST_ON_EMAIL)
