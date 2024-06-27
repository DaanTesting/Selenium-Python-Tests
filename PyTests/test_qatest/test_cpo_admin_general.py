import datetime
import time
import random
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.qatest_login_data)
def login_data(request):
    return request.param


class TestTwo(BaseClass):
    def test_filter_locations(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching locations list for 'Carrefour'.")
        locationsmainpage.find_location().send_keys("Carrefour" + "\n")
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tbody/tr")
        for result in results:
            assert "Carrefour" in result.text
        log.info("Verified only Carrefour locations show up.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_locations_search_devices(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for device 'QATEST'.")
        locationsmainpage.find_device().send_keys("QATEST" + "\n")
        devicedata = self.driver.find_element(
            By.XPATH, "//p[normalize-space()='QATEST']"
        ).text

        print(devicedata)
        assert devicedata == "QATEST"
        log.info("Verified 'QATEST' is only device returned.")
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_configure_location_information(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Autotest Location Configuration'.")
        locationsmainpage.find_location().send_keys("Autotest Location Configuration" + Keys.ENTER)
        individualcharginglocation = locationsmainpage.find_location_click_top_result()
        log.info("Attempting to edit 'Autotest Location'.")
        individualcharginglocation.edit_button()
        log.info("Edit location name.")
        individualcharginglocation.location_name_field().send_keys(" In Progress")
        log.info("Edit location phone number.")
        individualcharginglocation.contact_phone_field().clear()
        individualcharginglocation.contact_phone_field().send_keys("0477998844")
        log.info("Edit contact name.")
        individualcharginglocation.contact_name_field().send_keys(" Is Active")
        log.info("Attempting to update location.")
        individualcharginglocation.update_button()

        updatedlocationname = individualcharginglocation.overview_location_name().text
        assert (
            updatedlocationname
            == "Location: Autotest Location Configuration In Progress"
        )
        log.info("Verified location name changed correctly.")
        updatedcontactphone = individualcharginglocation.overview_contact_phone().text
        assert updatedcontactphone == "0477998844"
        log.info("Verified phone number changed correctly.")
        updatedcontactname = individualcharginglocation.overview_contact_name().text
        assert updatedcontactname == "Robo-Daan Is Active"
        log.info("Verified contact name changed correctly.")

        log.info("Attempting to reset location information.")
        individualcharginglocation.edit_button()
        individualcharginglocation.location_name_field().clear()
        individualcharginglocation.location_name_field().send_keys(
            "Autotest Location Configuration"
        )
        individualcharginglocation.contact_phone_field().clear()
        individualcharginglocation.contact_phone_field().send_keys("0477889955")

        individualcharginglocation.contact_name_field().clear()
        individualcharginglocation.contact_name_field().send_keys("Robo-Daan")
        individualcharginglocation.update_button()

        updatedlocationname = individualcharginglocation.overview_location_name().text
        assert updatedlocationname == "Location: Autotest Location Configuration"
        updatedcontactphone = individualcharginglocation.overview_contact_phone().text
        assert updatedcontactphone == "0477889955"
        updatedcontactname = individualcharginglocation.overview_contact_name().text
        assert updatedcontactname == "Robo-Daan"
        log.info("Succesfully reset location information.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_configure_location_location_data(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Autotest Location Configuration'.")
        locationsmainpage.find_location().send_keys("Autotest Location Configuration")
        individualcharginglocation = locationsmainpage.find_location_click_top_result()
        log.info("Attempting to edit 'Autotest Location'.")
        individualcharginglocation.edit_button()
        individualcharginglocation.location_address_field().clear()
        individualcharginglocation.location_address_field().send_keys(
            "Robotus Destroyusstraat 99"
        )
        log.info("Updated location adress")
        individualcharginglocation.location_postcode_field().clear()
        individualcharginglocation.location_postcode_field().send_keys("2440")
        log.info("Updated postcode.")
        individualcharginglocation.location_town_field().clear()
        individualcharginglocation.location_town_field().send_keys("Geel")
        log.info("Updated town.")
        individualcharginglocation.location_country_field_Netherlands()
        log.info("Updated country.")
        time.sleep(1)
        log.info("Attempting to update location data.")
        individualcharginglocation.update_button()
        time.sleep(1)

        updatedaddress = individualcharginglocation.overview_address().text
        assert updatedaddress == "Robotus Destroyusstraat 99, 2440 Geel, NL"
        log.info("Verified location data have been changed correctly.")
        log.info("Attempting to reset location data.")

        individualcharginglocation.edit_button()
        individualcharginglocation.location_address_field().clear()
        individualcharginglocation.location_address_field().send_keys(
            "Robotus Destroyuslaan 99"
        )
        individualcharginglocation.location_postcode_field().clear()
        individualcharginglocation.location_postcode_field().send_keys("9000")
        individualcharginglocation.location_town_field().clear()
        individualcharginglocation.location_town_field().send_keys("Gent")
        individualcharginglocation.location_country_field_Belgium()
        time.sleep(1)
        individualcharginglocation.update_button()
        time.sleep(1)

        updatedaddress = individualcharginglocation.overview_address().text
        assert updatedaddress == "Robotus Destroyuslaan 99, 9000 Gent, BE"
        log.info("Succesfully reset location data.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSix(BaseClass):
    def test_add_token(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        cpotokenspage = homepage.menu_label_cpo_tokens()
        cpotokenspage.add_token()
        generate_uid = str(random.randint(0, 999999999)).zfill(9)
        cpotokenspage.UID_field().send_keys(generate_uid)
        time.sleep(1)
        cpotokenspage.select_customer()
        time.sleep(1)
        cpotokenspage.save_token_button()

class TestSeven(BaseClass):
    def test_create_customer(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to customers page.")
        cpocustomerpage = homepage.menu_label_cpo_customers()
        createcustomerpage = cpocustomerpage.create_customer_button()
        random_integer = str(random.randint(100000000, 999999999))
        timestamp = str(datetime.datetime.now())
        createcustomerpage.company_name_field().send_keys(random_integer)
        createcustomerpage.company_type_field().send_keys("Generated on: " + timestamp)
        createcustomerpage.VAT_number_field().send_keys("BE1252175374")
        createcustomerpage.first_name_field().send_keys(random_integer)
        createcustomerpage.last_name_field().send_keys(random_integer)
        createcustomerpage.email_address_field().send_keys("daan.swinnen+" + random_integer + "@optimile.eu")
        createcustomerpage.phone_field().send_keys("+32474531188")
        createcustomerpage.address_field().send_keys("Autotest straat 123")
        createcustomerpage.postcode_field().send_keys("9000")
        createcustomerpage.town_field().send_keys("Gent")

        cpoindividualcustomer = createcustomerpage.save_button()
        message = cpoindividualcustomer.message_banner().text
        assert message == "Customer created."

        cpoindividualcustomer.delete_button()
        message = cpoindividualcustomer.message_banner().text
        assert "Customer successfully deleted." in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
