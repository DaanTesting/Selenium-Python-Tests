from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform


class GeneralObjects:
    def __init__(self, driver):
        self.driver = driver

    def sign_out_button(self):
        selector1 = (By.CSS_SELECTOR, "button[title='Sign out']")
        self.driver.find_element(*selector1).click()

    def open_new_tab(self):
        selector1 = (By.CSS_SELECTOR, "body")
        if platform.system() == 'Darwin':
            self.driver.find_element(*selector1).send_keys(Keys.COMMAND + 't')
        else:
            self.driver.find_element(*selector1).send_keys(Keys.CONTROL + 't')