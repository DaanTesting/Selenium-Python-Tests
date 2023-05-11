from selenium.webdriver.common.by import By


class ManageUsersPage:
    def __init__(self, driver):
        self.driver = driver
    
    def create_user_button(self):
        selector = (By.XPATH, "//a[text()='Create user']")
        self.driver.find_element(*selector).click()
    
    def create_user_email_field(self):
        selector = (By.CSS_SELECTOR, "#id_form-0-email")
        return self.driver.find_element(*selector)
    
    def checkbox_account_admin(self):
        selector = (By.CSS_SELECTOR, "#id_form-1-roles_0")
        self.driver.find_element(*selector).click()

    def create_user_save_button(self):
        selector = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector).click()
    
    def user_created_message(self):
        selector = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector)

