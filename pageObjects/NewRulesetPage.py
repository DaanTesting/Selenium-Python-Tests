from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class NewRulesetPage:
    def __init__(self, driver):
        self.driver = driver

    def ruleset_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#name")
        return self.driver.find_element(*selector1)
    
    def ruleset_mobility_policy_dropdown(self):
        selector1 = (By.CSS_SELECTOR, ".react-select__indicator.react-select__dropdown-indicator.css-1xc3v61-indicatorContainer")
        self.driver.find_element(*selector1).click()
        

    def ruleset_description_field(self):
        selector1 = (By.CSS_SELECTOR, "#description")
        return self.driver.find_element(*selector1)

    def ruleset_save(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def ruleset_message(self):
        selector1 = (By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")
        return self.driver.find_element(*selector1)