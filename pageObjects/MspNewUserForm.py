import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MspNewUserForm:
    def __init__(self, driver):
        self.driver = driver

    def first_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-first_name")
        return self.driver.find_element(*selector1)
    
    def last_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-last_name")
        return self.driver.find_element(*selector1)
    
    def email_address_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-email")
        return self.driver.find_element(*selector1)
    
    def phone_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-phone")
        return self.driver.find_element(*selector1)
    
    def address_field(self):
        selector1 = (By.XPATH, "//input[@id='id_form-0-address']")
        return self.driver.find_element(*selector1)
    
    def postcode_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-postcode")
        return self.driver.find_element(*selector1)
    
    def language_field(self):
        selector1 = (By.XPATH, "(//div[@class='filter-option'])[2]")
        selector2 = (By.XPATH, "(//input[@aria-label='Search'])[2]")
        selector3 = (By.CSS_SELECTOR, "#bs-select-1-1")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).send_keys("Nederlands" + Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*selector3).click()
    
    def town_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-town")
        return self.driver.find_element(*selector1)
    
    def country_dropdown_select_belgium(self):
        selector1 = (By.XPATH, "//div[@class='dropdown bootstrap-select bootstrapselect form-control']")
        selector2 = (By.XPATH, "//input[@aria-label='Search']")
        selector3 = (By.CSS_SELECTOR, "#bs-select-2-22")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).send_keys("Belgium" + Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(*selector3).click()

    def date_of_birth_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-birthday")
        return self.driver.find_element(*selector1)
    
    def rights_set_account_admin(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-1-SYS_ADMIN")
        self.driver.find_element(*selector1).click()

    def save_user_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector1).click()
