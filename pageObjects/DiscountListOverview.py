from selenium.webdriver.common.by import By
from pageObjects.CreateDiscountList import CreateDiscountList
from pageObjects.OpenDiscountList import OpenDiscountList


class DiscountListOverview:
    def __init__(self, driver):
        self.driver = driver
        
    def new_list_button(self):
        selector1 = (By.XPATH, "//a[contains(.,'New list')]")
        self.driver.find_element(*selector1).click()
        creatediscountlist = CreateDiscountList(self.driver)
        return creatediscountlist
    
    def edit_top_list(self):
        selector1 = (By.XPATH, "(//button[@data-bs-toggle='dropdown'])[2]")
        selector2 = (By.XPATH, "(//a[.=' Edit'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        creatediscountlist = CreateDiscountList(self.driver)
        return creatediscountlist
    
    def edit_second_list(self):
        selector1 = (By.XPATH, "(//button[@data-bs-toggle='dropdown'])[3]")
        selector2 = (By.XPATH, "(//a[.='Edit'])[2]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        creatediscountlist = CreateDiscountList(self.driver)
        return creatediscountlist
    
    def disable_top_list(self):
        selector1 = (By.XPATH, "(//button[@data-bs-toggle='dropdown'])[2]")
        selector2 = (By.XPATH, "(//span[.='Disable'])[1]")
        selector3 = (By.XPATH, "(//button[.='Yes'])[2]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def enable_top_list(self):
        selector1 = (By.XPATH, "(//button[@class='btn btn-default btn-sm cell-btn'])[1]")
        selector2 = (By.XPATH, "//span[.='Enable']")
        selector3 = (By.XPATH, "(//button[.='Yes'])[3]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def open_top_list(self):
        selector1 = (By.XPATH, "(//button[@class='btn btn-default btn-sm cell-btn'])[1]")
        selector2 = (By.XPATH, "(//a[.='Show'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        opendiscountlist = OpenDiscountList(self.driver)
        return opendiscountlist
    
    def open_autotest_list(self):
        selector1 = (By.XPATH, "//a[.=' Automatic Test Discount']")
        self.driver.find_element(*selector1).click()
        opendiscountlist = OpenDiscountList(self.driver)
        return opendiscountlist
    
    def message_banner(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)

