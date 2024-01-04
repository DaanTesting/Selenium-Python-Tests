from selenium.webdriver.common.by import By


class UserInvitesPage:
    def __init__(self, driver):
        self.driver = driver
    
    def page_title(self):
        selector1 = (By.XPATH, "//h1")
        return self.driver.find_element(*selector1)
