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
