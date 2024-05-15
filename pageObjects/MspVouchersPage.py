from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MspVouchersPage:
    def __init__(self, driver):
        self.driver = driver

    def generate_export_all(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='Export vouchers']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
