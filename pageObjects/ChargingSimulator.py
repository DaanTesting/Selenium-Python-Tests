from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime, timedelta


class ChargingSimulator:
    def __init__(self, driver):
        self.driver = driver

    def open_simulator(self):
        self.driver.get("https://test.optimile.eu/sim/")

    def OCPP_ID_Field(self):
        selector1 = (By.CSS_SELECTOR, "#ocppIdentity")
        return self.driver.find_element(*selector1)

    def mode_select_dropdown(self):
        selector1 = (By.CSS_SELECTOR, "#mode")
        dropdown = Select(self.driver.find_element(*selector1))
        dropdown.select_by_visible_text("Manual OCPP 1.6")

    def connect_button(self):
        selector1 = (By.CSS_SELECTOR, "#connect")
        self.driver.find_element(*selector1).click()

    def request_dropdown_start(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class$='dropdown-toggle']").click()
        self.driver.find_element(By.XPATH, "//li[8]").click()

    def connector_id_field(self):
        selector1 = (By.XPATH, "//input[@id='BrutusinForms#7_0']")
        return self.driver.find_element(*selector1)

    def id_tag_field(self):
        selector1 = (By.XPATH, "//input[@id='BrutusinForms#7_1']")
        return self.driver.find_element(*selector1)

    def meter_start_field(self):
        selector1 = (By.XPATH, "//input[@id='BrutusinForms#7_2']")
        return self.driver.find_element(*selector1)

    def start_transaction_button(self):
        selector1 = (By.CSS_SELECTOR, "#submit-cp-StartTransaction")
        self.driver.find_element(*selector1).click()

    def get_transaction_id(self):
        selector1 = (By.XPATH, '//*[@id="log"]/div[1]')
        result_list = []

        ResultStartTransaction = self.driver.find_elements(*selector1)
        for result in ResultStartTransaction:
            result_list.append(result.text)

        transaction_id = 0

        for finalresult in result_list:
            split_list = finalresult.split(": ")
            transaction_id = int(split_list[1].split(",")[0])

        return transaction_id

    def request_dropdown_stop(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class$='dropdown-toggle']").click()
        self.driver.find_element(By.XPATH, "//li[10]").click()

    def id_tag_field_stop(self):
        selector1 = (By.XPATH, "//input[@id='BrutusinForms#9_0']")
        return self.driver.find_element(*selector1)

    def meter_stop_field(self):
        selector1 = (By.XPATH, "//input[@id='BrutusinForms#9_1']")
        return self.driver.find_element(*selector1)

    def transaction_id_field(self):
        selector1 = (By.XPATH, "//input[@id='BrutusinForms#9_3']")
        return self.driver.find_element(*selector1)

    def timestamp_add_hour(self):
        timestamp_field = self.driver.find_element(
            By.XPATH, "//input[@id='BrutusinForms#9_2']"
        )
        timestamp_value = timestamp_field.get_attribute("value")
        timestamp_field.clear()
        dt = datetime.fromisoformat(timestamp_value[:-1])
        dt += timedelta(hours=1)
        new_timestamp_value = dt.isoformat() + "Z"
        timestamp_field.send_keys(new_timestamp_value)

    def reason_dropdown_evdisconnected(self):
        selector1 = (By.XPATH, "(//select[@id='BrutusinForms#9_4'])")
        dropdown = Select(self.driver.find_element(*selector1))
        dropdown.select_by_visible_text("EVDisconnected")

    def stop_transaction_button(self):
        selector1 = (By.CSS_SELECTOR, "#submit-cp-StopTransaction")
        self.driver.find_element(*selector1).click()
