import time
import pytest
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects


@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_pages_account(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_account()
        homepage.menu_label_msp_invoices()
        titlepageinvoices = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Invoices'])[1]"
        ).text
        assert titlepageinvoices == "Invoices"
        homepage.menu_label_payment_methods()
        titlepagepaymentmethods = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Payment methods'])[1]"
        ).text
        assert titlepagepaymentmethods == "Payment methods"
        accountdetailspage = homepage.menu_label_account_details()
        accountdetailspage.account_details_save_button()
        message = accountdetailspage.account_details_updated_message().text
        assert message == "Account details updated."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_profiles(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_profiles()
        homepage.menu_label_profiles_overview()
        titleprofilesoverview = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Overview'])[1]"
        ).text
        assert titleprofilesoverview == "Overview"
        tagmanagerpage = homepage.menu_label_tag_manager()
        titletagmanagerpage = tagmanagerpage.page_title().text
        assert titletagmanagerpage == "Tag manager"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_import_export(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_import_export()
        homepage.menu_label_import()
        titleimportpage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Import'])[1]"
        ).text
        assert titleimportpage == "Import"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_mobility(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_mobility_policies()
        titlemobilitypolicies = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Mobility policies'])[1]"
        ).text
        assert titlemobilitypolicies == "Mobility policies"
        homepage.menu_label_expenses()
        titleexpenses = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Expenses'])[1]"
        ).text
        assert titleexpenses == "Expenses"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_administration(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_administration_hr()
        homepage.menu_label_create_report()
        titlecreatereportpage = self.driver.find_element(By.XPATH, "(//h1[normalize-space()='Create report'])[1]").text
        assert titlecreatereportpage == "Create report"
