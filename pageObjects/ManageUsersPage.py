from selenium.webdriver.common.by import By


class ManageUsersPage:
    def __init__(self, driver):
        self.driver = driver

    def create_user_button(self):
        selector1 = (By.XPATH, "//a[text()='Create user']")
        self.driver.find_element(*selector1).click()

    def create_user_email_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-email")
        return self.driver.find_element(*selector1)

    def checkbox_account_admin(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-1-SYS_ADMIN")
        self.driver.find_element(*selector1).click()

    def create_user_save_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector1).click()

    def user_created_message(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
