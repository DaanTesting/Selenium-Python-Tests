from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def password_box(self):
        selector = (By.CSS_SELECTOR, "#id_password")
        return self.driver.find_element(*selector)

    def username_box(self):
        selector = (By.CSS_SELECTOR, "#id_username")
        return self.driver.find_element(*selector)

    def login_button(self):
        selector = (By.CSS_SELECTOR, 'button[name="login"]')
        self.driver.find_element(*selector).click()
        homepage = HomePage(self.driver)
        return homepage
