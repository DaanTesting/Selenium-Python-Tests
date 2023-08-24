from selenium.webdriver.common.by import By


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
