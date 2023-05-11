from selenium.webdriver.common.by import By
from pageObjects.ExpensesMainPage import ExpensesMainPage
from pageObjects.SplitBillingMainPage import SplitBillingMainPage
from pageObjects.MobilityPoliciesMainPage import MobilityPoliciesMainPage
from pageObjects.LocationsMainPage import LocationsMainPage
from pageObjects.MspCustomerPage import MspCustomerPage
from pageObjects.CpoCustomerPage import CpoCustomerPage
from pageObjects.ManageUsersPage import ManageUsersPage
from pageObjects.WhiteListPage import WhiteListPage
from pageObjects.TagManagerPage import TagManagerPage
from pageObjects.AccountDetailsPage import AccountDetailsPage
from pageObjects.HrProfilesOverview import HrProfilesOverview


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def menu_label_expenses(self):
        selector1 = (By.CSS_SELECTOR, 'a[href*="mobility"]')
        selector2 = (By.CSS_SELECTOR, 'a[href*="expenses"]')
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        expensesmainpage = ExpensesMainPage(self.driver)
        return expensesmainpage

    def menu_label_chargingpoints(self):
        selector1 = (By.XPATH, "//span[text()='Charging Points']")
        self.driver.find_element(*selector1).click()

    def menu_label_mobility(self):
        selector1 = (By.XPATH, "//span[text()='Mobility']")
        self.driver.find_element(*selector1).click()

    def menu_label_locations(self):
        selector1 = (By.XPATH, "//span[text()='Locations']")
        self.driver.find_element(*selector1).click()
        locationsmainpage = LocationsMainPage(self.driver)
        return locationsmainpage

    def menu_label_splitbilling(self):
        selector1 = (By.XPATH, "//span[text()='Split billing']")
        self.driver.find_element(*selector1).click()
        splitbillingmainpage = SplitBillingMainPage(self.driver)
        return splitbillingmainpage

    def menu_label_mobility_policies(self):
        selector1 = (By.CSS_SELECTOR, 'a[href*="mobility"]')
        selector2 = (
            By.XPATH,
            "//span[@class='menu-label'][text()='Mobility policies']",
        )
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        mobilitypoliciesmainpage = MobilityPoliciesMainPage(self.driver)
        return mobilitypoliciesmainpage

    def menu_label_msp_customers(self):
        selector1 = (By.XPATH, "(//span[text()='Customers'])[2]")
        self.driver.find_element(*selector1).click()
        mspcustomerpage = MspCustomerPage(self.driver)
        return mspcustomerpage

    def menu_label_cpo_customers(self):
        selector1 = (By.XPATH, "(//span[text()='Customers'])[1]")
        self.driver.find_element(*selector1).click()
        cpocustomerpage = CpoCustomerPage(self.driver)
        return cpocustomerpage

    def menu_label_administration_users(self):
        selector1 = (By.XPATH, "//span[text()='Administration']")
        selector2 = (By.XPATH, "(//span[text()='Users'])[1]")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        manageuserspage = ManageUsersPage(self.driver)
        return manageuserspage

    def menu_label_profiles(self):
        selector1 = (By.XPATH, "//span[contains(normalize-space(),'Profiles')]")
        self.driver.find_element(*selector1).click()

    def menu_label_tag_manager(self):
        selector1 = (
            By.XPATH,
            "(//span[@class='menu-label'][normalize-space()='Tag manager'])",
        )
        self.driver.find_element(*selector1).click()
        tagmanagerpage = TagManagerPage(self.driver)
        return tagmanagerpage

    def menu_label_whitelist(self):
        selector1 = (By.XPATH, "//span[.='Whitelist']")
        self.driver.find_element(*selector1).click()
        whitelistpage = WhiteListPage(self.driver)
        return whitelistpage

    def menu_label_account(self):
        selector1 = (By.XPATH, "//span[.='Account']")
        self.driver.find_element(*selector1).click()

    def menu_label_account_details(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Account details'])[1]")
        self.driver.find_element(*selector1).click()
        accountdetailspage = AccountDetailsPage(self.driver)
        return accountdetailspage

    def menu_label_msp_invoices(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Invoices'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_payment_methods(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Payment methods'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_profiles_overview(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Overview'])[1]")
        self.driver.find_element(*selector1).click()
        profilesoverview = HrProfilesOverview(self.driver)
        return profilesoverview

    def menu_label_import_export(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Import & Export'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_import(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Import'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_administration_hr(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Administration'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_create_report(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Create report'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_msp_tokens(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Tokens'])[2]")
        self.driver.find_element(*selector1).click()

    def menu_label_msp_vouchers(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Vouchers'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_msp_contracts(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Contracts'])[2]")
        self.driver.find_element(*selector1).click()

    def menu_label_msp_operators(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Operators'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_overview(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Overview'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_tokens(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Tokens'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_simcards(self):
        selector1 = (By.XPATH, "(//a[@href='/co/admin/simcards/'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_contracts(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Contracts'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_roaming(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Roaming'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_finance(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Finance'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_reports(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Reports'])[1]")
        self.driver.find_element(*selector1).click()
