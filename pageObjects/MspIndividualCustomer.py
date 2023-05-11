from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MspIndividualCustomer:
    def __init__(self, driver):
        self.driver = driver

    def activity_tab(self):
        selector = (By.XPATH, "//span[normalize-space()='Activity']")
        self.driver.find_element(*selector).click()
    
    def contracts_tab(self):
        selector = (By.XPATH, "(//span[contains(text(),'Contracts')])[3]")
        self.driver.find_element(*selector).click()
    
    def create_contract_button(self):
        selector = (By.XPATH, "//a[.='Create contract']")
        self.driver.find_element(*selector).click()
    
    def create_contract_select_formula_freepostpaid(self):
        selector = (By.XPATH, "(//button[@title='---------'])[1]")
        selector2 = (By.CSS_SELECTOR, "a[id='bs-select-1-2']")
        self.driver.find_element(*selector).click()
        self.driver.find_element(*selector2).click()
    
    def create_contract_select_user(self):
        selector = (By.CSS_SELECTOR, "#id_user")
        selectuserdropdown = Select(self.driver.find_element(*selector))
        return selectuserdropdown
        

    def create_contract_create_button(self):
        selector = (By.XPATH, "//button[@name='create']")
        self.driver.find_element(*selector).click()

    def message_contract_created(self):
        selector = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector)
    
    def tokens_tab(self):
        selector = (By.XPATH, "//a[@href='#tokens']")
        self.driver.find_element(*selector).click()
    
    def add_first_token(self):
        selector = (By.XPATH, "(//a[normalize-space()='Add token'])[1]")
        self.driver.find_element(*selector).click()

    def assign_token(self):
        selector = (By.CSS_SELECTOR, "form[id='assign_token'] button[name='save']")
        self.driver.find_element(*selector).click()

    def message_token_assigned(self):
        selector = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector)
    
    def mail_tab(self):
        selector = (By.XPATH, "//a[@href='#mail']")
        self.driver.find_element(*selector).click()
    
    def select_top_emailadress(self):
        selector = (By.XPATH, "//tr[3]/td[2]")
        return self.driver.find_element(*selector)

