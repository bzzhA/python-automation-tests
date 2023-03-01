from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_MAIN_PAGE = (By.XPATH, '//input[@aria-label="Search"]')
    TITLE_MAIN_PAGE = (By.XPATH, "//title[contains(text(), 'Google')]")
