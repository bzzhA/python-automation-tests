from selenium.webdriver.common.by import By


class FakeEmailLocators:
    COPY_BUTTON = (By.XPATH, '//button[@id="cprnd"]')
    MESSAGE = (By.XPATH, '//*[@class="nw"]/button[2]//span')
    FAKE_MAIL_HEADER = (By.XPATH, '//header/div[3]/div[1]')
    FAKE_MAIL_FRAME = (By.XPATH, '//*[@id="ifmail"]')
    REFRESH_BUTTON = (By.ID, 'refresh')
    TOTAL_ESTIMATE_COST_ON_EMAIL = (By.XPATH, "//div[@id='mail']//h3[contains(text(),'USD')]")
