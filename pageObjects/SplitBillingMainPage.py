from selenium.webdriver.common.by import By

class SplitBillingMainPage:
    def __init__(self, driver):
        self.driver = driver

    def reimbursement_policies_tab(self):
        selector = (By.XPATH, "//a[text()='Reimbursement policies']")
        self.driver.find_element(*selector).click()
    
    def blue_collar_testpolicy(self):
        selector = (By.XPATH, "//a[text()='Blue collar']")
        self.driver.find_element(*selector).click()

    def reimbursement_policy_value_button(self):
        selector = (By.CSS_SELECTOR, "button[name='rb-policy-value-form']")
        self.driver.find_element(*selector).click()
    
    def reimbursement_policy_new_value_field(self):
        selector = (By.CSS_SELECTOR, "#id_value")
        return self.driver.find_element(*selector)

    def reimbursement_policy_new_value_add(self):
        selector = (By.XPATH, "//button[text()='Add']")
        self.driver.find_element(*selector).click()
        
    def reimbursement_policy_value_delete(self):
        selector = (By.XPATH, "//button[text()='Delete']")
        selectorTwo = (By.CSS_SELECTOR, "#okButton")
        self.driver.find_element(*selector).click()
        self.driver.find_element(*selectorTwo).click()
