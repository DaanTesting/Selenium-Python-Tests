from selenium.webdriver.common.by import By

class CpoOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def issues_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Issues')]")
        self.driver.find_element(*selector1).click()

    def export_issues_csv_button(self):
        selector1 = (By.XPATH, "//button[contains(.,'Export')]")
        selector2 = (By.XPATH, "//a[.='CSV']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def sessions_tab(self):
        selector1 = (By.XPATH, "//a[@href='#sessions']")
        self.driver.find_element(*selector1).click()

    def open_activate_contract_table(self):
        selector1 = (By.XPATH, "(//i[@class='fa-sharp fa-solid fa-magnifying-glass'])[1]")
        self.driver.find_element(*selector1).click()

    def activate_top_contract(self):
        selector1 = (By.XPATH, "(//button[.='Activate'])[1]")
        self.driver.find_element(*selector1).click()
    
    def alert(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
