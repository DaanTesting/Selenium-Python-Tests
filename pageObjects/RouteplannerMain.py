from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class RouteplannerMain:
    def __init__(self, driver):
        self.driver = driver

    def scenario_dropdown(self):
        selector1 = (By.XPATH, "(//select[@class='form-select'])[1]")
        scenariodropdown = Select(self.driver.find_element(*selector1))
        return scenariodropdown
    
    def use_button(self):
        selector1 = (By.XPATH, "//button[.='Use']")
        self.driver.find_element(*selector1).click()

        

