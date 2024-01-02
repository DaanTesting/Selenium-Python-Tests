from selenium.webdriver.common.by import By

from pageObjects.AccountDetailsPage import AccountDetailsPage
from pageObjects.CpoCustomerPage import CpoCustomerPage
from pageObjects.CpoReportsPage import CpoReportsPage
from pageObjects.CpoRoamingPage import CpoRoamingPage
from pageObjects.CpoSimCardsPage import CpoSimCardsPage
from pageObjects.CpoTokensPage import CpoTokensPage
from pageObjects.ExpensesMainPage import ExpensesMainPage
from pageObjects.HrProfilesOverview import HrProfilesOverview
from pageObjects.LocationsMainPage import LocationsMainPage
from pageObjects.ManageUsersPage import ManageUsersPage
from pageObjects.MobilityPoliciesMainPage import MobilityPoliciesMainPage
from pageObjects.MspCustomerPage import MspCustomerPage
from pageObjects.MspOperatorsPage import MspOperatorsPage
from pageObjects.MspTokensPage import MspTokensPage
from pageObjects.MspVouchersPage import MspVouchersPage
from pageObjects.RuleEngineOverview import RuleEngineOverview
from pageObjects.SplitBillingMainPage import SplitBillingMainPage
from pageObjects.TagManagerPage import TagManagerPage
from pageObjects.UserDetailPageTest import UserDetailPageTest
from pageObjects.WhiteListPage import WhiteListPage
from pageObjects.DiscountListOverview import DiscountListOverview
from pageObjects.CpoPricingPage import CpoPricingPage
from pageObjects.ProfessionalPoliciesMainPage import ProfessionalPoliciesMainPage
from pageObjects.ReportingPage import ReportingPage
from pageObjects.FederalBudgetsPage import FederalBudgetsPage
from pageObjects.FederalPoliciesPage import FederalPoliciesPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def menu_label_expenses(self):
        selector1 = (By.XPATH, "//span[.='Expenses']")
        self.driver.find_element(*selector1).click()
        expensesmainpage = ExpensesMainPage(self.driver)
        return expensesmainpage

    def menu_label_chargingpoints(self):
        selector1 = (By.XPATH, "//span[text()='Charging Points']")
        self.driver.find_element(*selector1).click()

    def menu_label_mobility(self):
        selector1 = (By.XPATH, "//span[.='Mobility']")
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

    def menu_label_professional_policies(self):
        selector1 = (By.CSS_SELECTOR, 'a[href*="mobility"]')
        selector2 = (
            By.XPATH,
            "//span[.='Professional policies']",
        )
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        professionalpoliciesmainpage = ProfessionalPoliciesMainPage(self.driver)
        return professionalpoliciesmainpage

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

    def menu_label_administration(self):
        selector1 = (By.XPATH, "//span[.='Administration']")
        self.driver.find_element(*selector1).click()

    def menu_label_tag_manager(self):
        selector1 = (
            By.CSS_SELECTOR,
            "div[data-bs-original-title='Tags'] span[class='menu-label']",
        )
        self.driver.find_element(*selector1).click()
        tagmanagerpage = TagManagerPage(self.driver)
        return tagmanagerpage

    def menu_label_whitelist(self):
        selector1 = (By.XPATH, "//span[.='Whitelist']")
        self.driver.find_element(*selector1).click()
        whitelistpage = WhiteListPage(self.driver)
        return whitelistpage

    def menu_label_finance(self):
        selector1 = (By.XPATH, "//span[.='Finance']")
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
        hrprofilesoverview = HrProfilesOverview(self.driver)
        return hrprofilesoverview

    def menu_label_employees(self):
        selector1 = (By.XPATH, "//span[.='Employees']")
        self.driver.find_element(*selector1).click()

    def menu_label_import(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Import'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_administration_hr(self):
        selector1 = (By.XPATH, "//span[.='Administration']")
        self.driver.find_element(*selector1).click()

    def menu_label_create_report(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Create report'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_msp_tokens(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Tokens'])[2]")
        self.driver.find_element(*selector1).click()
        msptokenspage = MspTokensPage(self.driver)
        return msptokenspage

    def menu_label_msp_vouchers(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Vouchers'])[1]")
        self.driver.find_element(*selector1).click()
        mspvoucherspage = MspVouchersPage(self.driver)
        return mspvoucherspage

    def menu_label_msp_contracts(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Contracts'])[2]")
        self.driver.find_element(*selector1).click()

    def menu_label_msp_operators(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Operators'])[1]")
        self.driver.find_element(*selector1).click()
        mspoperatorspage = MspOperatorsPage(self.driver)
        return mspoperatorspage

    def menu_label_cpo_overview(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Overview'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_tokens(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Tokens'])[1]")
        self.driver.find_element(*selector1).click()
        cpotokenspage = CpoTokensPage(self.driver)
        return cpotokenspage

    def menu_label_cpo_simcards(self):
        selector1 = (By.XPATH, "(//a[@href='/co/admin/simcards/'])[1]")
        self.driver.find_element(*selector1).click()
        cposimcardspage = CpoSimCardsPage(self.driver)
        return cposimcardspage

    def menu_label_cpo_contracts(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Contracts'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_roaming(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Roaming'])[1]")
        self.driver.find_element(*selector1).click()
        cporoamingpage = CpoRoamingPage(self.driver)
        return cporoamingpage

    def menu_label_cpo_finance(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Finance'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_cpo_reports(self):
        selector1 = (By.XPATH, "(//span[normalize-space()='Reports'])[1]")
        self.driver.find_element(*selector1).click()
        cporeportspage = CpoReportsPage(self.driver)
        return cporeportspage

    def menu_label_preferences(self):
        selector1 = (
            By.XPATH,
            "(//span[contains(@class,'menu-label')][normalize-space()='Preferences'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_users(self):
        selector1 = (
            By.XPATH,
            "(//span[@class='menu-label'][normalize-space()='Users'])[1]",
        )
        self.driver.find_element(*selector1).click()
        userdetailpagetest = UserDetailPageTest(self.driver)
        return userdetailpagetest

    def menu_label_external_users(self):
        selector1 = (By.XPATH, "(//span[.='External users'])[1]")
        self.driver.find_element(*selector1).click()

    def menu_label_user_invites(self):
        selector1 = (
            By.XPATH,
            "(//span[@class='menu-label'][normalize-space()='User invites'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_invoices(self):
        selector1 = (
            By.XPATH,
            "(//span[contains(@class,'menu-label')][normalize-space()='Invoices'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_credit(self):
        selector1 = (
            By.XPATH,
            "(//span[contains(@class,'menu-label')][normalize-space()='Credit'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_revenue(self):
        selector1 = (
            By.XPATH,
            "(//span[contains(@class,'menu-label')][normalize-space()='Revenue'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_payment_requests(self):
        selector1 = (
            By.XPATH,
            "(//span[@class='menu-label'][normalize-space()='Payment requests'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_debit_notes(self):
        selector1 = (
            By.XPATH,
            "(//span[@class='menu-label'][normalize-space()='Debit notes'])[1]",
        )
        self.driver.find_element(*selector1).click()

    def menu_label_rule_engine(self):
        selector1 = (By.XPATH, "//span[.='Rule engine']")
        self.driver.find_element(*selector1).click()
        ruleengineoverview = RuleEngineOverview(self.driver)
        return ruleengineoverview
    
    def menu_label_discount_lists(self):
        selector1 = (By.XPATH, "//span[.='Discount lists']")
        self.driver.find_element(*selector1).click()
        discountlistoverview = DiscountListOverview(self.driver)
        return discountlistoverview
    
    def menu_label_cpo_pricing(self):
        selector1 = (By.XPATH, "//span[.='Pricing']")
        self.driver.find_element(*selector1).click()
        cpopricingpage = CpoPricingPage(self.driver)
        return cpopricingpage
    
    def menu_label_reporting(self):
        selector1 = (By.XPATH, "//span[@class='menu-label'][contains(.,'Reporting')]")
        self.driver.find_element(*selector1).click()
        reportingpage = ReportingPage(self.driver)
        return reportingpage
    
    def menu_label_federal_budgets(self):
        selector1 = (By.XPATH, "//span[.='Federal budgets']")
        self.driver.find_element(*selector1).click()
        federalbudgetspage = FederalBudgetsPage(self.driver)
        return federalbudgetspage             
    
    def menu_label_federal_policies(self):
        selector1 = (By.XPATH, "//span[.='Federal policies']")
        self.driver.find_element(*selector1).click()
        federalpoliciespage = FederalPoliciesPage(self.driver)
        return federalpoliciespage


