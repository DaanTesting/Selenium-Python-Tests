import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.AdhocPaymentPageTab import AdhocPaymentPageTab
from pageObjects.AdhocPayterSettingsTab import AdhocPayterSettingsTab


class AdhocPlatformPage:
    def __init__(self, driver):
        self.driver = driver

    def payment_page_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Payment page')]")
        self.driver.find_element(*selector1).click()
        paymentpagetab = AdhocPaymentPageTab(self.driver)
        return paymentpagetab
    
    def web_settings_tab(self):
        selector1 = (By.XPATH, "//a[@href='#web']")
        self.driver.find_element(*selector1).click()
        paymentpagetab = AdhocPaymentPageTab(self.driver)
        return paymentpagetab
    
    def payter_settings_tab(self):
        selector1 = (By.XPATH, "//a[@href='#payter']")
        self.driver.find_element(*selector1).click()
        paytersettingstab = AdhocPayterSettingsTab(self.driver)
        return paytersettingstab
    
    def export_button_excel(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='Excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def export_button_csv(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='CSV']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def search_bar(self):
        selector1 = (By.XPATH, "//div/input")
        return self.driver.find_element(*selector1)
    
    def filter_adhoc(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[2]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def filter_direct(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def filter_payment_page(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[3]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def filter_payter(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[4]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def filter_clear(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "//button[.='Clear filter(s)']")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()