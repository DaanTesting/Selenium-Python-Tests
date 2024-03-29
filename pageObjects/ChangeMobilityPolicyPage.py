import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ChangeMobilityPolicyPage:
    def __init__(self, driver):
        self.driver = driver

    def change_mobility_policy_activate_draft(self):
        selector1 = (
            By.XPATH,
            "//button[@style='padding: 0px;']",
        )
        selector2 = (By.XPATH, "//a[normalize-space()='Activate']")
        selector3 = (By.CSS_SELECTOR, "button[data-testid='confirmModalButton']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def change_mobility_policy_activation_message(self):
        selector1 = (
            By.CSS_SELECTOR,
            ".fade.alert.alert-success.alert-dismissible.show",
        )
        return self.driver.find_element(*selector1)

    def change_mobility_policy_name_field(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Type your policy name here']")
        return self.driver.find_element(*selector1)
    
    def get_header_checkbox(self, table):
        return table.find_element(By.TAG_NAME, "thead").find_element(By.TAG_NAME, "input")

    def change_mobility_policy_select_all_linked_users(self):
        selector1 = (By.XPATH, "(//div/input[@class='form-check-input'])[14]")
        self.driver.find_element(*selector1).click()

    def change_mobility_policy_select_all_available_users(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[13]")
        self.driver.find_element(*selector1).click()

    def change_mobility_policy_link_all_users(self):
        selector1 = (By.CSS_SELECTOR, "i[class='fa-sharp fa-solid fa-chevron-right']")
        self.driver.find_element(*selector1).click()

    def change_mobility_policy_unlink_all_users(self):
        selector1 = (By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-chevron-left")
        self.driver.find_element(*selector1).click()

    def change_mobility_policy_select_parking(self):
        selector1 = (By.CSS_SELECTOR, "div[title='Parking']")
        selector2 = (By.CSS_SELECTOR, "#service-1")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def change_mobility_policy_select_car_sharing(self):
        selector1 = (By.CSS_SELECTOR, "div[title='Car sharing']")
        selector2 = (By.CSS_SELECTOR, "#service-3")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def change_mobility_policy_select_bike_sharing(self):
        selector1 = (By.CSS_SELECTOR, "div[title='Bike sharing']")
        selector2 = (By.CSS_SELECTOR, "#service-4")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def change_mobility_policy_duplicate(self):
        selector1 = (
            By.XPATH,
            "//button[@style='padding: 0px;']",
        )
        selector2 = (By.XPATH, "(//a[.='Duplicate'])")
        selector3 = (By.XPATH, "(//button[.='Duplicate'])")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
        self.driver.find_element(*selector3).click()

    def change_mobility_policy_save(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def change_mobility_policy_save_as_draft(self):
        selector1 = (By.XPATH, "//button[.='Save as draft']")
        self.driver.find_element(*selector1).click()

    def change_mobility_policy_set_unlimited(self):
        selector1 = (By.XPATH, "//input[@value='unlimited']")
        self.driver.find_element(*selector1).click()
