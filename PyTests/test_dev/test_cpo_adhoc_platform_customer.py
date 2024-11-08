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


@pytest.fixture(params=LoginPageData.staging_customer_login_data)
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
        adhocplatformpage.search_bar().send_keys(adhoc_data["AdhocDevice"] + Keys.ENTER)
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tbody/tr/td[1]/a")
        for result in results:
            assert adhoc_data["AdhocDevice"] in result.text
        log.info("Verified only ABSDEV sessions show up.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_payter_settings(self, setup, login_data):
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
        paytersettingstab = adhocplatformpage.payter_settings_tab()

        paytersettingstab.starting_price_margin().clear()
        paytersettingstab.starting_price_margin().send_keys("0")
        paytersettingstab.starting_price_fixed().clear()
        paytersettingstab.starting_price_fixed().send_keys("5")

        paytersettingstab.hourly_price_margin().clear()
        paytersettingstab.hourly_price_margin().send_keys("100")
        paytersettingstab.hourly_price_fixed().clear()
        paytersettingstab.hourly_price_fixed().send_keys("0")

        paytersettingstab.kwh_price_margin().clear()
        paytersettingstab.kwh_price_margin().send_keys("100")
        paytersettingstab.kwh_price_fixed().clear()
        paytersettingstab.kwh_price_fixed().send_keys("0")

        paytersettingstab.save_button()
        message = paytersettingstab.message_alert().text
        assert "Adhoc markup updated." in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestThree(BaseClass):
    def test_adhoc_page_filters(self, setup, login_data):
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
        adhocplatformpage.filter_adhoc()
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//td/span")
        for result in results:
            assert "Ad hoc" in result.text
        log.info("Verified only Ad hoc payments show up.")
        adhocplatformpage.filter_clear()
        time.sleep(1)

        adhocplatformpage.filter_payment_page()
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tr/td[8]/div")
        for result in results:
            assert "Payment page" in result.text
        log.info("Verified only Payment page types show up.")
        adhocplatformpage.filter_clear()
        time.sleep(1)

        adhocplatformpage.filter_payter()
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tr/td[8]/div")
        for result in results:
            assert "Payter" in result.text
        log.info("Verified only Payment page types show up.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

