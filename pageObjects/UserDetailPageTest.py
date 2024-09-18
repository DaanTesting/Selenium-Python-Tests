from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserDetailPageTest:
    def __init__(self, driver):
        self.driver = driver

    def user_detail_open_top_user(self):
        selector1 = (By.XPATH, "(//button[@data-testid='dropdown-show-options'])[3]")
        selector2 = (By.XPATH, "//a[.='View']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def user_detail_first_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-first_name")
        return self.driver.find_element(*selector1)

    def user_detail_last_name(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-last_name")
        return self.driver.find_element(*selector1)

    def user_detail_email(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-email")
        return self.driver.find_element(*selector1)

    def user_detail_phone(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-phone")
        return self.driver.find_element(*selector1)

    def user_detail_language_select_nederlands(self):
        selector1 = (
            By.CSS_SELECTOR,
            "button[class$='btn dropdown-toggle btn-default']",
        )
        selector2 = (By.XPATH, "//span[.='Nederlands']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def user_detail_language_select_english(self):
        selector1 = (
            By.CSS_SELECTOR,
            "button[class$='btn dropdown-toggle btn-default']",
        )
        selector2 = (By.XPATH, "//span[.='English']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def user_detail_address(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-address")
        return self.driver.find_element(*selector1)

    def user_detail_postcode(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-postcode")
        return self.driver.find_element(*selector1)

    def user_detail_town(self):
        selector1 = (By.CSS_SELECTOR, "#id_user-town")
        return self.driver.find_element(*selector1)

    def user_detail_country_select_belgium(self):
        selector1 = (By.XPATH, "//button[@data-id='id_user-country']")
        self.driver.find_element(*selector1).send_keys("Belgium" + Keys.ENTER)

    def user_detail_country_select_netherlands(self):
        selector1 = (By.XPATH, "//button[@data-id='id_user-country']")
        self.driver.find_element(*selector1).send_keys("Netherlands" + Keys.ENTER)

    def user_detail_role_select_accountadmin(self):
        selector1 = (By.CSS_SELECTOR, "#id_permissions-SYS_ADMIN")
        self.driver.find_element(*selector1).click()

    def user_detail_notification_settings(self):
        selector1 = (By.CSS_SELECTOR, "#id_privacy-allow_direct_marketing")
        selector2 = (By.CSS_SELECTOR, "#id_privacy-send_reimbursement_updates")
        self.driver.find_element(*selector1).click
        self.driver.find_element(*selector2).click

    def user_detail_save_button(self):
        selector1 = (By.CSS_SELECTOR, "button[class='btn btn-primary']")
        self.driver.find_element(*selector1).click()

    def user_detail_update_message(self):
        selector1 = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        return self.driver.find_element(*selector1)
