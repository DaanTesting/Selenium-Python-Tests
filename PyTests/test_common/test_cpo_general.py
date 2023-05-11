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
from pageObjects.SplitBillingMainPage import SplitBillingMainPage


@pytest.fixture(params=LoginPageData.test_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_reimbursementpolicy_valuechange(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        splitbillingmainpage = homepage.menu_label_splitbilling()
        splitbillingmainpage.reimbursement_policies_tab()
        splitbillingmainpage.blue_collar_testpolicy()
        splitbillingmainpage.reimbursement_policy_value_button()
        splitbillingmainpage.reimbursement_policy_new_value_field().send_keys("5")
        splitbillingmainpage.reimbursement_policy_new_value_add()

        newreimbursementvalue = self.driver.find_element(
            By.XPATH, "//tbody/tr[1]/td[2]"
        ).text
        assert "€5.00" in newreimbursementvalue
        log.makeRecord

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

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_filter_locations(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Carrefour" + "\n")
        time.sleep(1)

        results = self.driver.find_elements(By.XPATH, "//tbody/tr")
        for result in results:
            assert "Carrefour" in result.text

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_locations_search_devices(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_device().send_keys("QATEST" + "\n")
        devicedata = self.driver.find_element(
            By.XPATH, "//p[normalize-space()='QATEST']"
        ).text

        print(devicedata)
        assert devicedata == "QATEST"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_configure_location_information(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Autotest Location Configuration")
        individualcharginglocation = locationsmainpage.find_location_click_top_result()
        individualcharginglocation.edit_button()
        individualcharginglocation.location_name_field().send_keys(" In Progress")
        individualcharginglocation.contact_phone_field().clear()
        individualcharginglocation.contact_phone_field().send_keys("0477998844")
        individualcharginglocation.contact_name_field().send_keys(" Is Active")
        individualcharginglocation.update_button()

        updatedlocationname = individualcharginglocation.overview_location_name().text
        assert (
            updatedlocationname
            == "Location: Autotest Location Configuration In Progress"
        )
        updatedcontactphone = individualcharginglocation.overview_contact_phone().text
        assert updatedcontactphone == "0477998844"
        updatedcontactname = individualcharginglocation.overview_contact_name().text
        assert updatedcontactname == "Robo-Daan Is Active"

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

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_configure_location_location_data(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Autotest Location Configuration")
        individualcharginglocation = locationsmainpage.find_location_click_top_result()
        individualcharginglocation.edit_button()
        individualcharginglocation.location_address_field().clear()
        individualcharginglocation.location_address_field().send_keys(
            "Robotus Destroyusstraat 99"
        )
        individualcharginglocation.location_postcode_field().clear()
        individualcharginglocation.location_postcode_field().send_keys("2440")
        individualcharginglocation.location_town_field().clear()
        individualcharginglocation.location_town_field().send_keys("Geel")
        individualcharginglocation.location_country_field_Netherlands()
        time.sleep(1)
        individualcharginglocation.update_button()
        time.sleep(1)

        updatedaddress = individualcharginglocation.overview_address().text
        assert updatedaddress == "Robotus Destroyusstraat 99, 2440 Geel, NL"

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

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_add_charging_device(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        homepage.menu_label_chargingpoints()
        locationsmainpage = homepage.menu_label_locations()
        locationsmainpage.find_location().send_keys("Autotest Location Configuration")
        individualcharginglocation = locationsmainpage.find_location_click_top_result()
        individualcharginglocation.devices_tab()
        individualcharginglocation.register_a_new_device()

        dt = str(datetime.datetime.now())
        individualcharginglocation.OCPP_ID_field().send_keys("MOCK_<" + dt + ">")
        individualcharginglocation.select_contract_dropdown()
        individualcharginglocation.register_new_device_button()
        time.sleep(1)
        message = individualcharginglocation.device_created_alert().text
        assert message == "Device created."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
