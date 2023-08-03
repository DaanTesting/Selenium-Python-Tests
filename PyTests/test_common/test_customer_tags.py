import pytest
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects


@pytest.fixture(params=LoginPageData.test_fullflow_data)
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

        tagname = str(datetime.now())
        tagmanagerpage.choose_tag_name_field().send_keys(tagname)
        log.info("Set tag name as 'timestamp'.")
        tagmanagerpage.select_available_user()
        time.sleep(2)
        tagmanagerpage.move_all_users_right()
        log.info("Linked available user.")
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

        tagname = str(datetime.now())
        now = datetime.now()
        tagdate = now.strftime("%Y-%m-%d")
        tagmanagerpage.choose_tag_name_field().send_keys(tagname)
        log.info("Set tag name as 'timestamp'.")
        tagmanagerpage.driver.find_element(
            By.CSS_SELECTOR, "span[class='color-badge color-badge-blue']"
        ).click()
        log.info("Set new tag color.")
        time.sleep(1)
        tagmanagerpage.select_available_user()
        time.sleep(2)
        tagmanagerpage.move_all_users_right()
        log.info("Link all available users.")
        tagmanagerpage.tag_save_button()
        log.info("Saved new tag.")
        time.sleep(1)
        homepage.menu_label_administration()
        userdetailpagetest = homepage.menu_label_users()
        time.sleep(1)
        assert userdetailpagetest.driver.find_element(
            By.XPATH, "(//div[@class='color-badge-blue user-tag'])[1]"
        )
        log.info("Succesfully verified badge color is correct.")

        tags = userdetailpagetest.driver.find_elements(
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
        time.sleep(2)
        tagmanagerpage.unlink_users()
        log.info("Unlinked all users.")
        tagmanagerpage.tag_save_button()
        log.info("Saved edited tag.")
        time.sleep(1)
        newtagname = tagmanagerpage.driver.find_element(
            By.CSS_SELECTOR, "div[class='text-truncate ']"
        ).text
        assert "SecondName" in newtagname
        log.info("Succesfully verified edited name.")
        numberoflinkedusers = tagmanagerpage.driver.find_element(
            By.XPATH, "//tr/td[4]"
        ).text
        assert numberoflinkedusers
        log.info("Succesfully verified number of linked users.")

        tagmanagerpage.delete_tag()
        log.info("Delete test tag.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()