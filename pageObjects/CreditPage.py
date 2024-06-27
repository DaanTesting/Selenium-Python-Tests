from selenium.webdriver.common.by import By


class CreditPage:
    def __init__(self, driver):
        self.driver = driver

    def add_credit_button(self):
        selector1 = (By.XPATH, "//a[.='Add credit']")
        self.driver.find_element(*selector1).click()
    
    def credit_amount_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_amount")
        return self.driver.find_element(*selector1)
    
    def select_existing_mandate(self):
        selector1 = (By.XPATH, "(//button[@class='btn btn-default'])[1]")
        self.driver.find_element(*selector1).click()
    
    def continue_button(self):
        selector1 = (By.XPATH, "//button[.='Continue']")
        self.driver.find_element(*selector1).click()