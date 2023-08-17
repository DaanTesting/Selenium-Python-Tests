from selenium.webdriver.common.by import By
from pageObjects.IndividualChargingLocation import IndividualChargingLocation


class LocationsMainPage:
    def __init__(self, driver):
        self.driver = driver

    def find_location(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Name, location or owner']")
        return self.driver.find_element(*selector1)

    def find_device(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Serial number, OCPP ID or EVSE ID']")
        return self.driver.find_element(*selector1)

    def find_location_click_top_result(self):
        selector1 = (By.CSS_SELECTOR, "a[href='/co/admin/locations/119/']")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation
    
    def generate_export(self):
        selector1 = (By.XPATH, "//a[.='» Export']")
        self.driver.find_element(*selector1).click()
