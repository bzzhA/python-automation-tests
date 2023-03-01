from selenium.webdriver.common.by import By

class CalculatorPageLocators:

    FIRST_FRAME = (By.XPATH, "//article[contains(@id, 'cloud-site')]//iframe")
    SECOND_FRAME = (By.ID, 'myFrame')
    NUMBER_OF_INSTANCES = (By.XPATH, "//input[contains(@ng-model, 'quantity')]")
    COMPUTE_ENGINE = (By.XPATH, '//md-tab-item[1]/div/div')
    OPERATING_SYSTEM = (By.XPATH, '//md-select[@ng-model="listingCtrl.computeServer.os"]')
    FREE_OPERATING_SYSTEM = (By.XPATH, "//md-option[@value='free']")
    VM_CLASS = (By.XPATH, '//md-select[@placeholder="VM Class"]')
    VM_CLASS_OPTION = (By.XPATH, '//md-option[@value="regular"]')
    SERIES = (By.XPATH, '//md-select[@placeholder="Series"]')
    SERIES_OPTION = (By.XPATH, '//md-option[@value="n1"]')
    MACHINE_TYPE = (By.XPATH, '//md-select[@placeholder="Instance type"]')
    MACHINE_TYPE_OPTION = (By.XPATH, '//md-option[@value="CP-COMPUTEENGINE-VMIMAGE-N1-STANDARD-8"]')
    CHECKBOX_GPU = (By.XPATH, "//form[@name='ComputeEngineForm']//md-checkbox[@aria-label='Add GPUs']")
    GPUS_TYPE = (By.XPATH, '//*[@placeholder="GPU type"]')
    GPUS_TYPE_OPTION = (By.XPATH, '//md-option[@value="NVIDIA_TESLA_P100"]')
    NUMBER_GPUS = (By.XPATH, '//*[@placeholder="Number of GPUs"]')
    NUMBER_GPUS_OPTION = (By.XPATH, "//div[@id='select_container_471']//md-option[@value='1']")
    LOCAL_SSD = (By.XPATH, '//form[@name="ComputeEngineForm"]//md-select[@placeholder="Local SSD"]')
    LOCAL_SSD_OPTION = (By.XPATH, "//md-select-menu[@role='presentation']//md-option//div[contains(text(), '2x375')]")
    DATACENTER_LOCATION = (By.XPATH, '//form[@name="ComputeEngineForm"]//md-select[@placeholder="Datacenter location"]')
    DATACENTER_LOCATION_OPTION = (By.XPATH, "//div[@class='md-select-menu-container cpc-region-select md-active md-clickable']//md-option//div[contains(text(), 'Frankfurt')]")
    COMMIT_USAGE = (By.XPATH, '//form[@name="ComputeEngineForm"]//md-select[@placeholder="Committed usage"]')
    COMMIT_USAGE_OPTION = (By.XPATH, "//md-option[@id='select_option_132']//div[1]")
    ESTIMATE_BUTTON = (By.XPATH, '//form[@name="ComputeEngineForm"]//button[@class="md-raised md-primary cpc-button md-button md-ink-ripple"]')
    ESTIMATE_CARD = (By.ID, '#resultBlock')
    CALCULATOR_PAGE_TITLE = (By.XPATH, '//title[contains(text(), "Google Cloud Pricing")]')
