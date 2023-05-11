from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
import time

class ChangeMobilityPolicyPage:
    def __init__(self, driver):
        self.driver = driver
    
    def change_mobility_policy_activate_draft(self):
        selector1 = (By.XPATH, "//button[@class='d-flex align-items-center custom-toggle-button-hidden dropdown-toggle btn btn-default']")
        selector2 = (By.XPATH, "//a[normalize-space()='Activate']")
        selector3 = (By.CSS_SELECTOR, "button[data-testid='confirmModalButton']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
    
    def change_mobility_policy_activation_message(self):
        selector1 = (By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")
        return self.driver.find_element(*selector1)
