from pom.pages.main_page import MainPage
from pom.pages.search_page import SearchPage
from pom.pages.calculator_page import CalculatorPage
from pom.pages.yop_email_page import YopEmailPage
from data.machine import MachineData
import allure


class TestGoogleCloudCalculatorFirefox:
    @allure.feature('Open page and search')
    @allure.description('Open calculator page on firefox browser and search Cloud Calculator')
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
        # assert search_page.check_search_url(), 'URL does not match'
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

    @allure.feature('Switch on fake email window and click copy fakemail, after return back calculator page')
    @allure.description('Open new window YOPmail and copy fake email'
                        'Switch window on calculator and send message on fake email')
    def test_get_cost_on_fake_email(self, firefox_driver):
        calculator_page = CalculatorPage(firefox_driver)
        yop_page = YopEmailPage(firefox_driver)
        yop_page.new_window()
        yop_page.switch_to_yop_page()
        yop_page.open_fake_mail()
        yop_page.copy_fake_email()
        calculator_page.switch_to_base_page()
        calculator_page.switch_to_frame()
        calculator_page.click_estimate_email_button()
        calculator_page.paste_estimate_email()
        calculator_page.click_send_email()
        yop_page.switch_to_yop_page()
        yop_page.click_check_post()
        yop_page.click_refresh()
        yop_page.switch_yop_mail_frame()

    @allure.feature('Compare price')
    @allure.description('Switch to YOPmail window and Compare price machine between calculator to email message')
    def test_compare_price_in_calculator_to_email_message(self, firefox_driver):
        yop_page = YopEmailPage(firefox_driver)
        assert MachineData.TOTAL_ESTIMATE_COST in yop_page.get_price(), 'Price does not match'


class TestGoogleCloudCalculatorChrome:
    @allure.feature('Open page and search')
    @allure.description('Open calculator page on chrome browser and search Cloud Calculator')
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
        # assert search_page.check_search_page_title(), 'Title does not match'
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

    @allure.feature('Switch on fake email window and click copy fakemail, after return back calculator page')
    @allure.description('Open new window YOPmail and copy fake email'
                        'Switch window on calculator and send message on fake email')
    def test_get_cost_on_fake_email(self, chrome_driver):
        calculator_page = CalculatorPage(chrome_driver)
        yop_page = YopEmailPage(chrome_driver)
        yop_page.new_window()
        yop_page.switch_to_yop_page()
        yop_page.open_fake_mail()
        yop_page.copy_fake_email()
        calculator_page.switch_to_base_page()
        calculator_page.switch_to_frame()
        calculator_page.click_estimate_email_button()
        calculator_page.paste_estimate_email()
        calculator_page.click_send_email()
        yop_page.switch_to_yop_page()
        yop_page.click_check_post()
        yop_page.click_refresh()
        yop_page.switch_yop_mail_frame()

    @allure.feature('Compare price')
    @allure.description('Switch to YOPmail window and Compare price machine between calculator to email message')
    def test_compare_price_in_calculator_to_email_message(self, chrome_driver):
        yop_page = YopEmailPage(chrome_driver)
        assert MachineData.TOTAL_ESTIMATE_COST in yop_page.get_price(), 'Price does not match'
