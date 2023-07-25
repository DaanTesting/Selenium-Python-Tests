from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class IndividualChargingLocation:
    def __init__(self, driver):
        self.driver = driver

    def edit_button(self):
        selector1 = (By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-ellipsis-vertical")
        selector2 = (By.CSS_SELECTOR, "a[href$='/co/admin/locations/119/edit/']")
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

    def overview_address(self):
        selector1 = (By.XPATH, "//dl[2]/dd[3]")
        return self.driver.find_element(*selector1)

    def devices_tab(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Devices'])")
        self.driver.find_element(*selector1).click()

    def register_a_new_device(self):
        selector1 = (By.XPATH, "//a[.='Register a new device']")
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
