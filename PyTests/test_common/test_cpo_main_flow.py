import time
import pytest
import random
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_create_user(self, setup):
        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys("daan.swinnen+splitbilling4@optimile.eu")
        loginpage.password_box().send_keys("hHsxpRXGX9NrN4aw6iCH")
        homepage = loginpage.login_button()
        manageuserspage = homepage.menu_label_administration_users()
        manageuserspage.create_user_button()

        random_num = str(random.randint(1000, 9999))
        manageuserspage.create_user_email_field().send_keys(
            "daan.swinnen+" + random_num + "@optimile.eu"
        )
        manageuserspage.checkbox_account_admin()
        manageuserspage.create_user_save_button()
        time.sleep(1)
        message = manageuserspage.user_created_message().text
        assert "User created:" in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestTwo(BaseClass):
    def test_create_user_contract(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        mspcustomerpage.search_by_name_field().send_keys("Automated Test Company")
        mspindividualcustomer = mspcustomerpage.click_on_main_flow_account()
        mspindividualcustomer.mail_tab()
        newestuser = mspindividualcustomer.select_top_emailadress().text
        mspindividualcustomer.contracts_tab()
        mspindividualcustomer.create_contract_button()
        mspindividualcustomer.create_contract_select_formula_freepostpaid()
        mspindividualcustomer.create_contract_select_user().select_by_visible_text(
            newestuser
        )
        mspindividualcustomer.create_contract_create_button()
        time.sleep(1)
        message = mspindividualcustomer.message_contract_created().text
        assert message == "Mobility contract created"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_assign_user_token(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        mspcustomerpage.search_by_name_field().send_keys("Automated Test Company")
        mspindividualcustomer = mspcustomerpage.click_on_main_flow_account()
        mspindividualcustomer.add_first_token()
        mspindividualcustomer.assign_token()
        time.sleep(1)
        message = mspindividualcustomer.message_token_assigned().text
        assert "Token assigned" in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_add_token_to_whitelist(self):
        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys("daan.swinnen+splitbilling4@optimile.eu")
        loginpage.password_box().send_keys("hHsxpRXGX9NrN4aw6iCH")
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        whitelistpage = homepage.menu_label_whitelist()
        whitelistpage.add_charging_tokens_button()
        whitelistpage.confirm_add_button()
        whitelistpage.save_add_button()
        time.sleep(1)
        message = whitelistpage.whitelist_saved_message().text
        assert message == "Whitelist entry saved."
