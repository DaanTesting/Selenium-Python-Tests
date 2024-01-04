import pytest
from selenium.webdriver.common.by import By
import time
import datetime
import os
from selenium.webdriver.common.keys import Keys
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from pageObjects.ChargingSimulator import ChargingSimulator
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory


@pytest.fixture(params=LoginPageData.test_auto_main_data)
def login_data(request):
    return request.param


@pytest.fixture(params=ChargingSessionData.discount_session_data)
def discount_session_data(request):
    return request.param


class TestOne(BaseClass):
    def test_activate_discount(self, login_data):
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
        discountlistoverview = homepage.menu_label_discount_lists()
        discountlistoverview.enable_top_list()

        message = discountlistoverview.message_banner().text
        assert message == "Discount list enabled."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_add_token_to_discount(self, login_data, discount_session_data):
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
        discountlistoverview = homepage.menu_label_discount_lists()
        opendiscountlist = discountlistoverview.open_autotest_list()
        opendiscountlist.add_charging_token_button()
        opendiscountlist.add_external_token_button()
        opendiscountlist.external_token_uid_field().send_keys(
            discount_session_data["discount RFID"]
        )
        opendiscountlist.token_description_field().send_keys("Ongoing test")
        opendiscountlist.save_charging_token_to_discount_list_button()

        message = opendiscountlist.message_banner().text
        assert message == "Token added to discount list."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_execute_discounted_session(self, login_data, discount_session_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(discount_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            discount_session_data["OCPP ID"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            discount_session_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            discount_session_data["discount RFID"]
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
            discount_session_data["discount RFID"]
        )
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


class TestFour(BaseClass):
    def test_check_discount_value(self, login_data):
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
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Discounts" + Keys.ENTER)
        time.sleep(1)
        individualcharginglocation = (
            locationsmainpage.find_location_click_top_result()
        )
        individualcharginglocation.sessions_tab()
        time.sleep(1)
        sessionvalue_string = (
            individualcharginglocation.top_session_value().text
        )
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 54 <= sessionvalue_float <= 56, "Incorrect discount value."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_remove_token_from_discount(self, login_data):
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
        discountlistoverview = homepage.menu_label_discount_lists()
        opendiscountlist = discountlistoverview.open_autotest_list()
        opendiscountlist.remove_top_token_from_discount()

        message = opendiscountlist.message_banner().text
        assert message == "Token removed from discount list."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSix(BaseClass):
    def test_full_price_session(self, login_data, discount_session_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(discount_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            discount_session_data["OCPP ID"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            discount_session_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            discount_session_data["discount RFID"]
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
            discount_session_data["discount RFID"]
        )
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


class TestSeven(BaseClass):
    def test_check_full_price_value(self, login_data):
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
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Discounts" + Keys.ENTER)
        time.sleep(1)
        individualcharginglocation = (
            locationsmainpage.find_location_click_top_result()
        )
        individualcharginglocation.sessions_tab()
        time.sleep(1)
        sessionvalue_string = individualcharginglocation.top_session_value().text
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 109 <= sessionvalue_float <= 111, "Incorrect discount value."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEight(BaseClass):
    def test_disable_discount(self, login_data):
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
        discountlistoverview = homepage.menu_label_discount_lists()
        discountlistoverview.disable_top_list()

        message = discountlistoverview.message_banner().text
        assert message == "Discount list disabled."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestNine(BaseClass):
    def test_full_price_session(self, login_data, discount_session_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(discount_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            discount_session_data["OCPP ID"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            discount_session_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            discount_session_data["discount RFID"]
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
            discount_session_data["discount RFID"]
        )
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


class TestTen(BaseClass):
    def test_check_full_price_value(self, login_data):
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
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Discounts" + Keys.ENTER)
        time.sleep(1)
        individualcharginglocation = (
            locationsmainpage.find_location_click_top_result()
        )
        individualcharginglocation.sessions_tab()
        time.sleep(1)
        sessionvalue_string = (
            individualcharginglocation.top_session_value().text
        )
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 109 <= sessionvalue_float <= 111, "Incorrect discount value."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
