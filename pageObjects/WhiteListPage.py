from selenium.webdriver.common.by import By

class WhiteListPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_charging_tokens_button(self):
        selector = (By.XPATH, "//a[.='Add charging token(s)']")
        self.driver.find_element(*selector).click()

    def confirm_add_button(self):
        selector = (By.XPATH, "//button[.='Add']")
        self.driver.find_element(*selector).click()
    
    def save_add_button(self):
        selector = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector).click()
    
    def whitelist_saved_message(self):
        selector = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector)