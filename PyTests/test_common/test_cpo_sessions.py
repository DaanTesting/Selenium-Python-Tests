import time
import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.ChargingSimulator import ChargingSimulator


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
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(roaming_session_data["OCPP ID"])
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        time.sleep(1)
        chargingsimulator.request_dropdown_start()
        chargingsimulator.connector_id_field().send_keys(
            roaming_session_data["connectorId"]
        )
        chargingsimulator.id_tag_field().send_keys(roaming_session_data["token RFID"])
        chargingsimulator.meter_start_field().send_keys("1")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        transaction_id = chargingsimulator.get_transaction_id()
        print(transaction_id)
        chargingsimulator.request_dropdown_stop()
        chargingsimulator.id_tag_field_stop().send_keys(
            roaming_session_data["token RFID"]
        )
        chargingsimulator.meter_stop_field().send_keys("10001")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        chargingsimulator.timestamp_add_hour()
        chargingsimulator.reason_dropdown_evdisconnected()
        chargingsimulator.stop_transaction_button()
        time.sleep(2)

    def test_roaming_session__platform_verification(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        self.driver.get("https://test.optimile.eu/")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_mobility()
        mspcustomerpage = homepage.menu_label_msp_customers()
        mspcustomerpage.search_by_name_field().send_keys("Autotesting Roaming" + "\n")
        time.sleep(1)
        mspindividualcustomer = mspcustomerpage.click_on_top_result_customer()
        mspindividualcustomer.activity_tab()
        statuslatestsession = self.driver.find_element(By.XPATH, "//tr[1]/td[6]").text
        assert statuslatestsession == "Normal"
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_whitelist_session(self, setup, roaming_session_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(roaming_session_data["OCPP ID"])
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        time.sleep(1)
        chargingsimulator.request_dropdown_start()
        chargingsimulator.connector_id_field().send_keys(
            roaming_session_data["connectorId"]
        )
        chargingsimulator.id_tag_field().send_keys(
            roaming_session_data["whitelist RFID"]
        )
        chargingsimulator.meter_start_field().send_keys("1")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        transaction_id = chargingsimulator.get_transaction_id()
        print(transaction_id)
        chargingsimulator.request_dropdown_stop()
        chargingsimulator.id_tag_field_stop().send_keys(
            roaming_session_data["whitelist RFID"]
        )
        chargingsimulator.meter_stop_field().send_keys("10001")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        chargingsimulator.timestamp_add_hour()
        chargingsimulator.reason_dropdown_evdisconnected()
        chargingsimulator.stop_transaction_button()

    def test_whitelist_session__platform_verification(self, setup, login_data): 
        log = self.get_logger()
        log.info(login_data["account"])
        self.driver.get("https://test.optimile.eu/")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        cpocustomerpage.search_by_name_field().send_keys("Carrefour" + "\n")
        cpoindividualcustomer = cpocustomerpage.click_on_top_result_carrefour()
        cpoindividualcustomer.sessions_tab()
        statuslatestsession = self.driver.find_element(
            By.XPATH, "//tr[1]/td[10]/span"
        ).text
        assert statuslatestsession == "Whitelist"
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_splitbilling_session(self, setup, roaming_session_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_session_data["splitbilling OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        time.sleep(1)
        chargingsimulator.request_dropdown_start()
        chargingsimulator.connector_id_field().send_keys(
            roaming_session_data["connectorId"]
        )
        chargingsimulator.id_tag_field().send_keys(
            roaming_session_data["splitbilling RFID"]
        )
        chargingsimulator.meter_start_field().send_keys("1")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        transaction_id = chargingsimulator.get_transaction_id()
        print(transaction_id)
        chargingsimulator.request_dropdown_stop()
        chargingsimulator.id_tag_field_stop().send_keys(
            roaming_session_data["splitbilling RFID"]
        )
        chargingsimulator.meter_stop_field().send_keys("10001")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        chargingsimulator.timestamp_add_hour()
        chargingsimulator.reason_dropdown_evdisconnected()
        chargingsimulator.stop_transaction_button()
        time.sleep(2)

    def test_splitbilling_session__platform_verification(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        self.driver.get("https://test.optimile.eu/")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        cpocustomerpage.search_by_name_field().send_keys("Autotest Splitbilling" + "\n")
        cpoindividualcustomer = cpocustomerpage.click_on_top_result_customer()
        cpoindividualcustomer.sessions_tab()
        statuslatestsession = self.driver.find_element(
            By.XPATH, "//tr[1]/td[10]/span"
        ).get_attribute("title")
        assert statuslatestsession == "Session is remunerated under split billing."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
