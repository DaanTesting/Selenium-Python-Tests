import time
import pytest
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects


@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_expenses_DownloadAttachment_HRmod(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()

        expensesmainpage = homepage.menu_label_expenses()

        expensesmainpage.driver.find_element(By.XPATH, "(//div/button)[3]").click()
        expensesmainpage.driver.find_element(By.PARTIAL_LINK_TEXT, "attachment").click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='fade alert alert-success alert-dismissible show']",
                )
            )
        )
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        assert Message == "The file was downloaded successfully."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_expenses_SearchByID_HRmod(self, setup, login_data):

        log = self.get_logger()

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()

        expensesmainpage = homepage.menu_label_expenses()

        expensesmainpage.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Search expenses']"
        ).send_keys("13423")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//td/div/div/button")))

        self.driver.find_element(By.XPATH, "//td/div/div/button").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "details").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn-muted-small.collapse-button.btn.btn-light"
        ).click()
        Result = self.driver.find_element(By.CSS_SELECTOR, ".id-tag").get_attribute(
            "innerHTML"
        )

        print(Result)
        assert Result == "13423"

        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close']").click()
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_expenses_SearchByType_HRmod(self, setup, login_data):

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()

        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Search expenses']"
        ).send_keys("Taxi")

        time.sleep(1)

        Expenses = self.driver.find_elements(By.XPATH, "//tbody/tr")
        for Expense in Expenses:
            assert self.driver.find_element(By.XPATH, "//td[5]").text == "Taxi"

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_expenses_DenyUndo_HRmod(self, setup, login_data):

        log = self.get_logger()

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()

        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.tab_all_expenses(self.driver)
        time.sleep(1)
        expensesmainpage.tab_new(self.driver)
        time.sleep(1)

        self.driver.find_element(By.XPATH, "(//tbody/tr/td/div/div/button)[1]").click()
        time.sleep(1)

        # Open and decline an expense

        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Show details']"
        ).click()

        self.driver.find_element(By.XPATH, "(//input[@type='radio'])[2]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply changes']").click()

        # Move to pending tab to verify presence of expense
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()

        time.sleep(1)

        self.driver.find_element(By.XPATH, "//span[text()='Pending']").click()
        self.driver.find_element(By.XPATH, "//tbody/tr/td/div/div/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Undo']").click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='fade alert alert-success alert-dismissible show']",
                )
            )
        )
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        print(Message)

        assert Message == "Expense was updated successfully and is now marked as new."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

    def test_expenses_ApproveUndo_HRmod(self, setup, login_data):

        log = self.get_logger()

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()

        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.tab_all_expenses(self.driver)
        time.sleep(1)
        expensesmainpage.tab_new(self.driver)
        time.sleep(1)

        self.driver.find_element(By.XPATH, "(//tbody/tr/td/div/div/button)[1]").click()
        time.sleep(1)

        # Open and decline an expense

        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Show details']"
        ).click()

        self.driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply changes']").click()

        # Move to pending tab to verify presence of expense
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()

        time.sleep(1)

        self.driver.find_element(By.XPATH, "//span[text()='Pending']").click()
        self.driver.find_element(By.XPATH, "//tbody/tr/td/div/div/button").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Undo']").click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='fade alert alert-success alert-dismissible show']",
                )
            )
        )
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        print(Message)

        assert Message == "Expense was updated successfully and is now marked as new."

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()

