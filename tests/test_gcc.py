import allure
from pom.pages.main_page import MainPage
from pom.pages.search_page import SearchPage
from pom.pages.calculator_page import CalculatorPage
from data.machine import MachineData


class TestGoogleCloudCalculatorFirefox:

    @allure.feature('Open page and search')
    @allure.feature('Open page in firefox browser, and search "Google cloud calculator"')
    def test_start_page(self, firefox_driver):
        main_page = MainPage(firefox_driver)
        # Open cloud search page and check
        main_page.open()
        main_page.click_input_and_paste_text()
        # Checking title page
        assert main_page.check_main_page_title(), 'Title does not match'

    @allure.feature('Click link')
    @allure.description('After search click link "Google cloud pricing calculator"')
    def test_search_page(self, firefox_driver):
        search_page = SearchPage(firefox_driver)
        # Checking title page
        # assert search_page.check_search_page_title(), 'Title does not match'
        assert search_page.check_search_url(), 'URL does not match'
        # Search target should be found and opened
        search_page.click_link()

    @allure.feature('Add data')
    @allure.description('Add data on a machine in cloud calculator')
    def test_calculator_page(self, firefox_driver):
        calculator_page = CalculatorPage(firefox_driver)
        # Checking title page
        assert calculator_page.check_calculator_page_title(), 'Title does not match'
        # Add data on a machine in cloud calculator
        calculator_page.switch_to_frame()
        calculator_page.select_compute_engine()
        calculator_page.paste_number_of_instances()
        calculator_page.select_operating_system()
        calculator_page.select_vm_class()
        calculator_page.select_series()
        calculator_page.select_machine_type()
        calculator_page.select_checkbox_gpu()
        calculator_page.select_gpu_type()
        calculator_page.select_numbers_of_gpus()
        calculator_page.select_local_ssd()
        calculator_page.select_datacenter_location()
        calculator_page.select_commit_usage()
        calculator_page.click_estimate_button()

    @allure.feature('Checking the selected data')
    @allure.description('Checking the selected data on estimate card')
    def test_check_estimate_card(self, firefox_driver):
        calculator_page = CalculatorPage(firefox_driver)
        # Checking title page
        assert calculator_page.check_calculator_page_title(), 'Title does not match'
        # Checking the selected data
        assert MachineData.REGION in calculator_page.get_text_region(), 'Region does not match'
        assert MachineData.PROVISIONING_MODEL in calculator_page.get_text_provision_model(), 'Model does not match'
        assert MachineData.COMMITMENT_TERM in calculator_page.get_text_commitment(), 'Commitment term does not match'
        assert MachineData.INSTANCE_TYPE in calculator_page.get_text_instance_type(), 'Instance type does not match'
        assert MachineData.LOCAL_SSD in calculator_page.get_text_local_ssd(), 'Local SSD does not match'
        assert MachineData.TOTAL_ESTIMATE_COST in calculator_page.get_text_total_cost(), 'Total cost does not match'


class TestGoogleCloudCalculatorChrome:

    @allure.feature('Open page and search')
    @allure.feature('Open page in chrome browser, and search "Google cloud calculator"')
    def test_start_page(self, chrome_driver):
        main_page = MainPage(chrome_driver)
        # Open cloud search page and check
        main_page.open()
        main_page.click_input_and_paste_text()
        # Checking title page
        assert main_page.check_main_page_title(), 'Title does not match'

    @allure.feature('Click link')
    @allure.description('After search click link "Google cloud pricing calculator"')
    def test_search_page(self, chrome_driver):
        search_page = SearchPage(chrome_driver)
        # Checking title page
        assert search_page.check_search_page_title(), 'Title does not match'
        # assert search_page.check_search_url(), 'URL does not match'
        # Search target should be found and opened
        search_page.click_link()

    @allure.feature('Add data')
    @allure.description('Add data on a machine in cloud calculator')
    def test_calculator_page(self, chrome_driver):
        calculator_page = CalculatorPage(chrome_driver)
        # Checking title page
        assert calculator_page.check_calculator_page_title(), 'Title does not match'
        # Add data on a machine in cloud calculator
        calculator_page.switch_to_frame()
        calculator_page.select_compute_engine()
        calculator_page.paste_number_of_instances()
        calculator_page.select_operating_system()
        calculator_page.select_vm_class()
        calculator_page.select_series()
        calculator_page.select_machine_type()
        calculator_page.select_checkbox_gpu()
        calculator_page.select_gpu_type()
        calculator_page.select_numbers_of_gpus()
        calculator_page.select_local_ssd()
        calculator_page.select_datacenter_location()
        calculator_page.select_commit_usage()
        calculator_page.click_estimate_button()

    @allure.feature('Checking the selected data')
    @allure.description('Checking the selected data on estimate card')
    def test_check_estimate_card(self, chrome_driver):
        calculator_page = CalculatorPage(chrome_driver)
        # Checking title page
        assert calculator_page.check_calculator_page_title(), 'Title does not match'
        # Checking the selected data
        assert MachineData.REGION in calculator_page.get_text_region(), 'Region does not match'
        assert MachineData.PROVISIONING_MODEL in calculator_page.get_text_provision_model(), 'Model does not match'
        assert MachineData.COMMITMENT_TERM in calculator_page.get_text_commitment(), 'Commitment term does not match'
        assert MachineData.INSTANCE_TYPE in calculator_page.get_text_instance_type(), 'Instance type does not match'
        assert MachineData.LOCAL_SSD in calculator_page.get_text_local_ssd(), 'Local SSD does not match'
        assert MachineData.TOTAL_ESTIMATE_COST in calculator_page.get_text_total_cost(), 'Total cost does not match'
