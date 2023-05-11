from selenium.webdriver.common.by import By


class SplitBillingMainPage:
    def __init__(self, driver):
        self.driver = driver

    def reimbursement_policies_tab(self):
        selector1 = (By.XPATH, "//a[text()='Reimbursement policies']")
        self.driver.find_element(*selector1).click()

    def blue_collar_testpolicy(self):
        selector1 = (By.XPATH, "//a[text()='Blue collar']")
        self.driver.find_element(*selector1).click()

    def reimbursement_policy_value_button(self):
        selector1 = (By.CSS_SELECTOR, "button[name='rb-policy-value-form']")
        self.driver.find_element(*selector1).click()

    def reimbursement_policy_new_value_field(self):
        selector1 = (By.CSS_SELECTOR, "#id_value")
        return self.driver.find_element(*selector1)

    def reimbursement_policy_new_value_add(self):
        selector1 = (By.XPATH, "//button[text()='Add']")
        self.driver.find_element(*selector1).click()

    def reimbursement_policy_value_delete(self):
        selector1 = (By.XPATH, "//button[text()='Delete']")
        selector2 = (By.CSS_SELECTOR, "#okButton")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
