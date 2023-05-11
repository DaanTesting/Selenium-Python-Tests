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
    def test_cpo_overview_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_overview()
        titleoverviewpage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Overview'])[1]"
            ).text
        )
        assert "Overview" in titleoverviewpage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_customers_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_customers()
        titlecustomerspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Customers'])[1]"
            ).text
        )
        assert titlecustomerspage is "Customers"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_customers_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_locations()
        titlelocationspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Locations'])[1]"
            ).text
        )
        assert titlelocationspage is "Locations"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_customers_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_tokens()
        titletokenspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Tokens in use'])[1]"
            ).text
        )
        assert "Tokens" in titletokenspage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_simcards_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_simcards()
        titlesimcardsspage = str(
            homepage.driver.find_element(
                By.XPATH,
                "(//h1[normalize-space()='List of sim cards in Simcontrol'])[1]",
            ).text
        )
        assert "sim" in titlesimcardsspage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_contracts_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_contracts()
        titlecontractspage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Device contracts'])[1]"
            ).text
        )
        assert "Device contracts" in titlecontractspage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_roaming_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_roaming()
        titleroamingpage = str(
            homepage.driver.find_element(
                By.XPATH, "(//span[normalize-space()='Roaming'])[1]"
            ).text
        )
        assert "Roaming" in titleroamingpage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_finance_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_finance()
        titlefinancepage = str(
            homepage.driver.find_element(
                By.XPATH, "(//span[normalize-space()='Finance'])[1]"
            ).text
        )
        assert "Finance" in titlefinancepage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_reports_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_cpo_reports()
        titlefinancepage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Reports'])[1]"
            ).text
        )
        assert "Reports" in titlefinancepage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_cpo_splitbilling_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        homepage.menu_label_splitbilling()
        titlefinancepage = str(
            homepage.driver.find_element(
                By.XPATH, "(//h1[normalize-space()='Split billing'])[1]"
            ).text
        )
        assert "Split billing" in titlefinancepage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
