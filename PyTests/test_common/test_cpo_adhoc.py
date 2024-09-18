import pytest
from selenium.webdriver.common.by import By
import time
import re
import math
import datetime
import platform
from selenium.webdriver.common.keys import Keys
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.AdhocWebApp import AdhocWebApp
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.ChargingSessionData import ChargingSessionData
from pageObjects.ChargingSimulator import ChargingSimulator
from pageObjects.IndividualChargingLocation import IndividualChargingLocation
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory

user_os = platform.system()


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


@pytest.fixture(params=ChargingSessionData.refresh_cp_data)
def refresh_cp_data(request):
    return request.param


class TestOne(BaseClass):
    def test_refresh_charging_point(self, setup, refresh_cp_data, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info(refresh_cp_data["OCPP ID"])

        chargingsimulator = ChargingSimulator(self.driver)
        log.info("Attempting to connect to simulator.")
        chargingsimulator.open_simulator_test()
        chargingsimulator.OCPP_ID_Field().clear()
        chargingsimulator.OCPP_ID_Field().send_keys(refresh_cp_data["OCPP ID"])
        chargingsimulator.mode_select_dropdown_simulator()
        chargingsimulator.connect_button()
        time.sleep(3)
        chargingsimulator.start_charging_session_button()
        time.sleep(20)
        chargingsimulator.stop_charging_session_button()
        time.sleep(3)


class TestTwo(BaseClass):
    def test_set_adhoc_markup(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        adhocplatformpage = homepage.menu_label_adhoc()
        paymentpagetab = adhocplatformpage.payment_page_tab()

        paymentpagetab.starting_price_margin().clear()
        paymentpagetab.starting_price_margin().send_keys("0")
        paymentpagetab.starting_price_fixed().clear()
        paymentpagetab.starting_price_fixed().send_keys("5")

        paymentpagetab.hourly_price_margin().clear()
        paymentpagetab.hourly_price_margin().send_keys("100")
        paymentpagetab.hourly_price_fixed().clear()
        paymentpagetab.hourly_price_fixed().send_keys("0")

        paymentpagetab.kwh_price_margin().clear()
        paymentpagetab.kwh_price_margin().send_keys("100")
        paymentpagetab.kwh_price_fixed().clear()
        paymentpagetab.kwh_price_fixed().send_keys("0")

        paymentpagetab.save_button()
        message = paymentpagetab.message_alert().text
        assert "Adhoc markup updated." in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_set_pricing_policy(self, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys(
            "Adhoc Remote Autotests" + Keys.ENTER
        )
        self.driver.find_element(
            By.XPATH, "//a[.='Adhoc Remote Autotests']"
        ).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        individualcharginglocation.pricing_tab()
        individualcharginglocation.edit_pricing_button()
        individualcharginglocation.choose_afir_policy()
        individualcharginglocation.set_pricing_policy()
        message = individualcharginglocation.generic_alert().text
        assert "Pricing policy set." in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_adhoc_payment_page_pricing(self):
        log = self.get_logger()
        adhocwebapp = AdhocWebApp(self.driver)
        adhocwebapp.get_adhoc_web_app()
        time.sleep(1)

        start_price_field = adhocwebapp.start_price().get_attribute(
            "innerText"
        )
        start_price_match = re.search(r"\d*\.\d+|\d+", start_price_field)

        if start_price_match:
            start_price = float(start_price_match.group())
            assert math.isclose(start_price, 6.16, rel_tol=1e-9)

        else:
            assert "Start price didn't contain a number" in start_price_field

        price_per_hour_field = adhocwebapp.price_per_hour().get_attribute(
            "innerText"
        )
        price_per_hour_match = re.search(r"\d*\.\d+|\d+", price_per_hour_field)

        if price_per_hour_match:
            price_per_hour = float(price_per_hour_match.group())
            assert math.isclose(price_per_hour, 0.0, rel_tol=1e-9)

        else:
            assert (
                "Price per hour didn't contain a number"
                in price_per_hour_field
            )
