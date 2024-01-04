from selenium.webdriver.common.by import By


class CpoIndividualCustomer:
    def __init__(self, driver):
        self.driver = driver

    def sessions_tab(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Sessions'])")
        self.driver.find_element(*selector1).click()
    
    def top_session_value(self):
        selector1 = (By.XPATH, "//tr[1]/td[8]")
        return self.driver.find_element(*selector1)
    
    def message_banner(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    
    def delete_button(self):
        selector1 = (By.XPATH, "//button[.='Delete']")
        self.driver.find_element(*selector1).click()
