from selenium.webdriver.common.by import By

class CpoFinancePage:
    def __init__(self, driver):
        self.driver = driver

    def invoices_tab(self):
        self.driver.get("https://test.optimile.eu/co/admin/finance/invoices/#/invoices")

    def revenues_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Revenues')]")
        self.driver.find_element(*selector1).click()
    
    def debit_notes_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Debit notes')]")
        self.driver.find_element(*selector1).click()

    def payment_requests_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Payment requests')]")
        self.driver.find_element(*selector1).click()

    def invoices_search_field(self):
        selector1 = (By.XPATH, "//input[@placeholder='Number or customer']")
        return self.driver.find_element(*selector1)
    
    def invoices_top_invoice(self):
        selector1 = (By.XPATH, "(//td/div/a)[1]")
        self.driver.find_element(*selector1).click()
        
    def process_invoice_button(self):
        selector1 = (By.XPATH, "//button[contains(.,'Process invoice')]")
        self.driver.find_element(*selector1).click()

    def set_invoice_number(self):
        selector1 = (By.CSS_SELECTOR, "#id_invoice_number")
        return self.driver.find_element(*selector1)
    
    def set_invoice_number_confirm(self):
        selector1 = (By.XPATH, "//button[.='Update']")
        self.driver.find_element(*selector1).click()

    def invoice_tab_search(self):
        selector1 = (By.XPATH, "//input[@placeholder='Number or customer']")
        return self.driver.find_element(*selector1)
    
    def invoice_tab_open_top_invoice(self):
        selector1 = (By.XPATH, "(//td/div/a)[1]")
        self.driver.find_element(*selector1).click()

    def close_invoice(self):
        selector1 = (By.XPATH, "//a[contains(.,'Close invoice')]")
        selector2 = (By.XPATH, "//button[.='Close invoice']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def top_invoice_status(self):
        selector1 = (By.XPATH, "(//td/div/span)[1]")
        return self.driver.find_element(*selector1)
    
    def overview_invoice_tab(self):
        selector1 = (By.XPATH, "(//a[contains(.,'Invoices')])[2]")
        self.driver.find_element(*selector1).click()

    def invoices_set_filter_unprocessed_open(self):
        selector1 = (By.XPATH, "//small[contains(.,'Filter')]")
        selector2 = (By.XPATH, "(//div/input)[28]")
        selector3 = (By.XPATH, "(//div/input)[29]")
        selector4 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
        self.driver.find_element(*selector4).click()

    def payreqs_set_filter_open(self):
        selector1 = (By.XPATH, "(//small[.='Filter'])[2]")
        selector2 = (By.XPATH, "(//div/input)[24]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
