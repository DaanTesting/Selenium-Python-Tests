from selenium.webdriver.common.by import By


class GeneralObjects:
    def __init__(self, driver):
        self.driver = driver

    def sign_out_button(self):
        selector1 = (By.CSS_SELECTOR, "a[title='Sign out']")
        self.driver.find_element(*selector1).click()