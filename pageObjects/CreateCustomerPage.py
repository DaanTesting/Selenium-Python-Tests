from selenium.webdriver.common.by import By
from pageObjects.CpoIndividualCustomer import CpoIndividualCustomer

class CreateCustomerPage:
    def __init__(self, driver):
        self.driver = driver
    
    def company_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-company_name")
        return self.driver.find_element(*selector1)
    
    def company_type_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-company_type")
        return self.driver.find_element(*selector1)
    
    def VAT_number_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-vat_number")
        return self.driver.find_element(*selector1)
    
    def first_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-first_name")
        return self.driver.find_element(*selector1)
    
    def last_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-last_name")
        return self.driver.find_element(*selector1)
    
    def email_address_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-email")
        return self.driver.find_element(*selector1)
    
    def phone_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-phone")
        return self.driver.find_element(*selector1)
    
    def address_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-address")
        return self.driver.find_element(*selector1)
    
    def postcode_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-postcode")
        return self.driver.find_element(*selector1)
    
    def town_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_details-town")
        return self.driver.find_element(*selector1)
    
    def save_button(self):
        selector1 = (By.XPATH, "(//button[.='Save'])")
        self.driver.find_element(*selector1).click()
        cpoindividualcustomer = CpoIndividualCustomer(self.driver)
        return cpoindividualcustomer
    
        
