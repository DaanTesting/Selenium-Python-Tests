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
    
    def no_charging_card_tab(self):
        selector1 = (By.XPATH, "//div[text()='No charging card']")
        self.driver.find_element(*selector1).click()

    def get_top_name(self):
        selector1 = (By.XPATH, "(//tr/td[2]/div)[1]")
        return self.driver.find_element(*selector1)
    
    def request_token_for_top_user(self):
        selector1 = (By.XPATH, "(//tr/td/div/button)[1]")
        selector2 = (By.XPATH, "//a[.='Request']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
    
    def generic_message(self):
        selector1 = (By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")
        return self.driver.find_element(*selector1)
