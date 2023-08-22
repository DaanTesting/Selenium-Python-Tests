from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MspVouchersPage:
    def __init__(self, driver):
        self.driver = driver

    def generate_export_all(self):
        selector1 = (By.XPATH, "//button[.=' Download as xlsx']")
        self.driver.find_element(*selector1).click()