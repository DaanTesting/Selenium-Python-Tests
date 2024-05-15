from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdhocWebApp:
    def __init__(self, driver):
        self.driver = driver

    def get_adhoc_web_app(self):
        self.driver.get("https://test.optimile.eu/co/adhoc/?d=ADHOCREMOTE")
    
    def get_local_adhoc_web_app(self):
        self.driver.get("http://localhost:8000/co/adhoc/?d=ADHOCREMOTE")

    def open_pricing(self):
        selector1 = (By.XPATH, "//small[.='Pricing']")
        self.driver.find_element(*selector1).click()

    def price_per_hour(self):
        selector1 = (By.XPATH, "//div[contains(text(),'€0.00 / h')]")
        return self.driver.find_element(*selector1)
    
    def start_price(self):
        selector1 = (By.XPATH, "(//div[@class='d-flex justify-content-between py-2 border-bottom'])[1]")
        return self.driver.find_element(*selector1)
