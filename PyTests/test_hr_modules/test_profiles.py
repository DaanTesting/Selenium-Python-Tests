import time
import pytest
import datetime
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


class TestOne(BaseClass):
    def test_tags_create_delete_basic(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to profiles page.")
        homepage.menu_label_administration()
        tagmanagerpage = homepage.menu_label_tag_manager()
        log.info("Attempting to create new tag.")
        tagmanagerpage.create_tag_button()

        tagname = str(datetime.datetime.now())
        tagmanagerpage.choose_tag_name_field().send_keys(tagname)
        log.info("Set tag name as 'timestamp'.")
        tagmanagerpage.select_all_available_users()
        tagmanagerpage.move_all_users_right()
        log.info("Linked all available users.")
        tagmanagerpage.tag_save_button()
        log.info("Saved new tag.")
        time.sleep(1)
        tagmanagerpage.delete_tag()
        log.info("Deleted new tag.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_tags_create_delete_expanded(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_administration()
        log.info("Succesfully logged in.")
        tagmanagerpage = homepage.menu_label_tag_manager()
        log.info("Attempting to create new tag.")
        tagmanagerpage.create_tag_button()

        tagname = str(datetime.datetime.now())
        now = datetime.datetime.now()
        tagdate = now.strftime("%Y-%m-%d")
        tagmanagerpage.choose_tag_name_field().send_keys(tagname)
        log.info("Set tag name as 'timestamp'.")
        tagmanagerpage.driver.find_element(By.CSS_SELECTOR, "span[class='color-badge color-badge-blue']").click()
        log.info("Set new tag color.")
        time.sleep(1)
        tagmanagerpage.select_all_available_users()
        tagmanagerpage.move_all_users_right()
        log.info("Link all available users.")
        tagmanagerpage.tag_save_button()
        log.info("Saved new tag.")
        time.sleep(1)
        homepage.menu_label_employees()
        profilesoverview = homepage.menu_label_profiles_overview()
        time.sleep(1)
        assert profilesoverview.driver.find_element(By.XPATH, "(//div[@class='color-badge-blue user-tag'])[1]")
        log.info("Succesfully verified badge color is correct.")

        tags = profilesoverview.driver.find_elements(
            By.XPATH, "//tr/td/div/div/div[@class='text-truncate ']"
        )
        for tag in tags:
            assert tagdate in tag.text
        
        log.info("Succesfully verified tagname.")

        homepage.menu_label_administration()
        tagmanagerpage = homepage.menu_label_tag_manager()
        time.sleep(1)
        log.info("Attempting to edit tag.")
        tagmanagerpage.edit_tag()
        time.sleep(1)
        tagmanagerpage.choose_tag_name_field().clear()
        tagmanagerpage.choose_tag_name_field().send_keys("SecondName")
        log.info("Edit tagname.")
        tagmanagerpage.select_all_linked_users()
        tagmanagerpage.unlink_users()
        log.info("Unlinked all users.")
        tagmanagerpage.tag_save_button()
        log.info("Saved edited tag.")
        time.sleep(1)
        newtagname = tagmanagerpage.driver.find_element(By.CSS_SELECTOR, "div[class='text-truncate ']").text
        assert "SecondName" in newtagname
        log.info("Succesfully verified edited name.")
        numberoflinkedusers = tagmanagerpage.driver.find_element(By.XPATH, "//tr/td[4]").text
        assert numberoflinkedusers
        log.info("Succesfully verified number of linked users.")

        tagmanagerpage.delete_tag()
        log.info("Delete test tag.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_profiles_multiple_app_invites(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        homepage.menu_label_administration()
        log.info("Navigating to profile overview.")
        hrprofilesoverview = homepage.menu_label_profiles_overview()
        log.info("Attempting to invite multiple users to the app.")
        hrprofilesoverview.profile_overview_checkbox_all_users()
        hrprofilesoverview.profile_overview_actions_button_invite()
        message = str(hrprofilesoverview.profile_overview_message().text)
        assert "app invitations have been sent successfully" in message
        log.info("Succesfully verified invites have been sent.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


    #blockeduntilissueresolved   def test_add_and_delete_user(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys("daan.swinnen@optimile.eu")
        loginpage.password_box().send_keys("UmVIi90k4GybBQz0X2Gv")
        homepage = loginpage.login_button()
        homepage.menu_label_cpo_customers()
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name, email, phone, or internal code']").send_keys("automatic" + Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/sp/admin/customers/1300/']").click()
        self.driver.find_element(By.XPATH, "//span[contains(.,'Users')]").click()
        self.driver.find_element(By.XPATH, "//a[.='Create user']").click()
        self.driver.find_element(By.CSS_SELECTOR, "#id_form-0-first_name").send_keys("Automatic")
        self.driver.find_element(By.CSS_SELECTOR, "#id_form-0-last_name").send_keys("Deleted")
        emailfield = self.driver.find_element(By.CSS_SELECTOR, "#id_form-0-email")
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime("%Y%m%d%H%M%S")
        emailfield.send_keys("daan.swinnen+" + timestamp_str + "@optimile.eu")
        self.driver.find_element(By.CSS_SELECTOR, "button[name='save']").click()

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_profiles()
        hrprofilesoverview = homepage.menu_label_profiles_overview()
        hrprofilesoverview.profile_overview_searchbar().send_keys("Automatic Deleted")









