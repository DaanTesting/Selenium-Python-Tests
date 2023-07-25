from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class ChangeRulesetPage:
    def __init__(self, driver):
        self.driver = driver
    
    def ruleset_name_field(self):
        selector1 = (By.CSS_SELECTOR, "#name")
        return self.driver.find_element(*selector1)
    
    def ruleset_mobility_policy_field(self):
        selector1 = (By.XPATH, "(//*[name()='svg'][@class='css-8mmkcg'])")
        self.driver.find_element(*selector1).click()

    def ruleset_description_field(self):
        selector1 = (By.CSS_SELECTOR, "#description")
        return self.driver.find_element(*selector1)
    
    def ruleset_save_button(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def ruleset_rules_tab(self):
        selector1 = (By.XPATH, "//button[.='Rules']")
        self.driver.find_element(*selector1).click()

    def ruleset_create_rule(self):
        selector1 = (By.XPATH, "//button[.='Create new rule']")
        self.driver.find_element(*selector1).click()

    def ruleset_new_rule_expense_type(self):
        selector1 = (By.XPATH, "(//*[name()='svg'][@class='css-8mmkcg'])[2]")
        self.driver.find_element(*selector1).click()
    
    def ruleset_new_rule_expense_amount(self):
        selector1 = (By.CSS_SELECTOR, "#maxAmount")
        return self.driver.find_element(*selector1)
    
    def ruleset_new_rule_select_days(self):
        selector1 = (By.XPATH, "//button[.='mo']")
        selector2 = (By.XPATH, "//button[.='tu']")
        selector3 = (By.XPATH, "//button[.='we']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_new_rule_save(self):
        selector1 = (By.XPATH, "(//button[@data-testid='confirmModalButton'])[1]")
        self.driver.find_element(*selector1).click()
    
    def ruleset_activate(self):
        selector1 = (By.XPATH, "(//*[name()='svg'][@class='m-2'])[1]")
        selector2 = (By.XPATH, "//a[.='Activate']")
        selector3 = (By.XPATH, "//button[.='Activate']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_deactivate(self):
        selector1 = (By.XPATH, "(//*[name()='svg'][@class='m-2'])[1]")
        selector2 = (By.XPATH, "//a[.='Deactivate']")
        selector3 = (By.XPATH, "//button[.='Deactivate']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_save_message(self):
        selector1 = (By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")
        return self.driver.find_element(*selector1)
    
    def ruleset_rule_activate(self):
        selector1 = (By.XPATH, "(//*[name()='svg'])[3]")
        selector2 = (By.XPATH, "//a[.='Activate']")
        selector3 = (By.XPATH, "//button[.='Activate']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()
    
    def ruleset_rule_deactivate(self):
        selector1 = (By.XPATH, "(//button[contains(@class,'d-flex align-items-center custom-toggle-button-hidden dropdown-toggle btn btn-invisible btn-sm')])[1]")
        selector2 = (By.XPATH, "//a[.='Deactivate']")
        selector3 = (By.XPATH, "//button[.='Deactivate']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_rule_edit(self):
        selector1 = (By.XPATH, "(//button[contains(@class,'d-flex align-items-center custom-toggle-button-hidden dropdown-toggle btn btn-invisible btn-sm')])[1]")
        selector2 = (By.XPATH, "//a[.='Edit']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def ruleset_rule_days_edit(self):
        selector1 = (By.XPATH, "//button[.='sa']")
        selector2 = (By.XPATH, "//button[.='tu']")
        selector3 = (By.XPATH, "//button[.='th']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_rule_amount_edit(self):
        selector1 = (By.CSS_SELECTOR, "#maxAmount")
        return self.driver.find_element(*selector1)
    
    def ruleset_settings_tab(self):
        selector1 = (By.XPATH, "//button[.='Settings']")
        self.driver.find_element(*selector1).click()



