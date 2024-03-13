import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.ChargingSimulator import ChargingSimulator
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=ChargingSessionData.roaming_session_data)
def roaming_session_data(request):
    return request.param


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_roaming_session(self, setup, roaming_session_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_session_data["OCPP ID"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_session_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_session_data["token RFID"]
        )
        chargingsimulator.meter_start_field().send_keys("1")
        log.info("Attempting to start transaction.")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        log.info("Getting transaction ID.")
        transaction_id = chargingsimulator.get_transaction_id()
        print(transaction_id)
        log.info("Requesting 'stop transaction'-screen.")
        chargingsimulator.request_dropdown_stop()
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field_stop().send_keys(
            roaming_session_data["token RFID"]
        )
        log.info("Simulating meter end value.")
        chargingsimulator.meter_stop_field().send_keys("10001")
        log.info("Sending transaction ID.")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        log.info("Sending timestamp.")
        chargingsimulator.timestamp_add_hour()
        log.info("Selecting transaction stop reason.")
        chargingsimulator.reason_dropdown_evdisconnected()
        log.info("Stopping transaction.")
        chargingsimulator.stop_transaction_button()
        time.sleep(1)

    def test_roaming_session__platform_verification(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        self.driver.get("https://test.optimile.eu/")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to msp customers page.")
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        log.info("Searching for 'Autotesting Roaming'.")
        mspcustomerpage.search_by_name_field().send_keys(
            "Autotesting Roaming" + "\n"
        )
        time.sleep(1)
        log.info("Opening customer.")
        mspindividualcustomer = mspcustomerpage.click_on_top_result_customer()
        log.info("Activity tab.")
        mspindividualcustomer.activity_tab()
        statuslatestsession = self.driver.find_element(
            By.XPATH, "//tr[1]/td[6]"
        ).text
        assert statuslatestsession == "Normal"
        log.info(
            "Succesfully verified charging session registered as 'normal'."
        )
        sessionvalue_string = mspindividualcustomer.top_session_value().text
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 144 <= sessionvalue_float <= 146, "Incorrect value."

        log.info("Successfully confirmed session value.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_whitelist_session(self, setup, roaming_session_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_session_data["OCPP ID"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_session_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_session_data["whitelist RFID"]
        )
        chargingsimulator.meter_start_field().send_keys("1")
        log.info("Attempting to start transaction.")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        log.info("Getting transaction ID.")
        transaction_id = chargingsimulator.get_transaction_id()
        print(transaction_id)
        log.info("Requesting 'stop transaction'-screen.")
        chargingsimulator.request_dropdown_stop()
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field_stop().send_keys(
            roaming_session_data["whitelist RFID"]
        )
        log.info("Simulating meter end value.")
        chargingsimulator.meter_stop_field().send_keys("10001")
        log.info("Sending transaction ID.")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        log.info("Sending timestamp.")
        chargingsimulator.timestamp_add_hour()
        log.info("Selecting transaction stop reason.")
        chargingsimulator.reason_dropdown_evdisconnected()
        log.info("Stopping transaction.")
        chargingsimulator.stop_transaction_button()
        time.sleep(1)

    def test_whitelist_session__platform_verification(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        self.driver.get("https://test.optimile.eu/")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to cpo customers page.")
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        log.info("Searching for 'Carrefour'.")
        cpocustomerpage.search_by_name_field().send_keys("Carrefour" + "\n")
        log.info("Opening user.")
        cpoindividualcustomer = cpocustomerpage.click_on_top_result_carrefour()
        log.info("Opening sessions-tab.")
        cpoindividualcustomer.sessions_tab()
        time.sleep(2)
        statuslatestsession = self.driver.find_element(
            By.XPATH, "//tr[1]/td[10]/span"
        ).text
        assert statuslatestsession == "Whitelist"

        sessionvalue_string = cpoindividualcustomer.top_session_value().text
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert sessionvalue_float == 0.00

        log.info("Succesfully verified session status as 'whitelist'.")
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_splitbilling_session(
        self, setup, roaming_session_data, login_data
    ):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_session_data["splitbilling OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_session_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_session_data["splitbilling RFID"]
        )
        chargingsimulator.meter_start_field().send_keys("1")
        log.info("Attempting to start transaction.")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        log.info("Getting transaction ID.")
        transaction_id = chargingsimulator.get_transaction_id()
        print(transaction_id)
        log.info("Requesting 'stop transaction'-screen.")
        chargingsimulator.request_dropdown_stop()
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field_stop().send_keys(
            roaming_session_data["splitbilling RFID"]
        )
        log.info("Simulating meter end value.")
        chargingsimulator.meter_stop_field().send_keys("10001")
        log.info("Sending transaction ID.")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        log.info("Sending timestamp.")
        chargingsimulator.timestamp_add_hour()
        log.info("Selecting transaction stop reason.")
        chargingsimulator.reason_dropdown_evdisconnected()
        log.info("Stopping transaction.")
        chargingsimulator.stop_transaction_button()
        time.sleep(1)

    def test_splitbilling_session__platform_verification(
        self, setup, login_data
    ):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        self.driver.get("https://test.optimile.eu/")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to CPO customers screen.")
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        log.info("Searching for 'Autotest Splitbilling'.")
        cpocustomerpage.search_by_name_field().send_keys(
            "Autotest Splitbilling" + "\n"
        )
        log.info("Opening user.")
        cpoindividualcustomer = cpocustomerpage.click_on_top_result_customer()
        log.info("Opening sessions-tab")
        cpoindividualcustomer.sessions_tab()
        time.sleep(2)
        statuslatestsession = self.driver.find_element(
            By.XPATH, "//tr[1]/td[10]/span"
        ).get_attribute("title")
        assert (
            statuslatestsession
            == "Session is remunerated under split billing."
        )

        sessionvalue_string = cpoindividualcustomer.top_session_value().text
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert sessionvalue_float == 10.00

        log.info("Succesfully verified the session as 'Split Billing'.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
