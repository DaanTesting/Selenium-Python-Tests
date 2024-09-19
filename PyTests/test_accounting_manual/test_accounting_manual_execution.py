import datetime
import time
import string
import pytest
import random
import urllib.parse
import os.path
import requests
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.SplitBillingMainPage import SplitBillingMainPage
from pageObjects.ApiDoc import ApiDoc
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
    def test_check_and_process_SB_documents(self, setup, login_data):
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

        log.info("Getting PR number + initial status")

        SB_PR_number = cpofinancepage.top_SB_PR_number().text
        SB_PR_status = cpofinancepage.top_SB_PR_status().text

        assert SB_PR_status == "Open"

        cpofinancepage.open_top_SB_PR()

        url = self.driver.current_url
        parsed_url = urllib.parse.urlparse(url)
        PR_pk = parsed_url.path.split('/')[-2]

        log.info("Verifying Debit Note initial status")

        cpofinancepage.view_debit_notes_button()
        cpofinancepage.debit_notes_search_field().send_keys(SB_PR_number + Keys.ENTER)
        SB_DN_status = cpofinancepage.top_SB_DN_status().text

        assert SB_DN_status == "Open"

        PR_close_request = f"https://test.optimile.eu/co/api/v10/admin/split-billing/payment-requests/{PR_pk}/close/"

        headers = {
            'Authorization': 'Token b5537b38-75ee-4f6f-b5cf-601516a0b320',
        }
        
        requests.post(PR_close_request, headers=headers)

        homepage.menu_label_cpo_finance()
        cpofinancepage.payment_requests_tab()
        time.sleep(1)
        cpofinancepage.pay_req_search_field().send_keys(SB_PR_number + Keys.ENTER)

        SB_PR_status = cpofinancepage.top_SB_PR_status().text

        assert SB_PR_status == "Paid"

        cpofinancepage.debit_notes_tab()
        cpofinancepage.debit_notes_search_field().send_keys(SB_PR_number + Keys.ENTER)
        SB_DN_status = cpofinancepage.top_SB_DN_status().text

        assert SB_DN_status == "Payment request paid"

        cpofinancepage.open_top_SB_DN()

        url = self.driver.current_url
        parsed_url = urllib.parse.urlparse(url)
        DN_pk = parsed_url.path.split('/')[-2]

        PR_close_request = f"https://test.optimile.eu/co/api/v10/admin/split-billing/debit-notes/{DN_pk}/close/"

        headers = {
            'Authorization': 'Token b5537b38-75ee-4f6f-b5cf-601516a0b320',
        }
        
        requests.post(PR_close_request, headers=headers)

        homepage.menu_label_cpo_finance()
        cpofinancepage.debit_notes_tab()
        time.sleep(1)
        cpofinancepage.debit_notes_search_field().send_keys(SB_PR_number + Keys.ENTER)
        SB_DN_status = cpofinancepage.top_SB_DN_status().text

        assert SB_DN_status == "Paid"

class TestThree(BaseClass):
    def test_check_and_process_host_invoices(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        cpofinancepage = homepage.menu_label_cpo_finance()
        cpofinancepage.revenues_tab()
        time.sleep(1)
        cpofinancepage.revenues_filter_unpaid()
        cpofinancepage.open_top_host_invoice()
        HI_status = cpofinancepage.host_invoice_status().text

        assert HI_status == "No"

        cpofinancepage.mark_HI_as_paid()
        HI_status = cpofinancepage.host_invoice_status().text

        assert HI_status == "Yes"

