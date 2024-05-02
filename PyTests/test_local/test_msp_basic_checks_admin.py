import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def _login(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        time.sleep(1)
        return homepage

    def test_msp_customers_screen(self, setup, login_data):
        homepage = self._login(login_data)
        log = self.get_logger()
        log.info("Navigating to msp customers page.")
        homepage.menu_label_mobility()
        homepage.menu_label_msp_customers()
        titlecustomerpage = self.driver.find_element(
            By.XPATH, "//h1[contains(.,'Customers')]"
        ).text
        assert "Customers" in titlecustomerpage
        log.info("Succesfully verified msp customers page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_tokens_screen(self, setup, login_data):
        homepage = self._login(login_data)
        log = self.get_logger()
        log.info("Navigating to msp tokens page.")
        homepage.menu_label_mobility()
        homepage.menu_label_msp_tokens()
        titlemsptokenspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Tokens in use'])[1]"
        ).text
        assert titlemsptokenspage == "Tokens in use"
        log.info("Succesfully verified tokens page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_vouchers_screen(self, setup, login_data):
        homepage = self._login(login_data)
        log = self.get_logger()
        log.info("Navigating to msp vouchers page.")
        homepage.menu_label_mobility()
        homepage.menu_label_msp_vouchers()
        titlevoucherspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Vouchers'])[1]"
        ).text
        assert titlevoucherspage == "Vouchers"
        log.info("Succesfully verified vouchers page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_contracts_screen(self, setup, login_data):
        homepage = self._login(login_data)
        log = self.get_logger()
        log.info("Navigating to msp contracts page.")
        homepage.menu_label_mobility()
        homepage.menu_label_msp_contracts()
        titlecontractspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Customer contracts'])[1]"
        ).text
        assert titlecontractspage == "Customer contracts"
        log.info("Succesfully verified contracts page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_operators_screen(self, setup, login_data):
        homepage = self._login(login_data)
        log = self.get_logger()
        log.info("Navigating to msp operators page.")
        homepage.menu_label_mobility()
        homepage.menu_label_msp_operators()
        titleoperatorspage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Operators'])[1]"
        ).text
        assert titleoperatorspage == "Operators"
        log.info("Succesfully verified operators page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_invoices_screen(self, setup, login_data):
        homepage = self._login(login_data)
        log = self.get_logger()
        log.info("Navigating to msp invoices page.")
        homepage.menu_label_mobility()
        homepage.menu_label_msp_invoices()
        titleinvoicespage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Invoices'])[1]"
        ).text
        assert titleinvoicespage == "Invoices"
        log.info("Succesfully verified invoices page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_msp_dashboard_screen_extended(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to CPO overview page.")
        mspoverviewpage = homepage.menu_label_msp_dashboard()

        mspoverviewpage.waiting_for_payment_tab()
        time.sleep(1)
        waitingforpaymenttitle = self.driver.find_element(By.XPATH, "//h3[.='Waiting for payment']").text
        assert waitingforpaymenttitle == "Waiting for payment"

        mspoverviewpage.assign_tokens()
        time.sleep(1)
        assigntokenstitle = self.driver.find_element(By.XPATH, "//h3[.='Assign tokens']").text
        assert assigntokenstitle == "Assign tokens"

        mspoverviewpage.sessions_tab()
        time.sleep(1)
        sessionstitle = self.driver.find_element(By.XPATH, "//h3[.='Charging sessions']").text
        assert sessionstitle == "Charging sessions"

        mspoverviewpage.new_registrations_tab()
        time.sleep(1)
        newregistrationstitle = self.driver.find_element(By.XPATH, "//h3[.='New registrations']").text
        assert newregistrationstitle == "New registrations"

        log.info("Succesfully verified CPO overview page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

        

