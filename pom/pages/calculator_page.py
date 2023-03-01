from pom.locators.calculator_page import CalculatorPageLocators
from pom.locators.estimate_card import Estimate
from data.machine import MachineData
from base.base import Base
from selenium.webdriver.common.keys import Keys


class CalculatorPage(Base):
    calculator_locators = CalculatorPageLocators
    estimate_locators = Estimate
    machine = MachineData

    def switch_to_frame(self):
        self.switch_frame(self.calculator_locators.FIRST_FRAME)
        self.switch_frame(self.calculator_locators.SECOND_FRAME)

    def switch_to_base_page(self):
        self.switch_window(0)

    def select_compute_engine(self):
        self.element_is_visible(self.calculator_locators.COMPUTE_ENGINE).click()

    def paste_number_of_instances(self):
        self.element_is_visible(self.calculator_locators.NUMBER_OF_INSTANCES).send_keys('4')

    def select_operating_system(self):
        self.element_is_visible(self.calculator_locators.OPERATING_SYSTEM).click()
        self.element_is_visible(self.calculator_locators.FREE_OPERATING_SYSTEM).click()

    def select_vm_class(self):
        self.element_is_visible(self.calculator_locators.VM_CLASS).click()
        self.element_is_visible(self.calculator_locators.VM_CLASS_OPTION).click()

    def select_series(self):
        self.element_is_visible(self.calculator_locators.SERIES).click()
        self.element_is_visible(self.calculator_locators.SERIES_OPTION).click()

    def select_machine_type(self):
        self.element_is_visible(self.calculator_locators.MACHINE_TYPE).click()
        self.element_is_visible(self.calculator_locators.MACHINE_TYPE_OPTION).click()

    def select_checkbox_gpu(self):
        self.element_is_visible(self.calculator_locators.CHECKBOX_GPU).click()

    def select_gpu_type(self):
        self.element_is_visible(self.calculator_locators.GPUS_TYPE).click()
        self.element_is_visible(self.calculator_locators.GPUS_TYPE_OPTION).click()

    def select_numbers_of_gpus(self):
        self.element_is_visible(self.calculator_locators.NUMBER_GPUS).click()
        self.element_is_visible(self.calculator_locators.NUMBER_GPUS_OPTION).click()

    def select_local_ssd(self):
        self.element_is_visible(self.calculator_locators.LOCAL_SSD).click()
        self.element_is_visible(self.calculator_locators.LOCAL_SSD_OPTION).click()

    def select_datacenter_location(self):
        self.element_is_visible(self.calculator_locators.DATACENTER_LOCATION).click()
        self.element_is_visible(self.calculator_locators.DATACENTER_LOCATION_OPTION).click()

    def select_commit_usage(self):
        self.element_is_visible(self.calculator_locators.COMMIT_USAGE).click()
        self.element_is_visible(self.calculator_locators.COMMIT_USAGE_OPTION).click()

    def click_estimate_button(self):
        self.element_is_visible(self.calculator_locators.ESTIMATE_BUTTON).click()

    def click_estimate_email_button(self):
        self.element_is_visible(self.estimate_locators.EMAIL_BUTTON).click()

    def paste_estimate_email(self):
        self.element_is_visible(self.estimate_locators.ESTIMATE_EMAIL).click()
        self.element_is_visible(self.estimate_locators.ESTIMATE_EMAIL).send_keys(Keys.COMMAND + 'V')

    def click_send_email(self):
        self.element_is_visible(self.estimate_locators.SEND_EMAIL_ESTIMATE).click()

    def get_text_region(self):
        return self.get_text(self.estimate_locators.REGION)

    def get_text_provision_model(self):
        return self.get_text(self.estimate_locators.PROVISIONING_MODEL)

    def get_text_commitment(self):
        return self.get_text(self.estimate_locators.COMMITMENT_TERM)

    def get_text_instance_type(self):
        return self.get_text(self.estimate_locators.INSTANCE_TYPE)

    def get_text_local_ssd(self):
        return self.get_text(self.estimate_locators.LOCAL_SSD)

    def get_text_total_cost(self):
        return self.get_text(self.estimate_locators.TOTAL_ESTIMATED_COST)

    def check_calculator_page_title(self):
        return self.get_title_page(self.machine.CALCULATOR_PAGE_TITLE)
