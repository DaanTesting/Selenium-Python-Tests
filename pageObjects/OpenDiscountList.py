from selenium.webdriver.common.by import By

class OpenDiscountList:
    def __init__(self, driver):
        self.driver = driver

    def add_charging_token_button(self):
        selector1 = (By.XPATH, "//a[.='Add charging token(s)']")
        self.driver.find_element(*selector1).click()

    def add_token_button(self):
        selector1 = (By.XPATH, "//button[.='Add']")
        self.driver.find_element(*selector1).click()
    
    def token_description_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_description")
        return self.driver.find_element(*selector1)
    
    def save_charging_token_to_discount_list_button(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()
    
    def delete_top_token(self):
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "//span[.='Remove']")
        selector3 = (By.XPATH, "(//button[.='Yes'])[2]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
    
    def edit_top_token(self):
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "(//a[.='Edit'])[2]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def update_token_in_discount_list_button(self):
        selector1 = (By.XPATH, "//button[.='Update']")
        self.driver.find_element(*selector1).click()

    def export_tokens_button(self):
        selector1 = (By.XPATH, "//a[.='Export tokens']")
        self.driver.find_element(*selector1).click()
    
    def charging_points_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Charging points')]")
        self.driver.find_element(*selector1).click()

    def edit_charging_points_button(self):
        selector1 = (By.XPATH, "//a[.='Edit charging points']")
        self.driver.find_element(*selector1).click()

    def link_all_charging_points_to_discount(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        selector2 = (By.XPATH, "(//button[@class='dual-table-add-item btn btn-default'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def unlink_all_charging_points_from_discount(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[2]")
        selector2 = (By.XPATH, "(//button[@class='dual-table-remove-item btn btn-default'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        
    def charging_point_save_button(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def add_external_token_button(self):
        selector1 = (By.XPATH, "//button[.='External token']")
        self.driver.find_element(*selector1).click()

    def external_token_uid_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_uid")
        return self.driver.find_element(*selector1)
    
    def remove_top_token_from_discount(self):
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "//li[.='Remove']")
        selector3 = (By.XPATH, "(//button[.='Yes'])[2]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def message_banner(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    



    

    
