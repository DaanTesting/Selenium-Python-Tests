import pytest
import platform
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import math
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.ChargingSimulator import ChargingSimulator
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory
from decimal import Decimal
user_os = platform.system()

@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param

@pytest.fixture(params=ChargingSessionData.credit_check_sessions)
def session_data(request):
    return request.param


class TestOne(BaseClass):
    def test_credit_free_charging_with_reserved_credit(
        self, setup, login_data, session_data,
    ):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        log.info("Creating second browser tab.")
        loginpage = LoginPage(self.driver)

        if user_os == "Darwin":
            loginpage.username_box().send_keys(Keys.COMMAND + "t")

        else:
            loginpage.username_box().send_keys(Keys.CONTROL + "t")

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        loginpage.login_button()
        log.info("Navigating to test-credit page.")
        self.driver.get(
            "https://staging.optimile-dev.eu/sp/admin/customers/2/users/55/credit/add/#/credit"
        )
        time.sleep(1)
        log.info("Saving starting credit.")
        start_credit = self.driver.find_element(
            By.XPATH, "//input[@id='id_credit']"
        ).get_attribute("value")

        start_credit_float = float(start_credit)


        original_window = self.driver.current_window_handle
        log.info("Swapping tab and navigating to charging simulator.")
        self.driver.switch_to.new_window("tab")
        self.driver.get("https://staging.optimile-dev.eu/sim/")
        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator_staging()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(session_data["OCPP ID FREE"])
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(session_data["connectorId"])
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(session_data["FREE RFID"])
        chargingsimulator.meter_start_field().send_keys("0")
        log.info("Attempting to start transaction.")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        log.info("Swapping to original window.")
        for window_handle in self.driver.window_handles:
            if window_handle == original_window:
                self.driver.switch_to.window(window_handle)
                break

        time.sleep(2)
        self.driver.get(
            "https://staging.optimile-dev.eu/sp/admin/customers/2/users/55/credit/add/#/credit"
        )
        time.sleep(2)
        log.info("Attempting to verify the correct amount of credit is being reserved.")
        reserved_credit = "50"
        credit_during_charging = self.driver.find_element(
            By.XPATH, "//input[@id='id_credit']"
        ).get_attribute("value")
        credit_during_charging_float = float(credit_during_charging)
        theoretical_credit_during_charging = Decimal(start_credit_float) - Decimal(reserved_credit)

        assert math.isclose(
            credit_during_charging_float,
            theoretical_credit_during_charging,
            rel_tol=0.2,
        )
        log.info("Verified correct amount of credit has been reserved.")
        log.info("Swapping back to simulator tab.")
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        
        log.info("Getting transaction ID.")
        transaction_id = chargingsimulator.get_transaction_id()
        log.info("Requesting 'stop transaction'-screen.")
        chargingsimulator.request_dropdown_stop()
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field_stop().send_keys(session_data["FREE RFID"])
        log.info("Simulating meter end value.")
        chargingsimulator.meter_stop_field().send_keys("10000")
        log.info("Sending transaction ID.")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        log.info("Sending timestamp.")
        chargingsimulator.timestamp_add_hour()
        log.info("Selecting transaction stop reason.")
        chargingsimulator.reason_dropdown_evdisconnected()
        log.info("Stopping transaction.")
        chargingsimulator.stop_transaction_button()
        time.sleep(1)
        log.info("Swapping back to original window.")
        for window_handle in self.driver.window_handles:
            if window_handle == original_window:
                self.driver.switch_to.window(window_handle)
                break

        time.sleep(2)
        log.info("Refreshing browser.")
        self.driver.get(
            "https://staging.optimile-dev.eu/sp/admin/customers/2/users/55/credit/add/#/credit"
        )
        time.sleep(2)
        log.info("Attempting to verify post-session credit is correct.")

        credit_after_charging = self.driver.find_element(
            By.XPATH, "//input[@id='id_credit']"
        ).get_attribute("value")
        credit_after_charging_float = float(credit_after_charging)

        assert credit_after_charging_float == start_credit_float
        log.info("Successfully verified credit was correct before, during, and after whitelist charging session.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_credit_paid_charging_with_reserved_credit(
        self, setup, login_data
    ):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        log.info("Opening second browser tab.")

        if user_os == "Darwin":
            loginpage.username_box().send_keys(Keys.COMMAND + "t")

        else:
            loginpage.username_box().send_keys(Keys.CONTROL + "t")

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        loginpage.login_button()
        log.info("Navigating to account credit page.")
        self.driver.get(
            "https://test.optimile.eu/sp/admin/customers/639/users/1005/credit/#/credit"
        )
        time.sleep(1)
        log.info("Saving starting credit.")
        start_credit = self.driver.find_element(
            By.XPATH, "//div/table/tbody/tr[contains(.,'Total')]"
        ).text
        start_credit_float = float(
            start_credit.replace("Total", "").replace("€", "").replace(",", "")
        )

        original_window = self.driver.current_window_handle

        log.info("Swapping to second browser tab and navigating to charging simulator.")

        self.driver.switch_to.new_window("tab")
        self.driver.get("https://test.optimile.eu/sim/")
        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator_test()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys("TestDevicePaidCharging")
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys("1")
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys("044FACDAFB6C81")
        chargingsimulator.meter_start_field().send_keys("0")
        log.info("Attempting to start transaction.")
        chargingsimulator.start_transaction_button()
        time.sleep(10)
        log.info("Swapping back to original tab.")
        for window_handle in self.driver.window_handles:
            if window_handle == original_window:
                self.driver.switch_to.window(window_handle)
                break

        time.sleep(2)
        log.info("Refreshing account credit page.")
        self.driver.get(
            "https://test.optimile.eu/sp/admin/customers/639/users/1005/credit/#/credit"
        )
        time.sleep(2)
        log.info("Verifying correct amount of credit gets reserved.")
        reserved_credit = "50"
        credit_during_charging = self.driver.find_element(
            By.XPATH, "//div/table/tbody/tr[contains(.,'Total')]"
        ).text
        credit_during_charging_float = float(
            credit_during_charging.replace("Total", "")
            .replace("€", "")
            .replace(",", "")
        )
        theoretical_credit_during_charging = Decimal(
            start_credit_float
        ) - Decimal(reserved_credit)

        assert math.isclose(
            credit_during_charging_float,
            theoretical_credit_during_charging,
            rel_tol=0.2,
        )
        log.info("Successfully verified correct credit reservation.")
        log.info("Swapping back to simulator tab.")
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        log.info("Getting transaction ID.")
        transaction_id = chargingsimulator.get_transaction_id()
        log.info("Requesting 'stop transaction'-screen.")
        chargingsimulator.request_dropdown_stop()
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field_stop().send_keys("044FACDAFB6C81")
        log.info("Simulating meter end value.")
        chargingsimulator.meter_stop_field().send_keys("10000")
        log.info("Sending transaction ID.")
        chargingsimulator.transaction_id_field().send_keys(transaction_id)
        log.info("Sending timestamp.")
        chargingsimulator.timestamp_add_hour()
        log.info("Selecting transaction stop reason.")
        chargingsimulator.reason_dropdown_evdisconnected()
        log.info("Stopping transaction.")
        chargingsimulator.stop_transaction_button()
        time.sleep(1)
        log.info("Swapping back to original tab.")
        for window_handle in self.driver.window_handles:
            if window_handle == original_window:
                self.driver.switch_to.window(window_handle)
                break

        time.sleep(2)
        log.info("Refreshing account credit page.")
        self.driver.get(
            "https://test.optimile.eu/sp/admin/customers/639/users/1005/credit/#/credit"
        )
        time.sleep(2)
        log.info("Verifying the correct amount of credit was deducted.")
        charging_cost = 133.10
        credit_after_charging = self.driver.find_element(
            By.XPATH, "//div/table/tbody/tr[contains(.,'Total')]"
        ).text
        credit_after_charging_float = float(
            credit_after_charging.replace("Total", "")
            .replace("€", "")
            .replace(",", "")
        )
        theoretical_credit_after_charging = Decimal(
            start_credit_float
        ) - Decimal(charging_cost)

        assert math.isclose(
            credit_after_charging_float,
            theoretical_credit_after_charging,
            rel_tol=0.2,
        )
        log.info("Successfully verified correct credit before, during, and after paid charging session.")
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()