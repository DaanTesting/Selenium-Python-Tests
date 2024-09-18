import datetime
import os
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_cpo_customers_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo customers page.")
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        log.info("Attempting to generate 'all customers' report.")
        cpocustomerpage.generate_all_customer_report()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"customers-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified 'all customers' report has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_cpo_locations_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        log.info("Attempting to generate locations export.")
        locationsmainpage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"locations-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified locations export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_cpo_tokens_exports(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to tokens page.")
        homepage.menu_label_chargingpoints()
        cpotokenspage = homepage.menu_label_cpo_tokens()
        log.info("Attempting to download 'tokens in use' export")
        cpotokenspage.select_tokens_in_use()
        cpotokenspage.download_tokens()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"tokens_assigned-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified 'tokens in use'-export has been downloaded.")

        log.info("Attempting to download 'available tokens' export.")
        cpotokenspage.select_tokens_available()
        cpotokenspage.download_tokens()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"tokens_available-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified 'available tokens' export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_cpo_simcards_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to simcards page.")
        homepage.menu_label_chargingpoints()
        cposimcardspage = homepage.menu_label_cpo_simcards()
        log.info("Attempting to generate simcards export.")
        cposimcardspage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"simcards-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified simcards export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_cpo_roaming_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to roaming page.")
        homepage.menu_label_chargingpoints()
        cporoamingpage = homepage.menu_label_cpo_roaming()
        log.info("Attempting to generate prices export.")
        cporoamingpage.export_prices()

        download_directory = cache_directory
        downloaded_file_name = f"17-Arval Test.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Succesfully verified prices export has been downloaded.")

        log.info("Attempting to export cdr.")
        cporoamingpage.export_cdr()

        download_directory = cache_directory
        downloaded_file_name = f"Optimile Test Brand-cp_test-2023-01-01-2024-01-01.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)
        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        log.info("Successfully verified cdr export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSix(BaseClass):
    def test_cpo_reports_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo reports page.")
        homepage.menu_label_chargingpoints()
        cporeportspage = homepage.menu_label_cpo_reports()
        log.info("Attempting to export excel report.")
        cporeportspage.export_excel()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"sessions-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified excel report has been downloaded.")
        log.info("Attempting to export csv report.")

        cporeportspage.export_csv()

        download_directory = cache_directory
        downloaded_file_name = f"sessions-{formatted_date}.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified csv report has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSeven(BaseClass):
    def test_cpo_splitbilling_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to splitbilling page.")
        homepage.menu_label_chargingpoints()
        splitbillingmainpage = homepage.menu_label_splitbilling()
        log.info("Attempting to generate splitbilling export.")
        splitbillingmainpage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"split_billing-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified splitbilling export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEight(BaseClass):
    def test_msp_customers_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to msp customers page.")
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        log.info("Attempting to generate mobility customers export.")
        mspcustomerpage.generate_mobility_customers_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"customers-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified mobility customers export has been downloaded.")

        log.info("Attempting to generate mobility users export.")
        mspcustomerpage.generate_mobility_users_export()
        time.sleep(10)

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"users-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified mobility users export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestNine(BaseClass):
    def test_msp_tokens_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_mobility()
        msptokenspage = homepage.menu_label_msp_tokens()
        msptokenspage.export_in_use_tokens()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"tokens_assigned-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        msptokenspage.export_available_tokens()
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"tokens_available-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTen(BaseClass):
    def test_msp_vouchers_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to msp vouchers page.")
        homepage.menu_label_mobility()
        mspvoucherspage = homepage.menu_label_msp_vouchers()
        log.info("Attempting to generate all vouchers export.")
        mspvoucherspage.generate_export_all()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"vouchers-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified all vouchers export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEleven(BaseClass):
    def test_msp_operators_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to msp operators page.")

        mspoperatorspage = homepage.menu_label_msp_operators()
        log.info("Attempting to export service records.")
        mspoperatorspage.export_service_records_button()
        mspoperatorspage.export_menu_from_field().send_keys("2022-01-01" + Keys.ENTER)
        mspoperatorspage.export_menu_until_field().send_keys("2023-12-12" + Keys.ENTER)
        mspoperatorspage.export_all_record_details()

        time.sleep(2)

        download_directory = cache_directory
        downloaded_file_name = f"export_from_2022-01-01_until_2023-12-13.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified service records export has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwelve(BaseClass):
    def test_cpo_issues_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo overview page.")
        homepage.menu_label_chargingpoints()
        cpooverviewpage = homepage.menu_label_cpo_overview()
        cpooverviewpage.issues_tab()
        log.info("Attempting to generate issues csv.")
        cpooverviewpage.export_issues_csv_button()

        time.sleep(2)
        today = datetime.datetime.today()
        timestamp = today.strftime('%Y-%m-%d')

        download_directory = cache_directory
        downloaded_file_name = f"Overview_issues-{timestamp}.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified issues csv has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestThirteen(BaseClass):
    def test_cpo_adhoc_export(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo overview page.")
        homepage.menu_label_chargingpoints()
        adhocplatformpage = homepage.menu_label_adhoc()
        adhocplatformpage.export_button_excel()
        time.sleep(2)
        today = datetime.datetime.today()
        timestamp = today.strftime('%Y-%m-%d')

        download_directory = cache_directory
        downloaded_file_name = f"adhoc_sessions-{timestamp}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified adhoc xlsx has been downloaded.")

        adhocplatformpage.export_button_csv()
        time.sleep(2)
        today = datetime.datetime.today()
        timestamp = today.strftime('%Y-%m-%d')

        download_directory = cache_directory
        downloaded_file_name = f"adhoc_sessions-{timestamp}.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)
        log.info("Successfully verified adhoc csv has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()