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


@pytest.fixture(params=LoginPageData.qatest_login_data)
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
        cpocustomerpage = homepage.menu_label_cpo_customers()
        cpocustomerpage.generate_all_customer_report()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
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
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
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
        cpotokenspage = homepage.menu_label_cpo_tokens()
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
        cposimcardspage = homepage.menu_label_cpo_simcards()
        cposimcardspage.generate_export()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
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
        cporoamingpage = homepage.menu_label_cpo_roaming()
        cporoamingpage.export_prices()

        download_directory = cache_directory
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
        cporeportspage = homepage.menu_label_cpo_reports()
        cporeportspage.export_excel()

        today = datetime.date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        download_directory = cache_directory
        downloaded_file_name = f"sessions-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        cporeportspage.export_csv()

        download_directory = cache_directory
        downloaded_file_name = f"sessions-{formatted_date}.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
