from selenium.webdriver.common.by import By
import time

class ExpensesMainPage:
    def __init__(self, driver):
        self.driver = driver

    def tab_new(self, driver):
        selector1 = (By.XPATH, "//span[text()='New']")
        self.driver.find_element(*selector1).click()

    def tab_all_expenses(self, driver):
        selector1 = (By.XPATH, "//button[text()='All expenses']")
        self.driver.find_element(*selector1).click()
        
    def expenses_tab_error(self):
        selector1 = (By.XPATH, "//span[.='Error']")
        self.driver.find_element(*selector1).click()

    def sign_out_button(self):
        selector1 = (By.CSS_SELECTOR, "a[title='Sign out']")
        self.driver.find_element(*selector1).click()
    
    def expenses_title_all_expenses(self):
        selector1 = (By.XPATH, "//button[.='All expenses']")
        return self.driver.find_element(*selector1)
    
    def expenses_open_top_expense_detail_modal(self):
        selector1 = (By.XPATH, "(//div/div/button)[2]")
        selector2 = (By.XPATH, "(//a[@role='button'][normalize-space()='Show details'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
    
    def expenses_detailmodal_show_details(self):
        selector1 = (By.XPATH, "//button[.='Show details']")
        self.driver.find_element(*selector1).click()

    def expenses_detailmodal_idtag(self):
        selector1 = (By.CSS_SELECTOR, ".id-tag")
        return self.driver.find_element(*selector1)
    
    def expenses_detailmodal_close(self):
        selector1 = (By.XPATH, "//button[@class='btn-close']")
        self.driver.find_element(*selector1).click()
    
    def expenses_detailmodal_next(self):
        selector1 = (By.XPATH, "//button[.='Next']")
        self.driver.find_element(*selector1).click()
    
    def expenses_detailmodal_attachment_scroll(self):
        selector1 = (By.CSS_SELECTOR, "i[class='fa-sharp fa-solid fa-chevron-right']")
        selector2 = (By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-chevron-left")
        self.driver.find_element(*selector1)
        self.driver.find_element(*selector2)
    
    def expenses_main_searchbar(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Search expenses']")
        return self.driver.find_element(*selector1)
    
    def expenses_datepicker_field(self):
        selector1 = (By.CSS_SELECTOR, "input[class='text-muted border-end-0 form-control flatpickr-input active']")
        return self.driver.find_element(*selector1)
    
    def expenses_filter_paid(self):
        selector1 = (By.CSS_SELECTOR, "button[class='d-flex align-items-center gap-2 btn btn-default']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[3]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        time.sleep(1)
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
