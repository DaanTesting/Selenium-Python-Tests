from selenium.webdriver.common.by import By


class HrProfilesOverview:
    def __init__(self, driver):
        self.driver = driver

    def profile_overview_checkbox_all_users(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.driver.find_element(*selector1).click()
    
    def profile_overview_actions_button_invite(self):
        selector1 = (By.XPATH, "//span[.='Actions']")
        selector2 = (By.XPATH, "//a[.='Send app invite']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def profile_overview_message(self):
        selector1 = (By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")
        return self.driver.find_element(*selector1)





