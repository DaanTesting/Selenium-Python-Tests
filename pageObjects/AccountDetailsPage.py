from selenium.webdriver.common.by import By

class AccountDetailsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def account_details_save_button(self):
        selector = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector).click()

    def account_details_updated_message(self):
        selector = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector)