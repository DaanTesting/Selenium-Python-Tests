import pytest
import os
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects


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
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        cpocustomerpage.generate_all_customer_report()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"customers-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

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
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"locations-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

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
        homepage.menu_label_chargingpoints()
        cpotokenspage = homepage.menu_label_cpo_tokens()
        cpotokenspage.select_tokens_in_use()
        cpotokenspage.download_tokens()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache"
        downloaded_file_name = f"tokens_assigned-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        cpotokenspage.select_tokens_available()
        cpotokenspage.download_tokens()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache"
        downloaded_file_name = f"tokens_available-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

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
        homepage.menu_label_chargingpoints()
        cposimcardspage = homepage.menu_label_cpo_simcards()
        cposimcardspage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"simcards-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

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
        homepage.menu_label_chargingpoints()
        cporoamingpage = homepage.menu_label_cpo_roaming()
        cporoamingpage.export_prices()

        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"1-sp_test.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        cporoamingpage.export_cdr()

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
        homepage.menu_label_chargingpoints()
        cporeportspage = homepage.menu_label_cpo_reports()
        cporeportspage.export_excel()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"sessions-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        cporeportspage.export_csv()

        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"sessions-{formatted_date}.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSix(BaseClass):
    def test_cpo_splitbilling_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_chargingpoints()
        splitbillingmainpage = homepage.menu_label_splitbilling()
        splitbillingmainpage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"split_billing-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSeven(BaseClass):
    def test_msp_customers_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        mspcustomerpage.generate_mobility_customers_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"customers-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        mspcustomerpage.generate_mobility_users_export()
        time.sleep(10)

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"users-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        mspcustomerpage.generate_all_customers_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"customers-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        mspcustomerpage.generate_all_users_export()
        time.sleep(10)

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"users-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEight(BaseClass):
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
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"tokens_in_use-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        msptokenspage.export_available_tokens()
        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"tokens_available-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestNine(BaseClass):
    def test_msp_vouchers_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_mobility()
        mspvoucherspage = homepage.menu_label_msp_vouchers()
        mspvoucherspage.generate_export_all()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"vouchers-{formatted_date}.xlsx"
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
        homepage.menu_label_mobility()
        mspoperatorspage = homepage.menu_label_msp_operators()
        mspoperatorspage.export_service_records_button()
        mspoperatorspage.export_menu_from_field().send_keys("2022-01-01" + Keys.ENTER)
        mspoperatorspage.export_menu_until_field().send_keys("2023-12-12" + Keys.ENTER)
        mspoperatorspage.export_all_record_details()

        time.sleep(2)

        download_directory = "/Users/daanswinnen/Downloads/SeleniumCache/"
        downloaded_file_name = f"export_from_2022-01-01_until_2023-12-13.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

