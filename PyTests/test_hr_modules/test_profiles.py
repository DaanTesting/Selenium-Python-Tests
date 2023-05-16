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


@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_tags_create_delete_basic(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_profiles()
        tagmanagerpage = homepage.menu_label_tag_manager()
        tagmanagerpage.create_tag_button()

        tagname = str(datetime.datetime.now())
        tagmanagerpage.choose_tag_name_field().send_keys(tagname)
        tagmanagerpage.select_all_available_users()
        tagmanagerpage.move_all_users_right()
        tagmanagerpage.tag_save_button()
        time.sleep(1)
        tagmanagerpage.delete_tag()

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_tags_create_delete_expanded(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_profiles()
        tagmanagerpage = homepage.menu_label_tag_manager()
        tagmanagerpage.create_tag_button()

        tagname = str(datetime.datetime.now())
        now = datetime.datetime.now()
        tagdate = now.strftime("%Y-%m-%d")
        tagmanagerpage.choose_tag_name_field().send_keys(tagname)
        tagmanagerpage.driver.find_element(By.CSS_SELECTOR, "span[class='color-badge color-badge-blue']").click()
        time.sleep(1)
        tagmanagerpage.select_all_available_users()
        tagmanagerpage.move_all_users_right()
        tagmanagerpage.tag_save_button()
        time.sleep(1)
        profilesoverview = homepage.menu_label_profiles_overview()
        time.sleep(1)
        assert profilesoverview.driver.find_element(By.XPATH, "(//div[@class='color-badge-blue user-tag'])[1]")

        tags = profilesoverview.driver.find_elements(
            By.XPATH, "//tr/td/div/div/div[@class='text-truncate ']"
        )
        for tag in tags:
            assert tagdate in tag.text

        tagmanagerpage = homepage.menu_label_tag_manager()
        time.sleep(1)
        tagmanagerpage.edit_tag()
        time.sleep(1)
        tagmanagerpage.choose_tag_name_field().clear()
        tagmanagerpage.choose_tag_name_field().send_keys("SecondName")
        tagmanagerpage.select_all_linked_users()
        tagmanagerpage.unlink_users()
        tagmanagerpage.tag_save_button()
        time.sleep(1)
        newtagname = tagmanagerpage.driver.find_element(By.CSS_SELECTOR, "div[class='text-truncate ']").text
        assert "SecondName" in newtagname
        numberoflinkedusers = tagmanagerpage.driver.find_element(By.XPATH, "//tr/td[4]").text
        assert numberoflinkedusers

        tagmanagerpage.delete_tag()

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_profiles_multiple_app_invites(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_profiles()
        hrprofilesoverview = homepage.menu_label_profiles_overview()
        hrprofilesoverview.profile_overview_checkbox_all_users()
        hrprofilesoverview.profile_overview_actions_button_invite()
        message = str(hrprofilesoverview.profile_overview_message().text)
        assert "app invitations have been sent successfully" in message

