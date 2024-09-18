import datetime
import time
import string
import pytest
import random
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.SplitBillingMainPage import SplitBillingMainPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_check_and_process_invoice(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")

        homepage.menu_label_chargingpoints()
        cpofinancepage = homepage.menu_label_cpo_finance()
        cpofinancepage.invoices_tab()
        cpofinancepage.invoices_set_filter_unprocessed_open()
        cpofinancepage.invoices_search_field().send_keys("Autotesting Roaming")
        cpofinancepage.invoices_top_invoice()
        cpofinancepage.process_invoice_button()

        today = date.today().strftime("%Y-%m-%d")
        random_digits = str(random.randint(1000, 9999))
        invoice_number = f"{today}-{random_digits}"
        cpofinancepage.set_invoice_number().send_keys(invoice_number)
        cpofinancepage.set_invoice_number_confirm()
        cpofinancepage.overview_invoice_tab()
        cpofinancepage.invoice_tab_search().send_keys(invoice_number + Keys.ENTER)
        cpofinancepage.invoice_tab_open_top_invoice()
        cpofinancepage.close_invoice()
        cpofinancepage.overview_invoice_tab()

        invoice_status = cpofinancepage.top_invoice_status().text
        assert invoice_status == "Closed"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_check_and_process_paymentrequest(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        cpofinancepage = homepage.menu_label_cpo_finance()
        cpofinancepage.payment_requests_tab()
        cpofinancepage.payreqs_set_filter_open()
