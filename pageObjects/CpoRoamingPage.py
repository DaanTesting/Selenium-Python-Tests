from selenium.webdriver.common.by import By

class CpoRoamingPage:
    def __init__(self, driver):
        self.driver = driver

    def export_prices(self):
        selector1 = (By.XPATH, "(//a[@class='btn btn-default btn-xs'][normalize-space()='Export prices'])[22]")
        self.driver.find_element(*selector1).click()
    
    def export_cdr(self):
        selector1 = (By.XPATH, "//a[@href='/co/admin/roaming/1/cdrs/']")
        selector3 = (By.XPATH, "//button[.='Export']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector3).click()