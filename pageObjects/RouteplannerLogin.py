from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from pageObjects.RouteplannerMain import RouteplannerMain


class RouteplannerLogin:
    def __init__(self, driver):
        self.driver = driver

    def username_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_username")
        return self.driver.find_element(*selector1)

    def password_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_password")
        return self.driver.find_element(*selector1)

    def login_button(self):
        selector1 = (By.CSS_SELECTOR, "button[type='submit']")
        self.driver.find_element(*selector1).click()
        routeplannermain = RouteplannerMain(self.driver)
        return routeplannermain
