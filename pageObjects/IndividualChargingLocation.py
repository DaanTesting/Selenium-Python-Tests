from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class IndividualChargingLocation:
    def __init__(self, driver):
        self.driver = driver

    def edit_button(self):
        selector1 = (By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-ellipsis-vertical")
        selector2 = (By.XPATH, "//a[contains(.,'Edit')]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def location_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_name")
        return self.driver.find_element(*selector1)

    def contact_phone_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_contact_phone")
        return self.driver.find_element(*selector1)

    def contact_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_contact_name")
        return self.driver.find_element(*selector1)

    def update_button(self):
        selector1 = (By.XPATH, "//button[text()='Update']")
        self.driver.find_element(*selector1).click()

    def overview_location_name(self):
        selector1 = (By.CSS_SELECTOR, "div[id='content'] h1")
        return self.driver.find_element(*selector1)

    def overview_contact_phone(self):
        selector1 = (By.XPATH, "//dl[2]/dd[1]")
        return self.driver.find_element(*selector1)

    def overview_contact_name(self):
        selector1 = (By.XPATH, "//dl[2]/dd[2]")
        return self.driver.find_element(*selector1)

    def location_address_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_ADDRESS")
        return self.driver.find_element(*selector1)

    def location_postcode_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_POSTCODE")
        return self.driver.find_element(*selector1)

    def location_town_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_TOWN")
        return self.driver.find_element(*selector1)

    def location_country_field_Netherlands(self):
        selector1 = (By.CSS_SELECTOR, "#id_country")
        dropdown = Select(self.driver.find_element(*selector1))
        dropdown.select_by_visible_text("Netherlands")

    def location_country_field_Belgium(self):
        selector1 = (By.CSS_SELECTOR, "#id_country")
        dropdown = Select(self.driver.find_element(*selector1))
        dropdown.select_by_visible_text("Belgium")
    
    def location_latitude(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_LATITUDE")
        return self.driver.find_element(*selector1)
    
    def location_longitude(self):
        selector1 = (By.CSS_SELECTOR, "#id_latlng_LONGITUDE")
        return self.driver.find_element(*selector1)

    def overview_address(self):
        selector1 = (By.XPATH, "//dl[2]/dd[3]")
        return self.driver.find_element(*selector1)

    def devices_tab(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Devices'])")
        self.driver.find_element(*selector1).click()

    def register_a_new_device(self):
        selector1 = (By.XPATH, "//small[.='Register a new device']")
        self.driver.find_element(*selector1).click()

    def OCPP_ID_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_device-device_number")
        return self.driver.find_element(*selector1)

    def select_contract_dropdown(self):
        selector1 = (By.CSS_SELECTOR, "button[title='---------']")
        selector2 = (By.CSS_SELECTOR, "#bs-select-1-1")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def register_new_device_button(self):
        selector1 = (By.XPATH, "//button[text()='Register']")
        self.driver.find_element(*selector1).click()

    def device_created_alert(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    
    def sessions_tab(self):
        selector1 = (By.XPATH, "//a[@href='#sessions']")
        self.driver.find_element(*selector1).click()
    
    def top_session_value(self):
        selector1 = (By.XPATH, "//tr[1]/td[8]")
        return self.driver.find_element(*selector1)
    
    def open_top_device(self):
        selector1 = (By.XPATH, "//tr/td[2]/div/a")
        self.driver.find_element(*selector1).click()

    def delete_device(self):
        selector1 = (By.XPATH, "//a[@class='btn btn-warning']")
        selector2 = (By.XPATH, "//a[@name='close']")
        selector3 = (By.CSS_SELECTOR, "#no-refund")
        selector4 = (By.CSS_SELECTOR, "#cancel-button")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
        self.driver.find_element(*selector4).click()
    
    def delete_button(self):
        selector1 = (By.XPATH, "//button[.='Delete']")
        self.driver.find_element(*selector1).click()

    def device_deleted_alert(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    
    def device_serial_number(self):
        selector1 = (By.XPATH, "//div[4]/div/p")
        return self.driver.find_element(*selector1)
    
    def new_device_serial_number_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_device-device_number")
        return self.driver.find_element(*selector1)
    
    def pricing_tab(self):
        selector1 = (By.XPATH, "(//li/a/span)[4]")
        self.driver.find_element(*selector1).click()

    def edit_pricing_button(self):
        selector1 = (By.XPATH, "//a[.='Edit pricing']")
        self.driver.find_element(*selector1).click()

    def set_pricing_policy(self):
        selector1 = (By.XPATH, "//input[@name='save']")
        self.driver.find_element(*selector1).click()
    
    def choose_afir_policy(self):
        selector1 = (By.XPATH, "//input[@class='form-check-input'][1]")
        self.driver.find_element(*selector1).click()

    def generic_alert(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    


