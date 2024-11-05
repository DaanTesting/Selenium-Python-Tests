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


@pytest.fixture(params=LoginPageData.staging_customer_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_cpo_customer_adhoc_export(self, setup, login_data):
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