from selenium.webdriver.common.by import By

class MspDashboard:
    def __init__(self, driver):
        self.driver = driver
    
    def sessions_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Sessions')]")
        self.driver.find_element(*selector1).click()
    
    def new_registrations_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'New registrations')]")
        self.driver.find_element(*selector1).click()

    def waiting_for_payment_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Waiting for payment')]")
        self.driver.find_element(*selector1).click()
    
    def assign_tokens(self):
        selector1 = (By.XPATH, "//span[contains(.,'Assign tokens')]")
        self.driver.find_element(*selector1).click()

    