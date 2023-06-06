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


class TestSubModuleOne(BaseClass):
    def test_mobility_policies_searchbar(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")

        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_searchbar().send_keys("OldPolicy")
        log.info("Searching for mobility policy named 'OldPolicy'.")
        time.sleep(1)
        searchresult = self.driver.find_element(By.XPATH, "(//tr/td)[1]").text
        assert searchresult == "OldPolicy"
        log.info("Succesfully verified search result.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_filter(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_active()
        log.info("Filtering 'active' mobility policies.")
        time.sleep(1)
        filterresults = self.driver.find_elements(By.XPATH, "//tbody/tr/td[5]/span")

        for filterresult in filterresults:
            assert (filterresult.text) == "Active"
        
        log.info("Succesfully verified filtering occurred correctly.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_create_policy(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        log.info("Attempting to create new mobility policy.")
        newmobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_create_button()
        )

        timestamp = str(datetime.now())

        newmobilitypolicypage.new_policy_name_field().send_keys(timestamp)
        log.info("Set policy name as 'timestamp'.")
        newmobilitypolicypage.new_policy_type_dropdown()
        log.info("Selected mobility policy type as 'professional'.")
        newmobilitypolicypage.new_policy_contract_dropdown()
        log.info("Selected second contract.")
        newmobilitypolicypage.new_policy_budget_value().send_keys("150")
        log.info("Set policy budget to '150'.")
        
        newmobilitypolicypage.new_policy_datepicker()
        log.info("Set start date on 'today'.")
        log.info("Set end date as undefined.")
        
        newmobilitypolicypage.new_policy_select_parking()
        log.info("Selected mobility option 'parking'.")

        newmobilitypolicypage.new_policy_select_all_available_users().click()
        newmobilitypolicypage.new_policy_move_users_to_linked()
        log.info("Linked all available users.")
        
        newmobilitypolicypage.new_policy_activate()
        time.sleep(1)
        newmobilitypolicypage.new_policy_accept_button()
        time.sleep(1)
        log.info("Activated mobility policy.")

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
        log.info("Succesfully verified new mobility policy is now active.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_create_draft(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        log.info("Attempting to create new mobility policy.")
        newmobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_create_button()
        )

        timestamp = str(datetime.now())

        newmobilitypolicypage.new_policy_name_field().send_keys(timestamp)
        log.info("Set policy name as 'timestamp'.")
        newmobilitypolicypage.new_policy_type_dropdown()
        log.info("Selected mobility policy type as 'professional'.")
        newmobilitypolicypage.new_policy_contract_dropdown()
        log.info("Selected second contract.")
        newmobilitypolicypage.new_policy_budget_value().send_keys("150")
        log.info("Set policy budget to '150'.")
        newmobilitypolicypage.new_policy_datepicker()
        log.info("Set start date on 'today'.")
        log.info("Set end date as undefined.")
        newmobilitypolicypage.new_policy_select_parking()
        log.info("Selected mobility option 'parking'.")
        newmobilitypolicypage.new_policy_select_all_available_users().click()
        newmobilitypolicypage.new_policy_move_users_to_linked()
        log.info("Linked all available users.")
        log.info("Saving the policy as a draft.")

        newmobilitypolicypage.save_policy_as_draft_button()
        time.sleep(1)
        message = newmobilitypolicypage.message_saved_as_draft().text
        assert message == "Mobility policy successfully saved as draft."
        log.info("Succesfully verified new mobility policy has been saved as draft.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_activate_draft(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_draft()
        log.info("Filtering for draft policies.")
        time.sleep(1)
        changemobilitypolicypage = mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        changemobilitypolicypage.change_mobility_policy_activate_draft()
        message = str(changemobilitypolicypage.change_mobility_policy_activation_message().text)
        assert "activated successfully" in message
        log.info("Succesfully activated draft policy.")

class TestSubModuleTwo(BaseClass):
    def test_mobility_policies_draft_link_users(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        log.info("Filtering for draft policies.")
        mobilitypoliciesmainpage.mobility_policies_filter_draft()
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        log.info("Opened top draft.")
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_select_all_linked_users()
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_unlink_all_users()
        log.info("Unlinked all users from draft policy.")
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.CONTROL + "a"
        )
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.DELETE
        )
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            "active test"
        )
        log.info("Changed draft name to 'active test'.")
        changemobilitypolicypage.change_mobility_policy_save()
        log.info("Saved draft.")
        mobilitypoliciesmainpage.mobility_policies_searchbar().send_keys("active test")
        time.sleep(1)
        log.info("Searched for 'active draft' policy.")
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        log.info("Opened 'active draft' policy.")
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_select_all_available_users()
        changemobilitypolicypage.change_mobility_policy_link_all_users()
        log.info("Linked all users to draft.")
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
        timestampbase = datetime.now()
        limitedtimestamp = timestampbase.strftime('%Y-%m-%d %H')

        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            timestamp
        )
        log.info("Changed draft name to 'timestamp'.")
        changemobilitypolicypage.change_mobility_policy_save()
        time.sleep(1)
        mobilitypoliciesmainpage.mobility_policies_filter_draft()
        mobilitypoliciesmainpage.mobility_policies_searchbar().send_keys(limitedtimestamp)
        mobilitypoliciesmainpage.mobility_policies_view_top_policy()

        changemobilitypolicypage.change_mobility_policy_activate_draft()
        message = str(
            changemobilitypolicypage.change_mobility_policy_activation_message().text
        )
        assert "activated successfully" in message
        log.info("Succesfully verified all users are linked and policy is activated.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_mobility_policies_active_change_mob(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")

        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_active()
        log.info("Filtered for 'active' policies.")
        time.sleep(1)
        changemobilitypolicypage = (
            mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        )
        log.info("Opened top policy.")
        time.sleep(1)
        changemobilitypolicypage.change_mobility_policy_select_parking()
        log.info("Selected mobility option 'parking'.")
        changemobilitypolicypage.change_mobility_policy_select_car_sharing()
        log.info("Selected mobility policy 'car sharing'.")
        changemobilitypolicypage.change_mobility_policy_select_bike_sharing()
        log.info("Selected mobility option 'bike sharing'.")
        changemobilitypolicypage.change_mobility_policy_save()
        time.sleep(1)
        message = str(changemobilitypolicypage.change_mobility_policy_activation_message().text)
        assert "updated" in message
        log.info("Succesfully verified that active policy has been updated.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
    
    def test_mobility_policies_duplicate(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])

        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to mobility policies page.")
        mobilitypoliciesmainpage = homepage.menu_label_mobility_policies()
        mobilitypoliciesmainpage.mobility_policies_filter_draft()
        log.info("Filtered for draft policies.")
        time.sleep(1)
        changemobilitypolicypage = mobilitypoliciesmainpage.mobility_policies_view_top_policy()
        log.info("Opened top policy.")
        log.info("Attempting to duplicate policy.")
        changemobilitypolicypage.change_mobility_policy_duplicate()
        time.sleep(1)
        policyname = changemobilitypolicypage.change_mobility_policy_name_field()
        newname = str(policyname.get_attribute("value"))
        assert 'copy' in newname
        log.info("Succesfully duplicated mobility policy.")

        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.CONTROL + "a"
        )
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(
            Keys.DELETE)
        
        timestamp = str(datetime.now())
        
        changemobilitypolicypage.change_mobility_policy_name_field().send_keys(timestamp)

        log.info("Named duplicate policy 'timestamp'.")
        changemobilitypolicypage.change_mobility_policy_save()
        log.info("Succesfully saved duplicate policy.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        