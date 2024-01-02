from selenium.webdriver.common.by import By


class FederalBudgetsPage:
    def __init__(self, driver):
        self.driver = driver

    def budget_management_tab(self):
        selector1 = (By.XPATH, "//button[.='Budget management']")
        self.driver.find_element(*selector1).click()
    
    def budget_creation_tab(self):
        selector1 = (By.XPATH, "//button[.='Budget creation']")
        self.driver.find_element(*selector1).click()