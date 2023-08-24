from selenium.webdriver.common.by import By
from pageObjects.NewRulesetPage import NewRulesetPage
from pageObjects.ChangeRulesetPage import ChangeRulesetPage


class RuleEngineOverview:
    def __init__(self, driver):
        self.driver = driver

    def create_ruleset_button(self):
        selector1 = (By.XPATH, "//button[.='Create ruleset']")
        self.driver.find_element(*selector1).click()
        newrulesetpage = NewRulesetPage(self.driver)
        return newrulesetpage

    def ruleset_overview_title(self):
        selector1 = (By.XPATH, "//h1[@class='title-with-button']")
        return self.driver.find_element(*selector1)

    def ruleset_select_top(self):
        selector1 = (By.XPATH, "(//*[name()='path'])[2]")
        selector2 = (By.XPATH, "//a[.='Edit']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        changerulesetpage = ChangeRulesetPage(self.driver)
        return changerulesetpage

    def ruleset_filter_inactive(self):
        selector1 = (By.XPATH, "//button[contains(.,'Filter')]")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[2]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_filter_active(self):
        selector1 = (By.XPATH, "//button[contains(.,'Filter')]")
        selector2 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_search_bar(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Search rulesets']")
        return self.driver.find_element(*selector1)

    def ruleset_filter_reset(self):
        selector1 = (By.XPATH, "//button[contains(.,'Filter')]")
        selector2 = (By.XPATH, "//button[.='Clear filter(s)']")
        selector3 = (By.XPATH, "//button[.='Apply']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def ruleset_sort_alphabet_up(self):
        selector1 = (By.CSS_SELECTOR, ".fa.fa-sort-up.text-primary.fa-stack-1x")
        self.driver.find_element(*selector1).click()

    def ruleset_sort_alphabet_down(self):
        selector1 = (
            By.XPATH,
            "(//span/i[@class='fa fa-sort-down opacity-25 fa-stack-1x'])[1]",
        )
        self.driver.find_element(*selector1).click()
