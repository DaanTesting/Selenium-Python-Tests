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

class TestThree(BaseClass):
    def test_request_token2(self, login_data, login_data2):

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        mspcustomerpage.search_by_name_field().send_keys(
            "Automated Test Company Main Flow" + Keys.ENTER
        )
        mspindividualcustomer = mspcustomerpage.click_on_main_flow_account()
        mspindividualcustomer.tokens_tab()

        token_requests = self.driver.find_elements(By.XPATH, "//tbody/tr")
        for token_request in token_requests:
            print(self.driver.find_element(By.XPATH, "//td[3]").text)
        