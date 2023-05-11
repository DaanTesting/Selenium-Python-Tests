from selenium.webdriver.common.by import By
from pageObjects.NewMobilityPolicyPage import NewMobilityPolicyPage
from pageObjects.ChangeMobilityPolicyPage import ChangeMobilityPolicyPage


class MobilityPoliciesMainPage:
    def __init__(self, driver):
        self.driver = driver

    def mobility_policies_searchbar(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Search policies']")
        return self.driver.find_element(*selector1)

    def mobility_policies_filter_active(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def mobility_policies_create_button(self):
        selector1 = (By.XPATH, "//a[.='Create policy']")
        self.driver.find_element(*selector1).click()
        newmobilitypolicypage = NewMobilityPolicyPage(self.driver)
        return newmobilitypolicypage

    def mobility_policies_filter_draft(self):
        selector1 = (By.XPATH, "//span[.='Filter']")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[3]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def mobility_policies_view_top_policy(self):
        selector1 = (By.XPATH, "(//*[name()='svg'])[2]")
        selector2 = (By.XPATH, "//a[normalize-space()='View']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        changemobilitypolicypage = ChangeMobilityPolicyPage(self.driver)
        return changemobilitypolicypage
