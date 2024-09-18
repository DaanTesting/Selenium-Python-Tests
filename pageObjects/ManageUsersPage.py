from selenium.webdriver.common.by import By


class ManageUsersPage:
    def __init__(self, driver):
        self.driver = driver

    def create_user_button(self):
        selector1 = (By.XPATH, "//a[.='Create user']")
        self.driver.find_element(*selector1).click()

    def create_user_email_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-email")
        return self.driver.find_element(*selector1)
    
    def create_user_first_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-first_name")
        return self.driver.find_element(*selector1)

    def create_user_last_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-last_name")
        return self.driver.find_element(*selector1)

    def checkbox_account_admin(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-1-SYS_ADMIN")
        self.driver.find_element(*selector1).click()

    def create_user_save_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector1).click()
    
    def get_newest_user_email(self):
        selector1 = (By.XPATH, "//tr[1]/td[2]/div/div/div")
        return self.driver.find_element(*selector1)

    def user_created_message(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
