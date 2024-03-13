import platform
import time
import os
from datetime import datetime
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory

user_os = platform.system()


@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param


class TestSubModuleOne(BaseClass):
    def test_create_budgets_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Budgets report" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.reporting_period_start().send_keys("2021-01-01" + Keys.ENTER)
        reportingpage.reporting_period_end().send_keys("2025-01-01" + Keys.ENTER)
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Budgets report" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"budgets_report.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleTwo(BaseClass):
    def test_create_expense_rulesets_report_excel(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Expense rulesets" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.select_excel_report()
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Expense rulesets" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"expense_rulesets.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleThree(BaseClass):
    def test_create_expense_rulesets_report_csv(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Expense rulesets" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Expense rulesets" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"expense_rulesets.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleFour(BaseClass):
    def test_create_expenses_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Expenses" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.reporting_period_start().send_keys("2021-01-01" + Keys.ENTER)
        reportingpage.reporting_period_end().send_keys("2025-01-01" + Keys.ENTER)
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Expenses" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"expenses.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleFive(BaseClass):
    def test_create_federal_policy_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Federal mobility policy report" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_button_end()
        time.sleep(1)
        topreport = reportingpage.top_report_name().text
        assert "Federal mobility policy report" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"federal_mobility_policy_report.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleSix(BaseClass):
    def test_create_finance_stats_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("finance stats" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.reporting_period_start().send_keys("2021-01-01" + Keys.ENTER)
        reportingpage.reporting_period_end().send_keys("2025-01-01" + Keys.ENTER)
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Finance stats" in topreport
        time.sleep(5)
        self.driver.get(self.driver.current_url)
        time.sleep(1)

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"Finance_Stats.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleSeven(BaseClass):
    def test_create_finance_extended_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Finance extended")
        actions.send_keys(Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.reporting_period_start().send_keys("2021-01-01" + Keys.ENTER)
        reportingpage.reporting_period_end().send_keys("2025-01-01" + Keys.ENTER)
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Finance extended" in topreport
        time.sleep(4)
        self.driver.get(self.driver.current_url)
        time.sleep(1)
        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"finance_extended.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleEight(BaseClass):
    def test_create_HR_extended_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("HR extended report" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_button_end()
        time.sleep(1)
        topreport = reportingpage.top_report_name().text
        assert "HR extended report" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"hr_extended_report.xlsx"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSubModuleNine(BaseClass):
    def test_create_professional_mobility_policy_report(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration_hr()

        reportingpage = homepage.menu_label_reporting()
        reportingpage.create_report_button()
        reportingpage.select_report_type()

        actions = ActionChains(self.driver)
        actions.send_keys("Professional mobility policy report" + Keys.ENTER)
        actions.perform()

        reportingpage.create_report_next_button()
        reportingpage.reporting_period_start().send_keys("2021-01-01" + Keys.ENTER)
        reportingpage.reporting_period_end().send_keys("2025-01-01" + Keys.ENTER)
        reportingpage.create_report_button_end()
        time.sleep(1)

        topreport = reportingpage.top_report_name().text
        assert "Professional mobility policy report" in topreport

        reportingpage.download_top_report()

        download_directory = cache_directory
        downloaded_file_name = f"professional_mobility_policy_report.csv"
        downloaded_file_path = os.path.join(download_directory, downloaded_file_name)

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

