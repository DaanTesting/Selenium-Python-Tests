from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ApiDoc:
    def __init__(self, driver):
        self.driver = driver

    def doc_request_param_bar(self):
        selector1 = (By.CSS_SELECTOR, ".request-param")
        return self.driver.find_element(*selector1)