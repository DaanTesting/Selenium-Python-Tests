import random
import time

import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_create_user_and_contract(self, setup, login_data):
        log = self.get_logger()
        log.info("daan.swinnen+splitbilling4@optimile.eu")
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(
            "daan.swinnen+splitbilling4@optimile.eu"
        )
        loginpage.password_box().send_keys("hHsxpRXGX9NrN4aw6iCH")
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to users page.")
        manageuserspage = homepage.menu_label_administration_users()
        log.info("Attempting to create new user.")
        manageuserspage.create_user_button()
        log.info("Creating random emailadres.")
        random_num = str(random.randint(1000, 9999))
        self.newestuser = "daan.swinnen+" + random_num + "@optimile.eu"
        manageuserspage.create_user_email_field().send_keys(self.newestuser)
        manageuserspage.checkbox_account_admin()
        log.info("Attempting to save new user.")
        manageuserspage.create_user_save_button()
        time.sleep(1)
        message = manageuserspage.user_created_message().text
        assert "User created:" in message
        log.info("Succesfully created new user.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        log.info("Navigating to msp customers page.")
        mspcustomerpage = homepage.menu_label_customers()
        log.info("Searching for 'Automated Test Company'.")
        mspcustomerpage.search_by_name_field().send_keys(
            "Automated Test Company Main Flow" + Keys.ENTER
        )
        log.info("Open 'Automated Test Company'.")
        mspindividualcustomer = mspcustomerpage.click_on_main_flow_account()

        log.info("Attempting to create new contract.")
        mspindividualcustomer.contracts_tab()
        mspindividualcustomer.create_contract_button()
        log.info("Selecting contract.")
        mspindividualcustomer.create_contract_select_formula_prepaid_tokenoptional()
        log.info("Selecting user.")
        mspindividualcustomer.create_contract_select_user_field().click()

        actions = ActionChains(self.driver)
        actions.send_keys(self.newestuser + Keys.ENTER)
        actions.perform()

        time.sleep(1)

        mspindividualcustomer.request_charging_card_checkbox()
        mspindividualcustomer.create_contract_create_button()
        time.sleep(1)
        message = mspindividualcustomer.message_contract_created().text
        assert message == "Mobility contract created"
        log.info("Contract has been successfully created.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_assign_user_token(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        log.info("Succesfully logged in.")
        log.info("Navigating towards msp customers page.")
        mspcustomerpage = homepage.menu_label_customers()
        log.info("Search for 'Automated Test Company'.")
        mspcustomerpage.search_by_name_field().send_keys(
            "Automated Test Company Main Flow" + Keys.ENTER
        )
        log.info("Opening customer.")
        mspindividualcustomer = mspcustomerpage.click_on_main_flow_account()
        log.info("Attempting to assign token to user.")
        mspindividualcustomer.add_first_token()
        available_token_string = mspindividualcustomer.next_available_token()
        time.sleep(1)
        available_token = mspindividualcustomer.get_available_token(
            available_token_string
        )
        mspindividualcustomer.select_token().send_keys(available_token)
        mspindividualcustomer.select_token_component_top_token()

        mspindividualcustomer.assign_token()
        time.sleep(1)
        message = mspindividualcustomer.message_token_assigned().text
        assert "Token assigned" in message
        log.info("Succesfully assigned token to user.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_add_token_to_whitelist(self, setup):
        log = self.get_logger()
        log.info("daan.swinnen+splitbilling4@optimile.eu")
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(
            "daan.swinnen+splitbilling4@optimile.eu"
        )
        loginpage.password_box().send_keys("hHsxpRXGX9NrN4aw6iCH")
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to whitelist page.")
        homepage.menu_label_chargingpoints()
        whitelistpage = homepage.menu_label_whitelist()
        log.info("Attempting to add tokens to whitelist.")
        whitelistpage.add_charging_tokens_button()
        whitelistpage.confirm_add_button()
        whitelistpage.save_add_button()
        time.sleep(1)
        message = whitelistpage.whitelist_saved_message().text
        assert message == "Whitelist entry saved."
        log.info("Succesfully added tokens to whitelist.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
