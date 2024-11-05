from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class CpoRoamingPage:
    def __init__(self, driver):
        self.driver = driver

    def export_prices(self):
        selector1 = (By.XPATH, "(//a[.='Export prices'])[1]")
        self.driver.find_element(*selector1).click()

    def export_cdr(self):
        selector1 = (By.XPATH, "(//button[@class='btn btn-default btn-sm cell-btn'])[1]")
        selector2 = (By.XPATH, '(//li[contains(.,"Export CDR")])[1]')
        selector3 = (By.XPATH, "//input[@id='id_date_from']")
        selector4 = (By.XPATH, "//input[@id='id_date_until']")
        selector5 = (By.XPATH, "//button[.='Export']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        time.sleep(1)
        self.driver.find_element(*selector3).clear()
        self.driver.find_element(*selector3).click()
        self.driver.find_element(*selector3).send_keys("2023-01-01" + Keys.ENTER)
        self.driver.find_element(*selector4).clear()
        self.driver.find_element(*selector4).click()
        self.driver.find_element(*selector4).send_keys("2024-01-01" + Keys.ENTER)
        self.driver.find_element(*selector5).click()
