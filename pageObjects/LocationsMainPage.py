from selenium.webdriver.common.by import By
from pageObjects.IndividualChargingLocation import IndividualChargingLocation

class LocationsMainPage:
    def __init__(self, driver):
        self.driver = driver

    def find_location(self):
        selector = (By.CSS_SELECTOR, "input[placeholder='Name, location or owner']")
        return self.driver.find_element(*selector)
    
    def find_device(self):
        selector = (By.CSS_SELECTOR, "input[placeholder='Serial number']")
        return self.driver.find_element(*selector)
    
    def find_location_click_top_result(self):
        selector = (By.CSS_SELECTOR, "a[href='/co/admin/locations/119/']")
        self.driver.find_element(*selector).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation

