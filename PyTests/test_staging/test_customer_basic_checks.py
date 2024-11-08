import platform
import random
import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from PyTests.TestData.GeneralData import GeneralData
from utilities.BaseClass import BaseClass

user_os = platform.system()


@pytest.fixture(params=LoginPageData.staging_customer_login_data)
def login_data(request):
    return request.param

@pytest.fixture(params=GeneralData.test_general_data)
def general_data(request):
    return request.param


class TestOne(BaseClass):
    def test_administration_tab(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to administration tab.")
        homepage.menu_label_administration()
        accountdetailspage = homepage.menu_label_account_details()
        accountdetailstitle = str(
            accountdetailspage.account_details_title().text
        )
        assert accountdetailstitle == "Account details"
        log.info("Verified account details page.")
        homepage.menu_label_preferences()
        preferencestitle = str(
            self.driver.find_element(
                By.XPATH, "//h1[.='Account preferences']"
            ).text
        )
        assert preferencestitle == "Account preferences"
        log.info("Verified preferences page.")
        homepage.menu_label_users()
        userstitle = str(
            self.driver.find_element(
                By.XPATH, "//h1[contains(.,'Overview')]"
            ).text
        )
        assert "Overview" in userstitle
        log.info("Verified users page.")

        # tagmanagerpage = homepage.menu_label_tag_manager()
        # tagtitle = str(tagmanagerpage.page_title().text)
        # assert "Tag manager" in tagtitle
        # log.info("Verified tags page.")

        homepage.menu_label_administration()
        homepage.menu_label_external_users()
        externalusertitle = str(
            self.driver.find_element(By.XPATH, "//h1[.='External users']").text
        )
        assert externalusertitle == "External users"
        log.info("Verified external users page.")
        homepage.menu_label_user_invites()
        titleuserinvites = str(
            self.driver.find_element(By.XPATH, "//h1[.='User invites']").text
        )
        assert titleuserinvites == "User invites"
        log.info("Verified user invites page.")

        reportingpage = homepage.menu_label_reporting()
        title_reportingpage = reportingpage.page_title().text
        assert title_reportingpage == "Reports\nCreate report"
        log.info("Succesfully verified reporting page")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_finance_tab(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to finance tab.")
        homepage.menu_label_finance()
        homepage.menu_label_invoices()
        titleinvoices = str(
            self.driver.find_element(By.XPATH, "//h1[.='Invoices']").text
        )
        assert titleinvoices == "Invoices"
        log.info("Verified invoices page.")
        homepage.menu_label_payment_methods()
        titlepaymentmethods = str(
            self.driver.find_element(
                By.XPATH, "//h1[.='Payment methods']"
            ).text
        )
        assert titlepaymentmethods == "Payment methods"
        log.info("Verified payment methods page.")
        homepage.menu_label_credit()
        titlecredit = str(
            self.driver.find_element(
                By.XPATH, "//h1[.='Credit transactions']"
            ).text
        )
        assert titlecredit == "Credit transactions"
        log.info("Verified credit transactions page.")
        homepage.menu_label_revenue()
        titlerevenue = str(
            self.driver.find_element(By.XPATH, "//h1[.='Revenue']").text
        )
        assert titlerevenue == "Revenue"
        log.info("Verified revenue page.")
        homepage.menu_label_payment_requests()
        titlepaymentrequests = str(
            self.driver.find_element(
                By.XPATH, "//h1[contains(.,'Payment requests')]"
            ).text
        )
        assert titlepaymentrequests == "Payment requests"
        log.info("Verified payment requests page.")
        homepage.menu_label_debit_notes()
        titledebitnotes = str(
            self.driver.find_element(By.XPATH, "//h1[.='Debit notes']").text
        )
        assert titledebitnotes == "Debit notes"
        log.info("Verified debit notes page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_account_details_screen(self, setup, login_data, general_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigate to account details screen.")
        homepage.menu_label_administration()
        accountdetailspage = homepage.menu_label_account_details()
        log.info("Attempting to change all account details.")
        accountdetailspage.account_details_company_type().clear()
        accountdetailspage.account_details_company_type().send_keys(
            "Active Flow"
        )
        accountdetailspage.account_details_first_name().clear()
        accountdetailspage.account_details_first_name().send_keys("ActiveTest")
        accountdetailspage.account_details_last_name().clear()
        accountdetailspage.account_details_last_name().send_keys("Ongoing")
        accountdetailspage.account_details_emailaddress().clear()
        accountdetailspage.account_details_emailaddress().send_keys(
            "daan.swinnen+active@optimile.eu"
        )
        accountdetailspage.account_details_phone().clear()
        accountdetailspage.account_details_phone().send_keys("014524213")
        accountdetailspage.account_details_language_select_english()

        time.sleep(1)

        accountdetailspage.account_details_save_button()
        message = str(
            accountdetailspage.account_details_updated_message().text
        )
        assert "Account details updated" in message
        log.info("Succesfully saved changes.")
        log.info("Attempting to verify accuracy of changes.")

        companytype = str(
            accountdetailspage.account_details_company_type().get_attribute(
                "value"
            )
        )
        assert companytype == "Active Flow"

        if user_os == "Darwin":
            accountdetailspage.account_details_company_type().send_keys(
                Keys.COMMAND + "a" + Keys.BACKSPACE
            )
        else:
            accountdetailspage.account_details_company_type().send_keys(
                Keys.CONTROL + "a" + Keys.BACKSPACE
            )

        accountdetailspage.account_details_company_type().send_keys(
            "Autotesting"
        )

        firstname = str(
            accountdetailspage.account_details_first_name().get_attribute(
                "value"
            )
        )
        assert firstname == "ActiveTest"

        if user_os == "Darwin":
            accountdetailspage.account_details_first_name().send_keys(
                Keys.COMMAND + "a" + Keys.BACKSPACE
            )
        else:
            accountdetailspage.account_details_first_name().send_keys(
                Keys.CONTROL + "a" + Keys.BACKSPACE
            )

        accountdetailspage.account_details_first_name().send_keys(
            "Splitbilling"
        )

        lastname = str(
            accountdetailspage.account_details_last_name().get_attribute(
                "value"
            )
        )
        assert lastname == "Ongoing"

        if user_os == "Darwin":
            accountdetailspage.account_details_last_name().send_keys(
                Keys.COMMAND + "a" + Keys.BACKSPACE
            )
        else:
            accountdetailspage.account_details_last_name().send_keys(
                Keys.CONTROL + "a" + Keys.BACKSPACE
            )

        accountdetailspage.account_details_last_name().send_keys(
            "TestCustomer"
        )

        emailaddress = str(
            accountdetailspage.account_details_emailaddress().get_attribute(
                "value"
            )
        )
        assert emailaddress == "daan.swinnen+active@optimile.eu"

        if user_os == "Darwin":
            accountdetailspage.account_details_emailaddress().send_keys(
                Keys.COMMAND + "a" + Keys.BACKSPACE
            )
        else:
            accountdetailspage.account_details_emailaddress().send_keys(
                Keys.CONTROL + "a" + Keys.BACKSPACE
            )

        accountdetailspage.account_details_emailaddress().send_keys(general_data['MainCustomerMail'])

        phonenumber = str(
            accountdetailspage.account_details_phone().get_attribute("value")
        )
        assert phonenumber == "+3214524213"

        if user_os == "Darwin":
            accountdetailspage.account_details_phone().send_keys(
                Keys.COMMAND + "a" + Keys.BACKSPACE
            )
        else:
            accountdetailspage.account_details_phone().send_keys(
                Keys.CONTROL + "a" + Keys.BACKSPACE
            )

        accountdetailspage.account_details_phone().send_keys("014568945")

        accountdetailspage.account_details_language_select_nederlands()

        accountdetailspage.account_details_save_button()
        message = str(
            accountdetailspage.account_details_updated_message().text
        )
        assert "Account details updated" in message

        log.info("Succesfully verified accuracy of changes.")
        log.info("Succesfully reset test.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_users_details_screen(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)
        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigate to users page.")
        homepage.menu_label_administration()
        userdetailpagetest = homepage.menu_label_users()
        log.info("Opening top user detail page.")
        userdetailpagetest.user_detail_open_top_user()
        log.info("Attempting to update all user data.")
        userdetailpagetest.user_detail_first_name().clear()
        userdetailpagetest.user_detail_first_name().send_keys("Robotester")
        userdetailpagetest.user_detail_last_name().clear()
        userdetailpagetest.user_detail_last_name().send_keys("Onamission")
        userdetailpagetest.user_detail_email().clear()
        current_datetime = datetime.now()
        timestamp = current_datetime.strftime("%m%d%Y%H%M%S%f")[:-3]
        email_format = f"daan.swinnen+{timestamp}@optimile.eu"

        userdetailpagetest.user_detail_email().send_keys(email_format)
        userdetailpagetest.user_detail_phone().clear()
        random_variable = str(random.randint(100000, 999999))
        userdetailpagetest.user_detail_phone().send_keys(
            "+32477" + random_variable
        )
        userdetailpagetest.user_detail_postcode().clear()
        userdetailpagetest.user_detail_postcode().send_keys("9999")
        userdetailpagetest.user_detail_town().clear()
        userdetailpagetest.user_detail_town().send_keys("Roboland")
        userdetailpagetest.user_detail_role_select_accountadmin()
        userdetailpagetest.user_detail_notification_settings()
        userdetailpagetest.user_detail_save_button()

        updatemessage = str(
            userdetailpagetest.user_detail_update_message().text
        )
        assert "User information updated" in updatemessage
        log.info("Verified user data was successfully updated.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
