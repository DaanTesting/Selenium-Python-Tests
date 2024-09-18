from selenium.webdriver.common.by import By


class ChargingCardPage:
    def __init__(self, driver):
        self.driver = driver

    def search_field(self):
        selector1 = (By.XPATH, "//input[@placeholder='Search']")
        return self.driver.find_element(*selector1)
    
    def top_status_badge(self):
        selector1 = (By.XPATH, "(//span[@class='status-badge bg-light'])[1]")
        return self.driver.find_element(*selector1)
    
    def processing_tab(self):
        selector1 = (By.XPATH, "//div[contains(text(),'Processing')]")
        self.driver.find_element(*selector1).click()
