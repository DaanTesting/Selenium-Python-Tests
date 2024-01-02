from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class NewRulesetPage:
    def __init__(self, driver):
        self.driver = driver

    def ruleset_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#name")
        return self.driver.find_element(*selector1)

    def ruleset_mobility_policy_dropdown(self):
        selector1 = (By.CSS_SELECTOR, ".react-select__input-container.css-19bb58m")
        self.driver.find_element(*selector1).click()

    def ruleset_description_field(self):
        selector1 = (By.CSS_SELECTOR, "#description")
        return self.driver.find_element(*selector1)

    def ruleset_save(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def ruleset_message(self):
        selector1 = (
            By.CSS_SELECTOR,
            ".fade.alert.alert-success.alert-dismissible.show",
        )
        return self.driver.find_element(*selector1)
