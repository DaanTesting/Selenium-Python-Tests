import datetime
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


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

        homepage.menu_label_payment_requests()
        titlepagepaymentrequests = self.driver.find_element(By.XPATH, "//h1[contains(.,'Payment requests')]").text
        assert titlepagepaymentrequests == "Payment requests"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
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
        title_accountdetailspage = accountdetailspage.account_details_title().text
        assert title_accountdetailspage == "Account details"
        log.info("Succesfully verified account details page.")

        accountdetailspage.account_details_save_button()
        message = accountdetailspage.account_details_updated_message().text
        assert message == "Account details updated."
        log.info("Succesfully updated account details.")

        tagmanagerpage = homepage.menu_label_tag_manager()
        title_tagmanagerpage = tagmanagerpage.page_title().text
        assert title_tagmanagerpage == "Tag manager\nCreate tag"
        log.info("Succesfully verified tag manager page.")

        homepage.menu_label_administration()

        externaluserspage = homepage.menu_label_external_users()
        title_externaluserspage = externaluserspage.page_title().text
        assert title_externaluserspage == "External users"
        log.info("Succesfully verified external users page.")

        userinvitespage = homepage.menu_label_user_invites()
        title_usersinvitespage = userinvitespage.page_title().text
        assert title_usersinvitespage == 'User invites'
        log.info("Succesfully verified User invites page.")

        reportingpage = homepage.menu_label_reporting()
        title_reportingpage = reportingpage.page_title().text
        assert title_reportingpage == "Reports\nCreate report"
        log.info("Succesfully verified reporting page")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
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
            By.XPATH, "//h1[.='Import employees']"
        ).text
        assert titleimportpage == "Import employees"
        log.info("Succesfully verified import-page.")

        homepage.menu_label_profiles_overview()
        titleprofilesoverview = self.driver.find_element(
            By.XPATH, "(//h1[.='Overview'])"
        ).text
        assert titleprofilesoverview == "Overview"
        log.info("Succesfully verified overview-page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_user_detail(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to employee overview.")
        homepage.menu_label_employees()
        hrprofilesoverview = homepage.menu_label_profiles_overview()
        log.info("Opening Auto 10 User 10's profile by clicking on name.")
        userdetailpage = hrprofilesoverview.profile_overview_click_name()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='Personal']")))
        log.info("Attempting to verify presence of all relevant elements.")
        userdetailpage.userdetail_verify_presence_personal_elements()
        log.info("Succesfully verified page elements.")
        log.info("Opening employment subtab.")
        userdetailpage.userdetail_select_employment_tab()
        userdetailpage.userdetail_verify_presence_employment_elements()
        log.info("Successfully verified employment subtab.")
        log.info("Opening financial info subtab.")
        userdetailpage.userdetail_select_financialinfo_tab()
        userdetailpage.userdetail_verify_presence_financialinfo_elements()
        log.info("Succesfully verified financial info subtab.")
        log.info("Opening identifiers subtab.")
        userdetailpage.userdetail_select_identifiers_tab()
        userdetailpage.userdetail_verify_presence_identifiers_elements()
        log.info("Succesfully verified securex subtab.")
        log.info("Attempting to navigate to the next user.")
        userdetailpage.userdetail_next_previous()
        log.info("Succesfully navigated to the next user detail.")
        log.info("Returning to profiles overview.")

        userdetailpage.userdetail_return_to_overview()
        log.info("Attempting to open profile through view-option.")
        userdetailpage.profile_overview_view_profile()
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='Personal']")))
        userinfotitle = self.driver.find_element(By.XPATH, "//h5[.='User info']").text
        assert userinfotitle == "User info"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_ruleset_overview(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to ruleset overview.")
        homepage.menu_label_mobility()
        ruleengineoverview = homepage.menu_label_rule_engine()
        rulesetoverviewtitle = str(ruleengineoverview.ruleset_overview_title().text)
        assert "Expense rule engine" in rulesetoverviewtitle

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSix(BaseClass):
    def test_federal_budgets(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        federalbudgetspage = homepage.menu_label_federal_budgets()
        federalbudgetspage.budget_management_tab()
        federalbudgetspage.budget_creation_tab()
        pagetitle = self.driver.find_element(By.XPATH, "//h1[@class='title-with-button']").text
        assert "Federal mobility budgets" in pagetitle

class TestSeven(BaseClass):
    def test_federal_policies(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_federal_policies()
        
        pagetitle = self.driver.find_element(By.XPATH, "//h1[@class='title-with-button']").text
        assert "Federal mobility policies" in pagetitle
    
class TestNine(BaseClass):
    def test_professional_policies(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        homepage.menu_label_professional_policies()
        
        pagetitle = self.driver.find_element(By.XPATH, "//h1[@class='title-with-button']").text
        assert "Professional mobility policies" in pagetitle