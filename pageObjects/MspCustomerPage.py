from selenium.webdriver.common.by import By
from pageObjects.MspIndividualCustomer import MspIndividualCustomer


class MspCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def search_by_name_field(self):
        selector1 = (
            By.CSS_SELECTOR,
            "input[placeholder='Name, email, phone, or internal code']",
        )
        return self.driver.find_element(*selector1)

    def click_on_top_result_customer(self):
        selector1 = (By.CSS_SELECTOR, "a[href='/sp/admin/customers/259/']")
        self.driver.find_element(*selector1).click()
        mspindividualcustomer = MspIndividualCustomer(self.driver)
        return mspindividualcustomer

    def click_on_main_flow_account(self):
        selector1 = (By.CSS_SELECTOR, "a[href='/sp/admin/customers/634/']")
        self.driver.find_element(*selector1).click()
        mspindividualcustomer = MspIndividualCustomer(self.driver)
        return mspindividualcustomer
