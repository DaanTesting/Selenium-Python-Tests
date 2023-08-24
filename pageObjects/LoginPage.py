from selenium.webdriver.common.by import By

from pageObjects.HomePage import HomePage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def password_box(self):
        selector1 = (By.CSS_SELECTOR, "#id_password")
        return self.driver.find_element(*selector1)

    def username_box(self):
        selector1 = (By.CSS_SELECTOR, "#id_username")
        return self.driver.find_element(*selector1)

    def login_button(self):
        selector1 = (By.CSS_SELECTOR, 'button[name="login"]')
        self.driver.find_element(*selector1).click()
        homepage = HomePage(self.driver)
        return homepage
