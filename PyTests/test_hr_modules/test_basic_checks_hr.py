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
    def test_pages_finance(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to finance-pages.")

        homepage.menu_label_finance()
        homepage.menu_label_msp_invoices()
        titlepageinvoices = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Invoices'])[1]"
        ).text
        assert titlepageinvoices == "Invoices"
        log.info("Succesfully verified invoices-page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_administration(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to administration-pages.")

        homepage.menu_label_administration()
        accountdetailspage = homepage.menu_label_account_details()
        titleaccountdetailspage = accountdetailspage.account_details_title().text
        assert titleaccountdetailspage == "Account details"
        log.info("Succesfully verified account details page.")

        accountdetailspage.account_details_save_button()
        message = accountdetailspage.account_details_updated_message().text
        assert message == "Account details updated."
        log.info("Succesfully updated account details.")

        tagmanagerpage = homepage.menu_label_tag_manager()
        titletagmanagerpage = tagmanagerpage.page_title().text
        assert titletagmanagerpage == "Tag manager"
        log.info("Succesfully verified tag manager page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_employees(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to employees pages.")

        homepage.menu_label_employees()
        homepage.menu_label_import()
        titleimportpage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Import'])[1]"
        ).text
        assert titleimportpage == "Import"
        log.info("Succesfully verified import-page.")

        homepage.menu_label_create_report()
        titlecreatereportpage = self.driver.find_element(
            By.XPATH, "(//h1[normalize-space()='Create report'])[1]"
        ).text
        assert titlecreatereportpage == "Create report"
        log.info("Succesfully verified report-page.")

        homepage.menu_label_profiles_overview()
        titleprofilesoverview = self.driver.find_element(
            By.XPATH, "(//h1[.='Overview'])"
        ).text
        assert titleprofilesoverview == "Overview"
        log.info("Succesfully verified overview-page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_pages_mobility_policies(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility-pages.")

        homepage.menu_label_mobility_policies()
        titlemobilitypolicies = self.driver.find_element(
            By.XPATH, "//span[.='Mobility policies']"
        ).text
        assert titlemobilitypolicies == "Mobility policies"
        log.info("Succesfully verified mobility policies-page.")

        homepage.menu_label_expenses()
        titleexpenses = self.driver.find_element(
            By.XPATH, "//h1[.='Expenses']"
        ).text
        assert titleexpenses == "Expenses"
        log.info("Succesfully verified expenses-page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()