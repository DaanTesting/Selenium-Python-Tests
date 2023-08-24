import time
from datetime import date

import pytest
from pageObjects.GeneralObjects import GeneralObjects
from pageObjects.LoginPage import LoginPage
from PyTests.TestData.LoginPageData import LoginPageData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param


class TestOne(BaseClass):
    def test_expenses_DownloadAttachment_HRmod(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")

        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        log.info("Attempting to download attachment.")
        expensesmainpage.driver.find_element(By.XPATH, "(//div/button)[3]").click()
        expensesmainpage.driver.find_element(By.PARTIAL_LINK_TEXT, "attachment").click()

        time.sleep(2)
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        assert Message == "The file was downloaded successfully."
        log.info("Succesfully downloaded attachment.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTwo(BaseClass):
    def test_expenses_verify_overview(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        overviewtitle = str(expensesmainpage.expenses_title_all_expenses().text)
        assert overviewtitle == "All expenses"
        log.info("Succesfully verified expenses overview-page.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestThree(BaseClass):
    def test_expenses_detail_modal(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.expenses_open_top_expense_detail_modal()
        expensesmainpage.expenses_detailmodal_show_details()
        log.info("Succesfully opened expense detail modal.")
        time.sleep(1)
        idtag1 = str(expensesmainpage.expenses_detailmodal_idtag().text)
        assert idtag1 != ""
        expensesmainpage.expenses_detailmodal_next()
        time.sleep(1)
        idtag2 = str(expensesmainpage.expenses_detailmodal_idtag().text)
        assert idtag2 != ""

        assert idtag1 != idtag2
        log.info("Succesfully scrolled between expenses.")
        log.info("Closing detail modal.")
        expensesmainpage.expenses_detailmodal_close()

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFour(BaseClass):
    def test_expenses_detail_modal_attachment_scroll(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        time.sleep(1)
        expensesmainpage.expenses_main_searchbar().send_keys("13513")
        log.info("Succesfully searched for expense with ID 13513.")
        time.sleep(1)
        expensesmainpage.expenses_open_top_expense_detail_modal()
        time.sleep(1)
        expensesmainpage.expenses_detailmodal_attachment_scroll()
        log.info("Succesfully scrolled between various attachments.")

        expensesmainpage.expenses_detailmodal_close()

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestFive(BaseClass):
    def test_expenses_SearchByID_HRmod(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()

        expensesmainpage.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Search expenses']"
        ).send_keys("13423")
        log.info("Searched for expense with ID 13423.")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//td/div/div/button")))

        self.driver.find_element(By.XPATH, "//td/div/div/button").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "details").click()
        log.info("Opened expense detail modal.")
        self.driver.find_element(
            By.CSS_SELECTOR, ".btn-muted-small.collapse-button.btn.btn-light"
        ).click()
        Result = self.driver.find_element(By.CSS_SELECTOR, ".id-tag").get_attribute(
            "innerHTML"
        )

        assert Result == "13423"
        log.info("Succesfully verified expense ID.")

        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Close']").click()

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSix(BaseClass):
    def test_expenses_SearchByType_HRmod(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        time.sleep(1)
        expensesmainpage.driver.find_element(
            By.CSS_SELECTOR, "input[placeholder='Search expenses']"
        ).send_keys("Taxi")
        log.info("Searched for expense type 'taxi'.")

        time.sleep(1)

        Expenses = self.driver.find_elements(By.XPATH, "//tbody/tr")
        for Expense in Expenses:
            assert self.driver.find_element(By.XPATH, "//td[5]").text == "Taxi"

        log.info("Succesfully verified that only taxi-expenses are visible.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestSeven(BaseClass):
    def test_expenses_DenyUndo_HRmod(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.tab_all_expenses(self.driver)
        time.sleep(1)
        expensesmainpage.tab_new(self.driver)
        log.info("Navigating to new expenses tab.")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//tbody/tr/td/div/div/button)[1]").click()
        time.sleep(1)

        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Show details']"
        ).click()

        self.driver.find_element(By.XPATH, "(//input[@type='radio'])[2]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply changes']").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
        log.info("Marked expense as 'denied'.")
        log.info("Navigating towards pending-tab.")
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//span[text()='Pending']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//tbody/tr/td/div/div/button)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Undo']").click()
        log.info("Undo expense.")

        time.sleep(2)

        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        assert "was updated successfully and is now marked as 'new'" in Message
        log.info("Succesfully marked expense as 'new'.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEight(BaseClass):
    def test_expenses_ApproveUndo_HRmod(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.tab_all_expenses(self.driver)
        time.sleep(1)
        expensesmainpage.tab_new(self.driver)
        time.sleep(1)
        log.info("Navigating to new expenses tab.")

        self.driver.find_element(By.XPATH, "(//tbody/tr/td/div/div/button)[1]").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "//a[normalize-space()='Show details']"
        ).click()
        log.info("Opening expense detail modal.")

        self.driver.find_element(By.XPATH, "(//input[@type='radio'])[1]").click()
        self.driver.find_element(By.XPATH, "//button[text()='Apply changes']").click()
        log.info("Marked expense as 'approved'.")

        # Move to pending tab to verify presence of expense
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()

        time.sleep(1)

        self.driver.find_element(By.XPATH, "//span[text()='Pending']").click()
        log.info("Navigating to pending expenses tab.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//tbody/tr/td/div/div/button)[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[.='Undo']").click()
        log.info("Undo expense.")

        time.sleep(3)
        Message = self.driver.find_element(
            By.XPATH, "//div[@class='fade alert alert-success alert-dismissible show']"
        ).text

        assert "was updated successfully and is now marked as 'new'" in Message
        log.info("Succesfully marked expense as 'new'.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestNine(BaseClass):
    def test_expenses_verify_error_tab(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        expensesmainpage.expenses_tab_error()
        log.info("Navigating to error tab.")
        time.sleep(1)
        statusbadge = str(self.driver.find_element(By.XPATH, "//tr/td[.='Error']").text)
        assert statusbadge == "Error"
        log.info(
            "Succesfully verified that only expenses marked as 'error' are present."
        )

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestTen(BaseClass):
    def test_expenses_date_picker(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR, ".fa-sharp.fa-solid.fa-calendar"
        ).click()
        expensesmainpage.expenses_datepicker_field().send_keys(
            "2023-05-16 to 2023-05-17"
        )
        expensesmainpage.expenses_datepicker_field().send_keys(Keys.ENTER)
        log.info("Selected date range in datepicker.")
        time.sleep(2)
        expensedates = self.driver.find_elements(By.XPATH, "//tr/td[3]")
        for expensedate in expensedates:
            assert str(expensedate.text) == "2023-05-17"

        log.info(
            "Succesfully verified that all expenses fall within correct date range."
        )

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()


class TestEleven(BaseClass):
    def test_expenses_status_filter(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting Login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to expenses-page.")
        homepage.menu_label_mobility()
        expensesmainpage = homepage.menu_label_expenses()

        expensesmainpage.expenses_filter_paid()
        log.info("Filtering expenses for 'paid'-status.")
        time.sleep(5)
        statustags = self.driver.find_elements(By.XPATH, "//tr/td[6]")
        for statustag in statustags:
            assert str(statustag.text) == "Paid"

        log.info("Succesfully verified that only 'Paid' expenses are present.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
