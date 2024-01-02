from selenium.webdriver.common.by import By



class ReportingPage:
    def __init__(self, driver):
        self.driver = driver

    def page_title(self):
        selector1 = (By.XPATH, "//h1[@class='title-with-button']")
        
    
    def create_report_button(self):
        selector1 = (By.XPATH, "//a[.='Create report']")
        self.driver.find_element(*selector1).click()
    
    def select_report_type(self):
        selector1 = (By.XPATH, "(//div[@class='react-select__input-container css-19bb58m'])[1]")
        self.driver.find_element(*selector1).click()
    
    def create_report_next_button(self):
        selector1 = (By.XPATH, "//button[.='Next']")
        self.driver.find_element(*selector1).click()

    def reporting_period_start(self):
        selector1 = (By.CSS_SELECTOR, "#id_period_0")
        return self.driver.find_element(*selector1)
    
    def reporting_period_end(self):
        selector1 = (By.CSS_SELECTOR, "#id_period_1")
        return self.driver.find_element(*selector1)
    
    def create_report_button_end(self):
        selector1 = (By.XPATH, "//button[.='Create report']")
        self.driver.find_element(*selector1).click()

    def top_report_name(self):
        selector1 = (By.XPATH, "(//tr/td[1])[1]")
        return self.driver.find_element(*selector1)
    
    def download_top_report(self):
        selector1 = (By.XPATH, "(//div[@class='action-btn'])[1]")
        self.driver.find_element(*selector1).click()

    def select_excel_report(self):
        selector1 = (By.CSS_SELECTOR, "button[title='CSV file']")
        selector2 = (By.XPATH, "//a[.='Excel file']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

