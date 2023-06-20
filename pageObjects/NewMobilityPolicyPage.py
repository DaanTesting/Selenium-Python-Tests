from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import datetime
import time


class NewMobilityPolicyPage:
    def __init__(self, driver):
        self.driver = driver

    def new_policy_name_field(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Type your policy name here']")
        return self.driver.find_element(*selector1)

    def new_policy_type_dropdown(self):
        selector1 = (By.CSS_SELECTOR, "select[name='type']")
        dropdown = Select(self.driver.find_element(*selector1))
        dropdown.select_by_index(0)

    def new_policy_contract_dropdown(self):
        selector1 = (By.CSS_SELECTOR, "select[placeholder='Select a contract type']")
        dropdown = Select(self.driver.find_element(*selector1))
        dropdown.select_by_index(1)

    def new_policy_budget_value(self):
        selector1 = (By.CSS_SELECTOR, "input[name*='refillLimit']")
        return self.driver.find_element(*selector1)
    
    #comment: This method of navigating the datepicker has been deprecated because of inconsistencies.
    #def new_policy_datepicker(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Start date']")
        selector2 = (By.XPATH, "//div[@class='flatpickr-days']/div/span")
        today = str(datetime.datetime.today().strftime("%B%e, %Y"))
        self.driver.find_element(*selector1).click()
        days = self.driver.find_elements(*selector2)
        time.sleep(1)
        for day in days:
                if day.get_attribute("aria-label") == today:
                    day.click()
                    break

    def new_policy_datepicker_alt(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Start date']")
        return self.driver.find_element(*selector1)

    def new_policy_select_parking(self):
        selector1 = (By.XPATH, "//h6[.='Parking']")
        selector2 = (By.CSS_SELECTOR, "#service-item-1")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def new_policy_select_all_available_users(self):
        selector1 = (By.XPATH, "(//div/input[contains(@type,'checkbox')])[12]")
        return self.driver.find_element(*selector1)

    def new_policy_move_users_to_linked(self):
        selector1 = (By.CSS_SELECTOR, "i[class='fas fa-chevron-right']")
        self.driver.find_element(*selector1).click()

    def new_policy_activate(self):
        selector1 = (By.XPATH, "//button[.='Activate']")
        self.driver.find_element(*selector1).click()

    def new_policy_accept_button(self):
        selector1 = (By.CSS_SELECTOR, "button[data-testid='confirmModalButton']")
        self.driver.find_element(*selector1).click()

    def save_policy_as_draft_button(self):
        selector1 = (By.XPATH, "//button[.='Save as draft']")
        self.driver.find_element(*selector1).click()

    def message_saved_as_draft(self):
        selector1 = (
            By.CSS_SELECTOR,
            ".fade.alert.alert-success.alert-dismissible.show",
        )
        return self.driver.find_element(*selector1)
