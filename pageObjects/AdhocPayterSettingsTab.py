import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdhocPayterSettingsTab:
    def __init__(self, driver):
        self.driver = driver

    def starting_price_margin(self):
        selector1 = (By.CSS_SELECTOR, "#id_start_price_margin")
        return self.driver.find_element(*selector1)

    def starting_price_fixed(self):
        selector1 = (By.CSS_SELECTOR, "#id_start_price_fixed")
        return self.driver.find_element(*selector1)

    def hourly_price_margin(self):
        selector1 = (By.CSS_SELECTOR, "#id_hourly_price_margin")
        return self.driver.find_element(*selector1)

    def hourly_price_fixed(self):
        selector1 = (By.CSS_SELECTOR, "#id_hourly_price_fixed")
        return self.driver.find_element(*selector1)

    def kwh_price_margin(self):
        selector1 = (By.CSS_SELECTOR, "#id_kWh_price_margin")
        return self.driver.find_element(*selector1)

    def kwh_price_fixed(self):
        selector1 = (By.CSS_SELECTOR, "#id_kWh_price_fixed")
        return self.driver.find_element(*selector1)
    
    def save_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector1).click()

    def message_alert(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)