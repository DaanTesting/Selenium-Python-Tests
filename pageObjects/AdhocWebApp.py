from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdhocWebApp:
    def __init__(self, driver):
        self.driver = driver

    def get_adhoc__web_app(self, driver):
        self.driver.get("https://test.optimile.eu/co/adhoc/?d=ADHOCREMOTE")

    def open_pricing(self):
        selector1 = (By.XPATH, "//small[.='Pricing']")
        self.driver.find_element(*selector1).click()

    
