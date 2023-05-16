import time
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects
from selenium.webdriver.common.keys import Keys


@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param


class SubModuleOne(BaseClass):
    def test_mobility_policies_searchbar(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_searchbar().send_keys("OldPolicy")
        time.sleep(1)
        searchresult = self.driver.find_element(By.XPATH, "(//tr/td)[1]").text
        assert searchresult == "OldPolicy"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_filter(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_active()
        time.sleep(1)
        filterresults = self.driver.find_elements(By.XPATH, "//tbody/tr/td[5]/span")

        for filterresult in filterresults:
            assert (filterresult.text) == "Active"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_create_policy(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        newmobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_create_button()
        )

        timestamp = str(datetime.now())

        newmobilitypolicypage.new_policy_name_field().send_keys(timestamp)
        newmobilitypolicypage.new_policy_type_dropdown()
        newmobilitypolicypage.new_policy_contract_dropdown()
        newmobilitypolicypage.new_policy_budget_value().send_keys("150")
        newmobilitypolicypage.new_policy_datepicker()
        newmobilitypolicypage.new_policy_select_parking()
        newmobilitypolicypage.new_policy_select_all_available_users()
        newmobilitypolicypage.new_policy_move_users_to_linked()
        newmobilitypolicypage.new_policy_activate()
        time.sleep(1)
        newmobilitypolicypage.new_policy_accept_button()
        time.sleep(1)

        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='fade alert alert-success alert-dismissible show']",
                )
            )
        )
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        print(Message)

        assert Message == "Mobility policy successfully saved as active."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_create_draft(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        newmobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_create_button()
        )

        timestamp = str(datetime.now())

        newmobilitypolicypage.new_policy_name_field().send_keys(timestamp)
        newmobilitypolicypage.new_policy_type_dropdown()
        newmobilitypolicypage.new_policy_contract_dropdown()
        newmobilitypolicypage.new_policy_budget_value().send_keys("150")
        newmobilitypolicypage.new_policy_datepicker()
        newmobilitypolicypage.new_policy_select_parking()
        newmobilitypolicypage.new_policy_select_all_available_users()
        newmobilitypolicypage.new_policy_move_users_to_linked()

        newmobilitypolicypage.save_policy_as_draft_button()
        time.sleep(1)
        message = newmobilitypolicypage.message_saved_as_draft().text
        assert message == "Mobility policy successfully saved as draft."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_activate_draft(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_draft()
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        changemobilitypolicypage.change_mobility_policy_activate_draft()
        message = str(
            changemobilitypolicypage.change_mobility_policy_activation_message().text
        )
        assert "activated successfully" in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_draft_link_users(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_draft()
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "(//div/input[@class='form-check-input'])[12]"
        ).click()
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_unlink_all_users()
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.CONTROL + "a"
        )
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.DELETE
        )
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            "active test"
        )
        changemobilitypolicypage.change_mobility_policy_save()
        mobilitypoliciesmainpage.mobility_policies_searchbar().send_keys("active test")
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_select_all_available_users()
        changemobilitypolicypage.change_mobility_policy_link_all_users()
        changemobilitypolicypage.change_mobility_policy_save()
        time.sleep(1)

        mobilitypoliciesmainpage.mobility_policies_searchbar().send_keys("active test")
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.CONTROL + "a"
        )
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.DELETE
        )
        timestamp = str(datetime.now())
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            timestamp
        )
        changemobilitypolicypage.change_mobility_policy_activate_draft()
        message = str(
            changemobilitypolicypage.change_mobility_policy_activation_message().text
        )
        assert "activated successfully" in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_active_change_mob(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_active()
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_select_parking()
        changemobilitypolicypage.change_mobility_policy_select_car_sharing()
        changemobilitypolicypage.change_mobility_policy_select_bike_sharing()
        changemobilitypolicypage.change_mobility_policy_save()
        message = str(
            changemobilitypolicypage.change_mobility_policy_activation_message().text
        )
        assert "changed" in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
