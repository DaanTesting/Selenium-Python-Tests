import time

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
        selector1 = (By.XPATH, "(//tr[1]/td[2])")
        self.driver.find_element(*selector1).click()
        mspindividualcustomer = MspIndividualCustomer(self.driver)
        return mspindividualcustomer

    def click_on_main_flow_account(self):
        selector1 = (By.CSS_SELECTOR, "a[href='/sp/admin/customers/634/']")
        self.driver.find_element(*selector1).click()
        mspindividualcustomer = MspIndividualCustomer(self.driver)
        return mspindividualcustomer

    def generate_mobility_customers_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download customers']")
        self.driver.find_element(*selector1).click()
        time.sleep(1)
        self.driver.find_element(*selector2).click()

    def generate_mobility_users_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download users']")
        self.driver.find_element(*selector1).click()
        time.sleep(1)
        self.driver.find_element(*selector2).click()

    def generate_all_customers_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download customers']")
        self.driver.find_element(*selector1).click()
        time.sleep(3)
        self.driver.find_element(*selector2).click()

    def generate_all_users_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download users']")
        self.driver.find_element(*selector1).click()
        time.sleep(3)
        self.driver.find_element(*selector2).click()
