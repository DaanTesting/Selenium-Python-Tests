from selenium.webdriver.common.by import By
from pageObjects.CpoIndividualCustomer import CpoIndividualCustomer


class CpoCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def search_by_name_field(self):
        selector = (
            By.CSS_SELECTOR,
            "input[placeholder='Name, email, phone, or internal code']",
        )
        return self.driver.find_element(*selector)

    def click_on_top_result_customer(self):
        selector = (By.CSS_SELECTOR, "a[href='/co/admin/customers/599/']")
        self.driver.find_element(*selector).click()
        cpoindividualcustomer = CpoIndividualCustomer(self.driver)
        return cpoindividualcustomer
    
    def click_on_top_result_carrefour(self):
        selector = (By.CSS_SELECTOR, "a[href='/co/admin/customers/3/']")
        self.driver.find_element(*selector).click()
        cpoindividualcustomer = CpoIndividualCustomer(self.driver)
        return cpoindividualcustomer
    

