import time

from pom.locators.search_page import SearchPageLocators
from base.base import Base
from data.machine import MachineData


class SearchPage(Base):
    search_locators = SearchPageLocators
    machine = MachineData

    def click_link(self):
        self.element_is_click(self.search_locators.SEARCH_LINK).click()

    def check_search_page_title(self):
        return self.get_title_page(self.machine.SEARCH_PAGE_TITLE)

    def check_search_url(self):
        return self.get_url(self.machine.SEARCH_URL)