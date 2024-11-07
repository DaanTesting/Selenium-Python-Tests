import datetime
import time
import string
import pytest
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.SplitBillingMainPage import SplitBillingMainPage
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.AdhocSetupData import AdhocSetupData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.staging_login_data)
def login_data(request):
    return request.param


@pytest.fixture(params=AdhocSetupData.test_adhoc_data)
def adhoc_data(request):
    return request.param


class TestOne(BaseClass):
    def test_adhoc_page_search(self, setup, login_data, adhoc_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to split billing page.")
        homepage.menu_label_chargingpoints()
        adhocplatformpage = homepage.menu_label_adhoc()
        adhocplatformpage.search_bar().send_keys(
            adhoc_data["AdhocDevice"] + Keys.ENTER
        )
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tbody/tr/td[1]/a")
        for result in results:
            assert adhoc_data["AdhocDevice"] in result.text
        log.info("Verified only correct sessions show up.")

        adhocplatformpage.search_bar().clear()
        adhocplatformpage.search_bar().send_keys(
            adhoc_data["AdhocCustomer"] + Keys.ENTER
        )
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tbody/tr/td[2]/a")
        for result in results:
            assert adhoc_data["AdhocCustomer"] in result.text
        log.info("Verified only adhoc customer sessions show up.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()