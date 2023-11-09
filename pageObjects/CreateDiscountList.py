from selenium.webdriver.common.by import By


class CreateDiscountList:
    def __init__(self, driver):
        self.driver = driver

    def name_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_discount_list-name")
        return self.driver.find_element(*selector1)

    def discount_percentage_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_config-discount_percentage")
        return self.driver.find_element(*selector1)

    def selection_charging_points_button(self):
        selector1 = (
            By.CSS_SELECTOR,
            "#id_config-apply_to_all_charging_points_0",
        )
        self.driver.find_element(*selector1).click()

    def all_charging_points_button(self):
        selector1 = (
            By.CSS_SELECTOR,
            "#id_config-apply_to_all_charging_points_0",
        )
        self.driver.find_element(*selector1).click()
    
    def create_button(self):
        selector1 = (By.XPATH, "//button[contains(.,'Create')]")
        self.driver.find_element(*selector1).click()

    def update_button(self):
        selector1 = (By.CSS_SELECTOR, "button[value='update']")
        self.driver.find_element(*selector1).click()
