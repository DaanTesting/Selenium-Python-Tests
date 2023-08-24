from selenium.webdriver.common.by import By


class CpoSimCardsPage:
    def __init__(self, driver):
        self.driver = driver

    def generate_export(self):
        selector1 = (By.XPATH, "//button[@name='export']")
        self.driver.find_element(*selector1).click()
