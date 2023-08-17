import pytest
import os
import datetime
import time
from selenium.webdriver.common.by import By
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
        download_directory = "/Users/daanswinnen/Downloads/"
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
        download_directory = "/Users/daanswinnen/Downloads/"
        downloaded_file_name = f"locations-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestThree(BaseClass):
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
        download_directory = "/Users/daanswinnen/Downloads/"
        downloaded_file_name = f"locations-{formatted_date}.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()