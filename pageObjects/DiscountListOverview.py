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
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "(//a[.=' Edit'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        creatediscountlist = CreateDiscountList(self.driver)
        return creatediscountlist
    
    def disable_top_list(self):
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "(//button[.='Disable'])[1]")
        selector3 = (By.CSS_SELECTOR, "#okButton")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def enable_top_list(self):
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "(//form[@id='remove_47'])[1]")
        selector3 = (By.CSS_SELECTOR, "#okButton")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def open_top_list(self):
        selector1 = (By.XPATH, "(//i[@class='fas fa-ellipsis-v'])[1]")
        selector2 = (By.XPATH, "(//a[.=' Show'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        opendiscountlist = OpenDiscountList(self.driver)
        return opendiscountlist

