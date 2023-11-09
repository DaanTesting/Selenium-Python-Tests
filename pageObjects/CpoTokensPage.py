from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CpoTokensPage:
    def __init__(self, driver):
        self.driver = driver

    def select_tokens_in_use(self):
        selector1 = (By.XPATH, "//a[contains(.,'In use')]")
        self.driver.find_element(*selector1).click()

    def select_tokens_available(self):
        selector1 = (By.XPATH, "//a[contains(.,'Available')]")
        self.driver.find_element(*selector1).click()

    def download_tokens(self):
        selector1 = (By.XPATH, "//button[.=' Download tokens']")
        self.driver.find_element(*selector1).click()

    def add_token(self):
        selector1 = (By.XPATH, "//a[.='» Add token']")
        self.driver.find_element(*selector1).click()

    def UID_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-0-uid")
        return self.driver.find_element(*selector1)
    
    def select_customer(self):
        selector1 = (By.CSS_SELECTOR, "button[title='---------']")
        selector2 = (By.XPATH, "//span[.='Carrefour (Autotest) (A00000002)']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def save_token_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='save']")
        self.driver.find_element(*selector1).click()

