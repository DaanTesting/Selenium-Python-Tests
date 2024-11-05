import pytest
from selenium.webdriver.common.by import By
import time
import datetime
import os
from selenium.webdriver.common.keys import Keys
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.GeneralData import GeneralData
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from pageObjects.ChargingSimulator import ChargingSimulator
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory


@pytest.fixture(params=LoginPageData.staging_customer_login_data)
def login_data(request):
    return request.param


@pytest.fixture(params=ChargingSessionData.discount_session_data)
def discount_session_data(request):
    return request.param

@pytest.fixture(params=GeneralData.test_general_data)
def general_data(request):
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
        log.info("Navigating to discount list page.")
        homepage.menu_label_chargingpoints()
        discountlistoverview = homepage.menu_label_discount_lists()
        log.info("Enabling top discount list.")
        discountlistoverview.enable_top_list()

        message = discountlistoverview.message_banner().text
        assert message == "Discount list enabled."
        log.info("Successfully enabled discount list.")

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
        log.info("Navigating to discount list page.")
        homepage.menu_label_chargingpoints()
        discountlistoverview = homepage.menu_label_discount_lists()
        log.info("Opening test discount list.")
        opendiscountlist = discountlistoverview.open_autotest_list()
        log.info("Adding charging token to list.")
        opendiscountlist.add_charging_token_button()
        log.info("Adding external token to list.")
        opendiscountlist.add_external_token_button()
        opendiscountlist.external_token_uid_field().send_keys(
            discount_session_data["discount RFID"]
        )
        log.info("Updating token description.")
        opendiscountlist.token_description_field().send_keys("Ongoing test")
        log.info("Saving token to discount list.")
        opendiscountlist.save_charging_token_to_discount_list_button()

        message = opendiscountlist.message_banner().text
        assert message == "Token added to discount list."
        log.info("Successfully added token to discount list.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_add_charging_points(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to discount list page.")
        homepage.menu_label_chargingpoints()
        discountlistoverview = homepage.menu_label_discount_lists()
        log.info("Opening top discount list.")
        opendiscountlist = discountlistoverview.open_top_list()
        log.info("Navigating to charging points tab.")
        opendiscountlist.charging_points_tab()
        log.info("Editing charging points.")
        opendiscountlist.edit_charging_points_button()
        log.info("Linking all charging points to discount.")
        opendiscountlist.link_all_charging_points_to_discount()
        opendiscountlist.charging_point_save_button()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Charging points edited." in alerttext

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_execute_discounted_session(self, login_data, discount_session_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(discount_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        log.info("Attempting to execute discounted charging session.")
        chargingsimulator.open_simulator_staging()
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


class TestFive(BaseClass):
    def test_check_discount_value(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Discounts' location.")
        time.sleep(1)
        log.info("Opening location 'Autotests Discounts'.")
        individualcharginglocation = (
            locationsmainpage.find_location_customer_click_main_location()
        )
        log.info("Opening sessions tab.")
        individualcharginglocation.sessions_tab()
        log.info("Attempting to verify correct discount was applied.")
        time.sleep(1)
        sessionvalue_string = (
            individualcharginglocation.top_session_value().text
        )
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 27 <= sessionvalue_float <= 28, "Incorrect discount value."
        log.info("Successfully verified discount price.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSix(BaseClass):
    def test_remove_token_from_discount(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to discount lists page.")
        homepage.menu_label_chargingpoints()
        discountlistoverview = homepage.menu_label_discount_lists()
        log.info("Opening autotest list.")
        opendiscountlist = discountlistoverview.open_autotest_list()
        log.info("Attempting to remove token from discount list.")
        opendiscountlist.remove_top_token_from_discount()

        message = opendiscountlist.message_banner().text
        assert message == "Token removed from discount list."
        log.info("Successfully removed token from discount list.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSeven(BaseClass):
    def test_full_price_session(self, login_data, discount_session_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(discount_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        log.info("Simulating full price charging session.(Token removed from discount.)")
        chargingsimulator.open_simulator_staging()
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


class TestEight(BaseClass):
    def test_check_full_price_value(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Autotest Discounts' location.")
        log.info("Opening 'Autotest Discounts' location.")
        time.sleep(1)
        individualcharginglocation = (
            locationsmainpage.find_location_customer_click_main_location()
        )
        log.info("Navigating to sessions tab.")
        individualcharginglocation.sessions_tab()
        time.sleep(1)
        log.info("Attempting to verify correct session price.")
        sessionvalue_string = individualcharginglocation.top_session_value().text
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 109 <= sessionvalue_float <= 111, "Incorrect discount value."
        log.info("Successfully verified session was not discounted.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestNine(BaseClass):
    def test_disable_discount(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to discount list page.")
        homepage.menu_label_chargingpoints()
        discountlistoverview = homepage.menu_label_discount_lists()
        log.info("Disabling top discount list.")
        discountlistoverview.disable_top_list()

        message = discountlistoverview.message_banner().text
        assert message == "Discount list disabled."
        log.info("Successfully disabled top discount list.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTen(BaseClass):
    def test_full_price_session(self, login_data, discount_session_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(discount_session_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        log.info("Simulating a full price charging session.(Discount disabled.)")
        chargingsimulator.open_simulator_staging()
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


class TestEleven(BaseClass):
    def test_check_full_price_value(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Autotest Discounts' location.")
        time.sleep(1)
        log.info("Opening top location.")
        individualcharginglocation = (
            locationsmainpage.find_location_customer_click_main_location()
        )
        log.info("Navigating to sessions tab.")
        individualcharginglocation.sessions_tab()
        time.sleep(1)
        log.info("Attempting to verify session cost.")
        sessionvalue_string = (
            individualcharginglocation.top_session_value().text
        )
        sessionvalue_string = sessionvalue_string[1:]
        sessionvalue_float = float(sessionvalue_string)

        assert 109 <= sessionvalue_float <= 111, "Incorrect discount value."
        log.info("Successfully verified full price charging session.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestTwelve(BaseClass):
    def test_remove_charging_points(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to discount list page.")
        homepage.menu_label_chargingpoints()
        discountlistoverview = homepage.menu_label_discount_lists()
        log.info("Opening top discount list.")
        opendiscountlist = discountlistoverview.open_top_list()
        log.info("Navigating to charging points tab.")
        opendiscountlist.charging_points_tab()
        log.info("Editing charging points.")
        opendiscountlist.edit_charging_points_button()
        opendiscountlist.unlink_all_charging_points_from_discount()
        opendiscountlist.charging_point_save_button()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Charging points edited." in alerttext
        log.info("Successfully verified all charging point have been removed.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
