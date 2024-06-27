import pytest
from selenium.webdriver.common.by import By
import time
import datetime
import os
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass
from utilities.Settings import cache_directory


@pytest.fixture(params=LoginPageData.test_local_customer_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_discount_list_create(self, setup, login_data):
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
        log.info("Attempting to create a new discount list.")
        creatediscountlist = discountlistoverview.new_list_button()
        creatediscountlist.name_field().send_keys("Automatic Test Discount")
        creatediscountlist.discount_percentage_field().send_keys("75")
        creatediscountlist.selection_charging_points_button()
        creatediscountlist.create_button()

        creatediscountlist = discountlistoverview.new_list_button()
        creatediscountlist.name_field().send_keys("second_discount")
        creatediscountlist.discount_percentage_field().send_keys("75")
        creatediscountlist.selection_charging_points_button()
        creatediscountlist.create_button()

        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Discount list saved" in alerttext
        log.info("Successfully created new discount list.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_discount_list_disable_enable(self, setup, login_data):
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
        log.info("Disabling top discount list.")
        discountlistoverview.disable_top_list()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Discount list disabled" in alerttext
        log.info("Successfully verified top list has been disabled.")
        time.sleep(2)
        log.info("Enabling top discount list.")
        discountlistoverview.enable_top_list()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Discount list enabled" in alerttext
        log.info("Successfully verified top list has been enabled.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_discount_list_edit(self, setup, login_data):
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
        log.info("Editing second discount list.")
        creatediscountlist = discountlistoverview.edit_second_list()
        creatediscountlist.name_field().clear()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        creatediscountlist.name_field().send_keys(timestamp)
        creatediscountlist.discount_percentage_field().clear()
        creatediscountlist.discount_percentage_field().send_keys("50")
        creatediscountlist.update_button()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Discount list saved" in alerttext
        log.info("Successfully verified discount list has been edited.")
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_discount_list_add_edit_delete_token(self, setup, login_data):
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
        log.info("Adding a token to discount list.")
        opendiscountlist.add_charging_token_button()
        opendiscountlist.add_token_button()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        opendiscountlist.token_description_field().send_keys(timestamp)
        opendiscountlist.save_charging_token_to_discount_list_button()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Token added to discount list." in alerttext
        log.info("Successfully verified token has been added to discount list.")
        log.info("Editing top token.")
        opendiscountlist.edit_top_token()
        opendiscountlist.token_description_field().clear
        opendiscountlist.token_description_field().send_keys(timestamp)
        opendiscountlist.update_token_in_discount_list_button()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Token updated" in alerttext
        log.info("Successfully verified that token has been updated.")
        log.info("Removing top token.")
        opendiscountlist.delete_top_token()
        alerttext = self.driver.find_element(
            By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"
        ).text
        assert "Token removed" in alerttext
        log.info("Successfully verified top token has been deleted.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_export_tokens(self, setup, login_data):
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
        log.info("Opening top discount list.")
        opendiscountlist = discountlistoverview.open_top_list()
        log.info("Exporting tokens list.")
        opendiscountlist.export_tokens_button()

        download_directory = cache_directory
        today = datetime.datetime.now()
        timestamp = today.strftime('%Y-%m-%d')
        downloaded_file_name = "tokens_assigned_to_first_discount-" + timestamp + ".csv"
        downloaded_file_path = os.path.join(
            download_directory, downloaded_file_name
        )

        time.sleep(3)
        os.path.exists(downloaded_file_path)
        os.remove(downloaded_file_path)

        log.info("Successfully verified token list has been downloaded.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSix(BaseClass):
    def test_add_remove_charging_points(self, setup, login_data):
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
        log.info("Successfully verified charging points have been edited.")
        log.info("Removing all charging points from discount.")
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
