from selenium.webdriver.common.by import By


class CpoIndividualCustomer:
    def __init__(self, driver):
        self.driver = driver

    def sessions_tab(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Sessions'])")
        self.driver.find_element(*selector1).click()