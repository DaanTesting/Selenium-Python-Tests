from selenium.webdriver.common.by import By

class CpoFinancePage:
    def __init__(self, driver):
        self.driver = driver

    def invoices_tab(self):
        self.driver.get("https://test.optimile.eu/co/admin/finance/invoices/#/invoices")
    
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

    def top_SB_PR_number(self):
        selector1 = (By.XPATH, "//tr[1]/td[1]")
        return self.driver.find_element(*selector1)
    
    def top_SB_PR_status(self):
        selector1 = (By.XPATH, "(//td/div/span)[1]")
        return self.driver.find_element(*selector1)
    
    def open_top_SB_PR(self):
        selector1 = (By.XPATH, "(//td[1]/div/a)[1]")
        self.driver.find_element(*selector1).click()

    def pay_req_search_field(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Customer, debit note No. or payment request No.']")
        return self.driver.find_element(*selector1)
    
    def view_debit_notes_button(self):
        selector1 = (By.XPATH, "//a[.=' View debit notes']")
        self.driver.find_element(*selector1).click()

    def debit_notes_search_field(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Search...']")
        return self.driver.find_element(*selector1)
    
    def top_SB_DN_status(self):
        selector1 = (By.XPATH, "(//td/div/span)[1]")
        return self.driver.find_element(*selector1)
    
    def open_top_SB_DN(self):
        selector1 = (By.XPATH, "(//td[1]/div/a)[1]")
        self.driver.find_element(*selector1).click()
    
    def revenues_tab(self):
        selector1 = (By.XPATH, "//a[@href='#revenues']")
        self.driver.find_element(*selector1).click()
    
    def revenues_filter_unpaid(self):
        selector1 = (By.XPATH, "(//small[contains(.,'Filter')])[2]")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[23]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
    
    def open_top_host_invoice(self):
        selector1 = (By.XPATH, "(//tr[1]/td/div/a/span)[1]")
        self.driver.find_element(*selector1).click()
    
    def host_invoice_status(self):
        selector1 = (By.XPATH, "(//td/span)[1]")
        return self.driver.find_element(*selector1)
    
    def mark_HI_as_paid(self):
        selector1 = (By.XPATH, "//a[contains(.,'Mark as paid')]")
        self.driver.find_element(*selector1).click()