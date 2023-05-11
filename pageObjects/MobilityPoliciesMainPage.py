from selenium.webdriver.common.by import By
from pageObjects.NewMobilityPolicyPage import NewMobilityPolicyPage
from pageObjects.ChangeMobilityPolicyPage import ChangeMobilityPolicyPage

class MobilityPoliciesMainPage:
    def __init__(self, driver):
        self.driver = driver

    def mobility_policies_searchbar(self):
        selector = (By.CSS_SELECTOR, "input[placeholder='Search policies']")
        return self.driver.find_element(*selector)
    
    def mobility_policies_filter_active(self):
        selector = (By.XPATH, "//span[.='Filter']")
        selectorTwo = (By.XPATH, "(//input[@type='checkbox'])[1]")
        selectorThree = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector).click()
        self.driver.find_element(*selectorTwo).click()
        self.driver.find_element(*selectorThree).click()

    def mobility_policies_create_button(self):
        selector = (By.XPATH, "//a[.='Create policy']")
        self.driver.find_element(*selector).click()
        newmobilitypolicypage = NewMobilityPolicyPage(self.driver)
        return newmobilitypolicypage
    
    def mobility_policies_filter_draft(self):
        selector = (By.XPATH, "//span[.='Filter']")
        selectorTwo = (By.XPATH, "(//input[@type='checkbox'])[3]")
        selectorThree = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector).click()
        self.driver.find_element(*selectorTwo).click()
        self.driver.find_element(*selectorThree).click()
    
    def mobility_policies_view_top_policy(self):
        selector = (By.XPATH, "(//*[name()='svg'])[2]")
        selectorTwo = (By.XPATH, "//a[normalize-space()='View']")
        self.driver.find_element(*selector).click()
        self.driver.find_element(*selectorTwo).click()
        changemobilitypolicypage = ChangeMobilityPolicyPage(self.driver)
        return changemobilitypolicypage
    

