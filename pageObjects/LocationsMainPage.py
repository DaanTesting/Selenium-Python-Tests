from selenium.webdriver.common.by import By

from pageObjects.IndividualChargingLocation import IndividualChargingLocation


class LocationsMainPage:
    def __init__(self, driver):
        self.driver = driver

    def find_location(self):
        selector1 = (By.XPATH, "//input[@placeholder='Search by device, location or address']")
        return self.driver.find_element(*selector1)

    def find_device(self):
        selector1 = (
            By.XPATH,
            "//input[@placeholder='Search by device, location or address']",
        )
        return self.driver.find_element(*selector1)

    def find_location_click_top_result(self):
        selector1 = (By.XPATH, "(//td/div/a)[1]")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation
    
    def find_location_customer_click_top_result(self):
        selector1 = (By.XPATH, "(//tr/td[2]/a[1])[1]")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation
    
    def find_location_customer_click_main_location(self):
        selector1 = (By.XPATH, "//a[.='Autotesting Main Location']")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation

    def generate_export(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='Excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def create_location_button(self):
        selector1 = (By.XPATH, "//button[.='Create location']")
        self.driver.find_element(*selector1).click()
    
    def create_location_select_customer(self):
        selector1 = (By.XPATH, "(//span[@role='combobox'])[1]")
        selector2 = (By.XPATH, "//li[.='Main Customer Autotesting (A00000002)']")
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
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation

    def click_top_location(self):
        selector1 = (By.XPATH, "//tr/td/div/a[1]")
        self.driver.find_element(*selector1).click()
        individualcharginglocation = IndividualChargingLocation(self.driver)
        return individualcharginglocation
    
    def location_latitude(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_LATITUDE")
        return self.driver.find_element(*selector1)
    
    def location_longitude(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_LONGITUDE")
        return self.driver.find_element(*selector1)
