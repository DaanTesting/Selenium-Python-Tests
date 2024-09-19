import time
import pytest
from pageObjects.ChargingSimulator import ChargingSimulator
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test2_login_data)
def login_data(request):
    return request.param

@pytest.fixture(params=ChargingSessionData.roaming_test2_data)
def roaming_test2_data(request):
    return request.param

class TestOne(BaseClass):
    def test_splitbilling_sessions(self, setup, roaming_test2_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_test2_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator_test2()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_test2_data["splitbilling OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_test2_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_test2_data["splitbilling RFID"]
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
            roaming_test2_data["splitbilling RFID"]
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

        chargingsimulator.open_simulator_test2()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_test2_data["splitbilling OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_test2_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_test2_data["splitbilling RFID"]
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
            roaming_test2_data["splitbilling RFID"]
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

        chargingsimulator.open_simulator_test2()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_test2_data["splitbilling OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_test2_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_test2_data["splitbilling RFID"]
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
            roaming_test2_data["splitbilling RFID"]
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

    def test_roaming_session(self, setup, roaming_test2_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(roaming_test2_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator_test2()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_test2_data["accounting OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_test2_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_test2_data["token RFID"]
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
            roaming_test2_data["token RFID"]
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

        chargingsimulator.open_simulator_test2()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_test2_data["accounting OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_test2_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_test2_data["token RFID"]
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
            roaming_test2_data["token RFID"]
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

        chargingsimulator.open_simulator_test2()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(
            roaming_test2_data["accounting OCPP"]
        )
        chargingsimulator.mode_select_dropdown()
        chargingsimulator.connect_button()
        log.info("Connected to simulator.")
        time.sleep(1)
        log.info("Requesting 'start transaction'-screen.")
        chargingsimulator.request_dropdown_start()
        log.info("Entering connectorID.")
        chargingsimulator.connector_id_field().send_keys(
            roaming_test2_data["connectorId"]
        )
        log.info("Sending token RFID.")
        chargingsimulator.id_tag_field().send_keys(
            roaming_test2_data["token RFID"]
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
            roaming_test2_data["token RFID"]
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

