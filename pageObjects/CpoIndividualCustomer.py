from selenium.webdriver.common.by import By
from pageObjects.CpoNewUserForm import CpoNewUserForm

class CpoIndividualCustomer:
    def __init__(self, driver):
        self.driver = driver

    def sessions_tab(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Sessions'])")
        self.driver.find_element(*selector1).click()

    def users_tab(self):
        selector1 = (By.XPATH, "//span[contains(.,'Users')]")
        self.driver.find_element(*selector1).click()
    
    def top_session_value(self):
        selector1 = (By.XPATH, "//tr[1]/td[8]")
        return self.driver.find_element(*selector1)
    
    def message_banner(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
    
    def delete_button(self):
        selector1 = (By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-ellipsis-vertical")
        selector2 = (By.XPATH, "//a[.='Delete']")
        selector3 = (By.XPATH, "//button[.='Delete']")

        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()


    def create_user_button(self):
        selector1 = (By.XPATH, "//a[.='Create user']")
        self.driver.find_element(*selector1).click()
        cpo_new_user_form = CpoNewUserForm(self.driver)
        return cpo_new_user_form
    
    def approve_customer_button(self):
        selector1 = (By.XPATH, "//button[.='Approve customer']")
        self.driver.find_element(*selector1).click()

