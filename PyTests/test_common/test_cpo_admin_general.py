import datetime
import time
import pytest
import random
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from pageObjects.SplitBillingMainPage import SplitBillingMainPage
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_reimbursementpolicy_valuechange(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to split billing page.")
        homepage.menu_label_chargingpoints()
        splitbillingmainpage = homepage.menu_label_splitbilling()
        log.info("Opening reimbursement policy tab.")
        splitbillingmainpage.reimbursement_policies_tab()
        log.info("Opening blue collar testpolicy.")
        splitbillingmainpage.blue_collar_testpolicy()
        log.info("Attempting to change policy value.")
        splitbillingmainpage.reimbursement_policy_value_button()
        splitbillingmainpage.reimbursement_policy_new_value_field().send_keys("5")
        splitbillingmainpage.reimbursement_policy_new_value_add()

        newreimbursementvalue = self.driver.find_element(
            By.XPATH, "//tbody/tr[1]/td[2]"
        ).text
        assert "€5.00" in newreimbursementvalue
        log.info("Succesfully changed policy value.")

        splitbillingmainpage.reimbursement_policy_value_delete()

        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='alert alert-success alert-dismissible']",
                )
            )
        )
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='alert alert-success alert-dismissible']"
        ).text

        print(Message)

        assert Message == "Reimbursement policy value has been deleted."
        log.info("Deleted new value. Test has been reset.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

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
        homepage.menu_label_chargingpoints()
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
        homepage.menu_label_chargingpoints()
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
        homepage.menu_label_chargingpoints()
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
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Autotest Location Configuration'.")
        locationsmainpage.find_location().send_keys("Autotest Location Configuration" + Keys.ENTER)
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
    def test_add_charging_device(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        log.info("Searching for 'Autotest Location Configuration'.")
        locationsmainpage.find_location().send_keys("Autotest Location Configuration" + Keys.ENTER)
        individualcharginglocation = locationsmainpage.find_location_click_top_result()
        log.info("Navigating to devices tab.")
        individualcharginglocation.devices_tab()
        log.info("Attempting to register a new device.")
        individualcharginglocation.register_a_new_device()

        dt = str(datetime.now())
        log.info("Setting OCPP_ID.")
        individualcharginglocation.OCPP_ID_field().send_keys("MOCK_<" + dt + ">")
        log.info("Selecting contract from dropdown.")
        individualcharginglocation.select_contract_dropdown()
        log.info("Attempting to finalize registration.")
        individualcharginglocation.register_new_device_button()
        time.sleep(1)
        message = individualcharginglocation.device_created_alert().text
        assert message == "Device created."
        log.info("Succesfully registered new device.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestSeven(BaseClass):
    def test_add_charging_location(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to locations page.")
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.create_location_button()
        locationsmainpage.create_location_select_customer()
        timestamp = str(datetime.now())
        locationsmainpage.create_location_location_name().send_keys(timestamp)
        locationsmainpage.create_location_address().send_keys("Raas Van Gaverestraat 11")
        locationsmainpage.create_location_postcode().send_keys("9000")
        locationsmainpage.create_location_town().send_keys("Gent" + Keys.ENTER)
        locationsmainpage.create_location_create_button()
        successmessage = str(self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text)
        assert "Charging location saved" in successmessage

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestEight(BaseClass):
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
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        createcustomerpage = cpocustomerpage.create_customer_button()
        random_integer = str(random.randint(100000000, 999999999))
        timestamp = str(datetime.now())
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
        assert "Customer deleted:" in message

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestNine(BaseClass):
    def test_activate_pending_contract(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to customers page.")
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()
        cpocustomerpage.pending_contracts_button()
        cpocustomerpage.activate_top_pending_contract()
        message = cpocustomerpage.message_banner().text
        assert message == "Contract approved."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        
class TestTen(BaseClass):
    def test_activate_customer(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to customers page.")
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()

        cpocustomerpage.active_customers_filter()
        cpocustomerpage.blocked_customer_filter()
        title = cpocustomerpage.page_title().text
        assert "Customers that require activation" in title

        cpocustomerpage.click_on_top_result_customer()

        try:
            cpocustomerpage.approve_customer()
            message = cpocustomerpage.message_banner().text
            assert message == "Customer accepted"
        except Exception as error:
            log.info(error)

        cpocustomerpage.approve_registration()
        message = cpocustomerpage.message_banner().text
        assert message == "Customer registered and login credentials are sent."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

class TestEleven(BaseClass):
    def test_filters_customer_page(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to customers page.")
        homepage.menu_label_chargingpoints()
        cpocustomerpage = homepage.menu_label_cpo_customers()

        cpocustomerpage.active_customers_filter()
        cpocustomerpage.pending_customer_filter()
        cpocustomerpage.new_customer_filter()
        cpocustomerpage.blocked_customer_filter()

        empty_page_title = self.driver.find_element(By.XPATH, "(//p)[2]").text
        assert empty_page_title == "No customers found."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()








