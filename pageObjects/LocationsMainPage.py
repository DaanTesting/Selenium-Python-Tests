from selenium.webdriver.common.by import By

from pageObjects.IndividualChargingLocation import IndividualChargingLocation


class LocationsMainPage:
    def __init__(self, driver):
        self.driver = driver

    def find_location(self):
        selector1 = (By.XPATH, "(//div/input)[1]")
        return self.driver.find_element(*selector1)

    def find_device(self):
        selector1 = (
            By.CSS_SELECTOR,
            "input[placeholder='Serial number, OCPP ID or EVSE ID']",
        )
        return self.driver.find_element(*selector1)

    def find_location_click_top_result(self):
        selector1 = (By.XPATH, "(//tr/td[3]/a[1])[1]")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation
    
    def find_location_customer_click_top_result(self):
        selector1 = (By.XPATH, "(//tr/td[2]/a[1])[1]")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation

    def generate_export(self):
        selector1 = (By.XPATH, "//a[.='» Export']")
        self.driver.find_element(*selector1).click()

    def create_location_button(self):
        selector1 = (By.XPATH, "//a[.='» Create location']")
        self.driver.find_element(*selector1).click()
    
    def create_location_select_customer(self):
        selector1 = (By.XPATH, "(//span[@role='combobox'])[1]")
        selector2 = (By.XPATH, "//li[.='Automated Test Company Main (A00000639)']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def create_location_location_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_name")
        return self.driver.find_element(*selector1)

    def create_location_address(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_ADDRESS")
        return self.driver.find_element(*selector1)
    
    def create_location_postcode(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_POSTCODE")
        return self.driver.find_element(*selector1)
    
    def create_location_town(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_TOWN")
        return self.driver.find_element(*selector1)
    
    def create_location_create_button(self):
        selector1 = (By.XPATH, "//button[.='Create']")
        self.driver.find_element(*selector1).click()
