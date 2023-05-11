from selenium.webdriver.common.by import By


class ExpensesMainPage:
    def __init__(self, driver):
        self.driver = driver

    def tab_new(self, driver):
        selector1 = (By.XPATH, "//span[text()='New']")
        self.driver.find_element(*selector1).click()

    def tab_all_expenses(self, driver):
        selector1 = (By.XPATH, "//button[text()='All expenses']")
        self.driver.find_element(*selector1).click()

    def sign_out_button(self):
        selector1 = (By.CSS_SELECTOR, "a[title='Sign out']")
        self.driver.find_element(*selector1).click()
