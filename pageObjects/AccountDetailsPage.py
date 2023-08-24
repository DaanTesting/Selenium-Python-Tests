from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AccountDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def account_details_save_button(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def account_details_updated_message(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)

    def account_details_title(self):
        selector1 = (By.XPATH, "(//h1[normalize-space()='Account details'])[1]")
        return self.driver.find_element(*selector1)

    def account_details_company_type(self):
        selector1 = (By.CSS_SELECTOR, "#id_company_type")
        return self.driver.find_element(*selector1)

    def account_details_VAT_number(self):
        selector1 = (By.CSS_SELECTOR, "#id_vat_number")
        return self.driver.find_element(*selector1)

    def account_details_first_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_first_name")
        return self.driver.find_element(*selector1)

    def account_details_last_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_last_name")
        return self.driver.find_element(*selector1)

    def account_details_emailaddress(self):
        selector1 = (By.CSS_SELECTOR, "#id_email")
        return self.driver.find_element(*selector1)

    def account_details_phone(self):
        selector1 = (By.CSS_SELECTOR, "#id_phone")
        return self.driver.find_element(*selector1)

    def account_details_language_select_english(self):
        selector1 = (
            By.CSS_SELECTOR,
            "button[class*='btn dropdown-toggle btn-default']",
        )
        selector2 = (By.XPATH, "//span[.='English']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def account_details_language_select_nederlands(self):
        selector1 = (
            By.CSS_SELECTOR,
            "button[class*='btn dropdown-toggle btn-default']",
        )
        selector2 = (By.XPATH, "//span[.='Nederlands']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def account_details_address(self):
        selector1 = (By.CSS_SELECTOR, "#id_address")
        return self.driver.find_element(*selector1)

    def account_details_postcode(self):
        selector1 = (By.CSS_SELECTOR, "#id_postcode")
        return self.driver.find_element(*selector1)

    def account_details_town(self):
        selector1 = (By.CSS_SELECTOR, "#id_town")
        return self.driver.find_element(*selector1)

    def account_details_invoice_email(self):
        selector1 = (By.CSS_SELECTOR, "#id_invoice_email")
        return self.driver.find_element(*selector1)
