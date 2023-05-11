from selenium.webdriver.common.by import By


class WhiteListPage:
    def __init__(self, driver):
        self.driver = driver

    def add_charging_tokens_button(self):
        selector1 = (By.XPATH, "//a[.='Add charging token(s)']")
        self.driver.find_element(*selector1).click()

    def confirm_add_button(self):
        selector1 = (By.XPATH, "//button[.='Add']")
        self.driver.find_element(*selector1).click()

    def save_add_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector1).click()

    def whitelist_saved_message(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
