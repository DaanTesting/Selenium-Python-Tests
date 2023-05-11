from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
import time

class NewMobilityPolicyPage:
    def __init__(self, driver):
        self.driver = driver

    def new_policy_name_field(self):
        selector = (By.CSS_SELECTOR, "input[placeholder='Type your policy name here']")
        return self.driver.find_element(*selector)
    
    def new_policy_type_dropdown(self):
        selector = (By.CSS_SELECTOR, "select[name='type']")
        dropdown = Select(self.driver.find_element(*selector))
        dropdown.select_by_index(0)

    def new_policy_contract_dropdown(self):
        selector = (By.CSS_SELECTOR, "select[placeholder='Select a contract type']")
        dropdown = Select(self.driver.find_element(*selector))
        dropdown.select_by_index(1)

    def new_policy_budget_value(self):
        selector = (By.CSS_SELECTOR, "input[name*='refillLimit']")
        return self.driver.find_element(*selector)   
    
    def new_policy_datepicker(self):
        selectorOne = (By.CSS_SELECTOR, "input[placeholder='Start date']")
        selectorTwo = (By.XPATH, "//div[@class='dayContainer']/span")
        today = str(datetime.today().strftime('%B %d, %Y'))
        self.driver.find_element(*selectorOne).click()
        days = self.driver.find_elements(*selectorTwo)
        for day in days: 
            if day.get_attribute("aria-label")==(today):
                day.click()
                break
    
    def new_policy_select_parking(self):
        selector = (By.XPATH, "//h6[.='Parking']")
        selectorTwo = (By.CSS_SELECTOR, "#service-item-1")
        self.driver.find_element(*selector).click()
        self.driver.find_element(*selectorTwo).click()

    def new_policy_select_all_available_users(self):
        selector = (By.XPATH, "(//input[@type='checkbox'])[11]")
        self.driver.find_element(*selector).click()
    
    def new_policy_move_users_to_linked(self):
        selector = (By.CSS_SELECTOR, "i[class='fas fa-chevron-right']")
        self.driver.find_element(*selector).click()

    def new_policy_activate(self):
        selector = (By.XPATH, "//button[.='Activate']")
        self.driver.find_element(*selector).click()

    def new_policy_accept_button(self):
        selector = (By.CSS_SELECTOR, "button[data-testid='confirmModalButton']")
        self.driver.find_element(*selector).click()
    
    def save_policy_as_draft_button(self):
        selector = (By.XPATH, "//button[.='Save as draft']")
        self.driver.find_element(*selector).click()

    def message_saved_as_draft(self):
        selector = (By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")
        return self.driver.find_element(*selector)
