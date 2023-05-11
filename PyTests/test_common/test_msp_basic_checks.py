import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_msp_customers_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_msp_customers()
        titlecustomerpage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Customers'])[1]"
        ).text
        assert titlecustomerpage == "Customers"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_tokens_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_msp_tokens()
        titlemsptokenspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Tokens in use'])[1]"
        ).text
        assert titlemsptokenspage == "Tokens in use"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_vouchers_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_msp_vouchers()
        titlevoucherspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Vouchers'])[1]"
        ).text
        assert titlevoucherspage == "Vouchers"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_contracts_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_msp_contracts()
        titlecontractspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Customer contracts'])[1]"
        ).text
        assert titlecontractspage == "Customer contracts"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_operators_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_msp_operators()
        titleoperatorspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Operators'])[1]"
        )
        assert titleoperatorspage == "Operators"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_invoices_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_msp_invoices()
        titleinvoicespage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Invoices'])[1]"
        ).text
        assert titleinvoicespage == "Invoices"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
