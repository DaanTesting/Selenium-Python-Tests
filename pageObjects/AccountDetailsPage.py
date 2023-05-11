from selenium.webdriver.common.by import By


class AccountDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def account_details_save_button(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def account_details_updated_message(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
