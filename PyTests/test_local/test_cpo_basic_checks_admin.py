import pytest
import time
from selenium.webdriver.common.by import By

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test_local_admin_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_cpo_overview_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to CPO overview page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_overview()

        assert self.driver.find_element(By.CSS_SELECTOR, "#mapDivId")
        log.info("Verifying overview map is present.")

        titleoverviewpage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Overview'])[1]"
            ).text
        )
        assert titleoverviewpage == "Overview"
        log.info("Succesfully verified CPO overview page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_cpo_customers_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to CPO customers page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_customers()
        titlecustomerspage = str(
            self.driver.find_element(
                By.XPATH, "//h1[contains(.,'Customers')]"
            ).text
        )
        assert "Customers" in titlecustomerspage
        log.info("Succesfully verified customers page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_cpo_charging_locations_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to charging locations page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_locations()
        titlelocationspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Locations'])[1]"
            ).text
        )
        assert titlelocationspage == "Locations"
        log.info("Succesfully verified locations page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_cpo_tokens_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to tokens page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_tokens()
        titletokenspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Tokens in use'])[1]"
            ).text
        )
        assert "Tokens" in titletokenspage
        log.info("Succesfully verified tokens page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_cpo_simcards_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to simcards page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_simcards()
        titlesimcardsspage = str(
            homepage.driver.find_element(
                By.XPATH,
                "(//h1[normalize-space()='List of sim cards in Simcontrol'])[1]",
            ).text
        )
        assert "sim" in titlesimcardsspage
        log.info("Succesfully verified simcards page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSix(BaseClass):
    def test_cpo_contracts_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to contracts page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_contracts()
        titlecontractspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Device contracts'])[1]"
            ).text
        )
        assert "Device contracts" in titlecontractspage
        log.info("Succesfully verified contracts page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSeven(BaseClass):
    def test_cpo_roaming_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to roaming page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_roaming()
        titleroamingpage = str(
            homepage.driver.find_element(
                By.XPATH, "(//span[normalize-space()='Roaming'])[1]"
            ).text
        )
        assert "Roaming" in titleroamingpage
        log.info("Succesfully verified roaming page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEight(BaseClass):
    def test_cpo_finance_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to finance page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_finance()
        titlefinancepage = str(
            homepage.driver.find_element(
                By.XPATH, "(//span[normalize-space()='Finance'])[1]"
            ).text
        )
        assert "Finance" in titlefinancepage
        log.info("Succesfully verified finance page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestNine(BaseClass):
    def test_cpo_reports_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo reports page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_reports()
        time.sleep(1)
        titlefinancepage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Reports'])[1]"
            ).text
        )
        assert "Reports" in titlefinancepage
        log.info("Succesfully verified reports page.")
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTen(BaseClass):
    def test_cpo_splitbilling_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to splitbilling page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_splitbilling()
        titlefinancepage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Split billing'])[1]"
            ).text
        )
        assert "Split billing" in titlefinancepage
        log.info("Succesfully verified split billing page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEleven(BaseClass):
    def test_cpo_pricing_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo reports page.")
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_pricing()
        titlepricingpage = str(
            homepage.driver.find_element(
                By.XPATH, "//h1[.='Pricing policies']"
            ).text
        )
        assert "Pricing policies" in titlepricingpage
        log.info("Succesfully verified reports page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwelve(BaseClass):
    def test_cpo_overview_screen_extended(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to CPO overview page.")
        homepage.menu_label_chargingpoints()
        cpooverviewpage = homepage.menu_label_cpo_overview()

        cpooverviewpage.sessions_tab()
        assert self.driver.find_element(By.CSS_SELECTOR, "#mapDivId")
        log.info("Verifying overview map is present.")

        titleoverviewpage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Overview'])[1]"
            ).text
        )
        assert titleoverviewpage == "Overview"

        cpooverviewpage.issues_tab()
        time.sleep(1)
        tableheader = self.driver.find_element(By.XPATH, "//th[2]").text
        assert tableheader == "Start time"

        log.info("Succesfully verified CPO overview page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
