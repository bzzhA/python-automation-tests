from selenium.webdriver.common.by import By


class Estimate:
    ESTIMATE_CARD = (By.XPATH, "//md-card-content[@id='resultBlock']//h2[text()='Estimate']")
    REGION = (By.XPATH, '//div[contains(text(),"Region")]')
    PROVISIONING_MODEL = (By.XPATH, '//div[contains(text(),"Provisioning model")]')
    COMMITMENT_TERM = (By.XPATH, '//div[contains(text(),"Commitment term")]')
    INSTANCE_TYPE = (By.XPATH, '//div[contains(text(),"Instance type")]')
    LOCAL_SSD = (By.XPATH, '//div[contains(text(),"Local SSD:")]')
    TOTAL_ESTIMATED_COST = (By.XPATH, '//b[contains(text(),"Total Estimated Cost")]')
    EMAIL_BUTTON = (By.XPATH, '//button[@title="Email Estimate"]')
    ESTIMATE_EMAIL = (By.XPATH, '//form[@name="emailForm"]/md-content/div[3]//input')
    SEND_EMAIL_ESTIMATE = (By.XPATH, '//button[contains(text(), "Send Email")]')
