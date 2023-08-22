from selenium.webdriver.common.by import By

class CpoReportsPage:
    def __init__(self, driver):
        self.driver = driver

    def export_excel(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-filter-export")
        selector2 = (By.XPATH, "//a[.='Excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def export_csv(self):
        selector1 = (By.CSS_SELECTOR, "#id_form-filter-export")
        selector2 = (By.XPATH, "//a[.='CSV']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        

