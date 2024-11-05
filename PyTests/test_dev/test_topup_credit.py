import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass

@pytest.fixture(params=LoginPageData.staging_customer_login_data)
def login_data(request):
    return request.param

@pytest.fixture(params=LoginPageData.dev_stripe_login_data)
def login_data2(request):
    return request.param


class TestOne(BaseClass):
    def test_topup_credit_adyen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to finance tab.")
        homepage.menu_label_finance()
        log.info("Navigating to credit page.")
        creditpage = homepage.menu_label_credit()
        creditpage.add_credit_button()
        creditpage.credit_amount_field().send_keys("100")
        creditpage.select_existing_mandate()
        creditpage.continue_button()
        time.sleep(10)
        status = self.driver.find_element(By.XPATH, "//tr[4]/td").text
        assert status == "confirmed"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_topup_credit_stripe(self, setup, login_data2):
        log = self.get_logger()
        log.info("Attempting login.")
        self.driver.get(login_data2['URL'])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data2['account'])
        loginpage.password_box().send_keys(login_data2['password'])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to finance tab.")
        homepage.menu_label_finance()
        log.info("Navigating to credit page.")
        creditpage = homepage.menu_label_credit()
        creditpage.add_credit_button()
        creditpage.credit_amount_field().send_keys("100")
        creditpage.select_existing_mandate()
        creditpage.continue_button()
        time.sleep(10)
        status = self.driver.find_element(By.XPATH, "//tr[4]/td").text
        assert status == "confirmed"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
