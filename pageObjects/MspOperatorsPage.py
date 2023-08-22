from selenium.webdriver.common.by import By


class MspOperatorsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def export_service_records_button(self):
        selector1 = (By.XPATH, "//a[contains(.,'Download all service records')]")
        self.driver.find_element(*selector1).click()

    def export_menu_from_field(self):
        selector1 = (By.XPATH, "(//input[@id='id_date_from'])")
        return self.driver.find_element(*selector1)
    
    def export_menu_until_field(self):
        selector1 = (By.XPATH, "(//input[@id='id_date_until'])")
        return self.driver.find_element(*selector1)
    
    def export_all_record_details(self):
        selector1 = (By.CSS_SELECTOR, "#id_export_format_1")
        selector2 = (By.XPATH, "//button[@name='export']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()