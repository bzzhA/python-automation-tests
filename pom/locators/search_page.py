from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_LINK = (By.XPATH, '//div[@class="gsc-thumbnail-inside"]//a[@class="gs-title"]//b[contains(text(), "Google Cloud Pricing Calculator")]')
