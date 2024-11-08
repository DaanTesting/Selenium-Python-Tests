from selenium.webdriver.common.by import By


class SplitBillingMainPage:
    def __init__(self, driver):
        self.driver = driver

    def reimbursement_policies_button(self):
        selector1 = (By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-ellipsis-vertical")
        selector2 = (By.XPATH, "//a[contains(.,'Reimbursement policies')]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def autotesting_reimbursement(self):
        selector1 = (By.XPATH, "//a[.='Autotesting Reimbursement']")
        self.driver.find_element(*selector1).click()
    
    def open_top_policy(self):
        selector1 = (By.CSS_SELECTOR, "a[href='/co/admin/split-billing/reimbursements/1']")
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
        selector2 = (By.XPATH, "//button[.='Yes']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def generate_export(self):
        selector1 = (By.XPATH, "//button[.='Export']")
        selector2 = (By.XPATH, "//a[.='Export excel']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
