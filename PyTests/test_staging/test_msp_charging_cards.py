import random
import time
import pytest
import string

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.ChargingCardPage import ChargingCardPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param

@pytest.fixture(params=LoginPageData.test_fullflow_data)
def login_data2(request):
    return request.param

class TestOne(BaseClass):
    def test_create_user_contract_and_verify_token_request(self, setup, login_data, login_data2):
        log = self.get_logger()
        log.info("daan.swinnen+splitbilling4@optimile.eu")
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data2["account"])
        loginpage.password_box().send_keys(login_data2["password"])
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
        mspcustomerpage = homepage.menu_label_msp_customers()
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
        actions.send_keys(self.newestuser)
        actions.perform()
        time.sleep(1)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        time.sleep(3)

        mspindividualcustomer.request_charging_card_checkbox()

        time.sleep(5)

        mspindividualcustomer.create_contract_create_button()
        time.sleep(1)
        message = mspindividualcustomer.message_contract_created().text
        assert message == "Mobility contract created"
        log.info("Contract has been successfully created.")
        
        self.driver.get("https://test.optimile.eu/sp/customer/634/charging-cards/#/no-charging-card")

        chargingcardpage = ChargingCardPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='status-badge bg-light'])[1]")))
        chargingcardpage.search_field().send_keys(self.newestuser)
        chargingcardpage.search_field().send_keys(Keys.ENTER)

        time.sleep(5)
        status = chargingcardpage.top_status_badge().get_attribute("textContent")
        assert status == "Eligible"

class TestTwo(BaseClass):
    def test_request_token(self, login_data, login_data2):
        log = self.get_logger()
        log.info("daan.swinnen+splitbilling4@optimile.eu")
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data2["account"])
        loginpage.password_box().send_keys(login_data2["password"])
        homepage = loginpage.login_button()
        chargingcardpage = homepage.menu_label_charging_cards()
        chargingcardpage.no_charging_card_tab()
        time.sleep(2)
        top_name = chargingcardpage.get_top_name().text
        chargingcardpage.request_token_for_top_user()
        time.sleep(2)
        message = chargingcardpage.generic_message().text
        
        assert message == "Token requested successfully"

        chargingcardpage.processing_tab()
        time.sleep(1)
        chargingcardpage.search_field().send_keys(top_name + Keys.ENTER)
        time.sleep(1)
        processing_top_name = chargingcardpage.get_top_name().text

        assert top_name == processing_top_name

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


    

