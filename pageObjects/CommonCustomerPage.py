import time
from selenium.webdriver.common.by import By
from pageObjects.MspIndividualCustomer import MspIndividualCustomer
from pageObjects.CpoIndividualCustomer import CpoIndividualCustomer
from pageObjects.CreateCustomerPage import CreateCustomerPage


class CommonCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def search_by_name_field(self):
        selector1 = (
            By.CSS_SELECTOR,
            "input[placeholder='Name, email, phone, or internal code']",
        )
        return self.driver.find_element(*selector1)

    def click_on_top_result_customer(self):
        selector1 = (By.XPATH, "//tr/td/div/div/a")
        self.driver.find_element(*selector1).click()
        mspindividualcustomer = MspIndividualCustomer(self.driver)
        return mspindividualcustomer

    def click_on_main_flow_account(self):
        selector1 = (By.XPATH, "//a[.='Main Customer Autotesting']")
        self.driver.find_element(*selector1).click()
        mspindividualcustomer = MspIndividualCustomer(self.driver)
        return mspindividualcustomer

    def generate_mobility_customers_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download customers']")
        self.driver.find_element(*selector1).click()
        time.sleep(1)
        self.driver.find_element(*selector2).click()

    def generate_mobility_users_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download users']")
        self.driver.find_element(*selector1).click()
        time.sleep(1)
        self.driver.find_element(*selector2).click()

    def generate_all_customers_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download customers']")
        self.driver.find_element(*selector1).click()
        time.sleep(3)
        self.driver.find_element(*selector2).click()

    def generate_all_users_export(self):
        selector1 = (By.XPATH, "//small[.='Export']")
        selector2 = (By.XPATH, "//a[.='Download users']")
        self.driver.find_element(*selector1).click()
        time.sleep(3)
        self.driver.find_element(*selector2).click()

    def page_title(self):
        selector1 = (By.XPATH, "//h1")
        return self.driver.find_element(*selector1)

    def search_by_name_field(self):
        selector1 = (
            By.CSS_SELECTOR,
            "input[placeholder='Name, email, phone, or internal code']",
        )
        return self.driver.find_element(*selector1)

    def click_on_top_result_customer(self):
        selector1 = (By.XPATH, "//tr[1]/td/div/div/a")
        self.driver.find_element(*selector1).click()
        cpoindividualcustomer = CpoIndividualCustomer(self.driver)
        return cpoindividualcustomer

    def click_on_top_result(self):
        selector1 = (By.XPATH, "//tr[1]/td/div/div/a")
        self.driver.find_element(*selector1).click()
        cpoindividualcustomer = CpoIndividualCustomer(self.driver)
        return cpoindividualcustomer

    def generate_all_customer_report(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='Excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
    
    def create_customer_button(self):
        selector1 = (By.XPATH, "//button[.='Create customer']")
        self.driver.find_element(*selector1).click()
        createcustomerpage = CreateCustomerPage(self.driver)
        return createcustomerpage
    
    def pending_contracts_button(self):
        selector1 = (By.XPATH, "//button[.='Actions']")
        selector2 = (By.XPATH, "//a[.='Pending contracts']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def activate_top_pending_contract(self):
        selector1 = (By.XPATH, "(//button[.='Activate'])[1]")
        self.driver.find_element(*selector1).click()
    
    def message_banner(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    
    def active_customers_filter(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def new_customer_filter(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[24]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def pending_customer_filter(self):
        selector1 = (By.XPATH, "//a[contains(.,'Pending customers')]")
        self.driver.find_element(*selector1).click()

    def blocked_customer_filter(self):
        selector1 = (By.XPATH, "//a[contains(.,'Blocked customers')]")
        self.driver.find_element(*selector1).click()

    def approve_customer(self):
        selector1 = (By.XPATH, "//button[.='Accept']")
        self.driver.find_element(*selector1).click()

    def activate_customer(self):
        selector1 = (By.XPATH, "//button[.='Activate']")
        self.driver.find_element(*selector1).click()
