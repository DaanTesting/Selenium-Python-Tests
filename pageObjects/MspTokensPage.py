from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MspTokensPage:
    def __init__(self, driver):
        self.driver = driver

    def export_in_use_tokens(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='Excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def export_available_tokens(self):
        selector1 = (By.XPATH, "//a[contains(.,'Available')]")
        selector2 = (By.XPATH, "//button[.='Export']")
        selector3 = (By.XPATH, "//a[.='Excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
