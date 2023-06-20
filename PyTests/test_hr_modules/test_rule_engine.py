import time
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.LoginPage import LoginPage
from datetime import datetime
from PyTests.TestData.LoginPageData import LoginPageData
from pageObjects.GeneralObjects import GeneralObjects
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(params=LoginPageData.testhr_login_data)
def login_data(request):
    return request.param

class TestSubModuleOne(BaseClass):
    def test_re_create_ruleset(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Attempting to create a ruleset.")
        newrulesetpage = ruleengineoverview.create_ruleset_button()

        timestamp = str(datetime.now())

        newrulesetpage.ruleset_name_field().send_keys("active test")
        newrulesetpage.ruleset_mobility_policy_dropdown()
        actions = ActionChains(self.driver)
        actions.send_keys("Expense Money" + Keys.ENTER)
        actions.perform()
        newrulesetpage.ruleset_description_field().send_keys("This ruleset was created by an automatic test on" + timestamp)
        newrulesetpage.ruleset_save()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")))
        message = str(newrulesetpage.ruleset_message().text)
        assert "successfully created" in message
        log.info("Succesfully created new ruleset.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        
class TestSubmoduleTwo(BaseClass):
    def test_re_edit_settings_inactive(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Filtering for inactive rulesets.")
        ruleengineoverview.ruleset_filter_inactive()
        time.sleep(1)
        changerulesetpage = ruleengineoverview.ruleset_select_top()
        timestamp = str(datetime.now())
        changerulesetpage.ruleset_name_field().send_keys(Keys.CONTROL, "a")
        changerulesetpage.ruleset_name_field().send_keys(Keys.BACKSPACE)
        changerulesetpage.ruleset_name_field().send_keys("Edited on: " + timestamp)
        log.info("Edited name field.")
        changerulesetpage.ruleset_mobility_policy_field()
        log.info("Edited mobility policy field.")

        actions = ActionChains(self.driver)
        actions.send_keys("OldPolicy" + Keys.ENTER)
        actions.perform()

        changerulesetpage.ruleset_description_field().send_keys(Keys.CONTROL, "a")
        changerulesetpage.ruleset_description_field().send_keys(Keys.BACKSPACE)
        changerulesetpage.ruleset_description_field().send_keys("This ruleset was edited by an automatic test on: " + timestamp)
        log.info("Edited description field.")
        changerulesetpage.ruleset_save_button()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")))
        rulesetsavemessage = str(changerulesetpage.ruleset_save_message().text)
        assert "successfully updated" in rulesetsavemessage
        log.info("Successfully updated ruleset.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        

class TestSubmoduleThree(BaseClass):
    def test_re_activate_ruleset(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Filtering for inactive rulesets.")
        ruleengineoverview.ruleset_filter_inactive()
        time.sleep(1)
        log.info("Opening ruleset.")
        changerulesetpage = ruleengineoverview.ruleset_select_top()
        changerulesetpage.ruleset_activate()
        log.info("Activated ruleset.")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")))
        rulesetactivateemessage = str(changerulesetpage.ruleset_save_message().text)
        assert "ruleset status has successfully been applied" in rulesetactivateemessage
        log.info("Successfully updated ruleset status to 'Active'.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        

class TestSubmoduleFour(BaseClass):
    def test_re_deactivate_ruleset(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Filtering for active rulesets.")
        ruleengineoverview.ruleset_filter_active()
        time.sleep(1)
        log.info("Opening ruleset.")
        changerulesetpage = ruleengineoverview.ruleset_select_top()
        changerulesetpage.ruleset_deactivate()
        log.info("Deactivated ruleset.")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")))
        rulesetactivateemessage = str(changerulesetpage.ruleset_save_message().text)
        assert "ruleset status has successfully been applied" in rulesetactivateemessage
        log.info("Succesfully updated ruleset status to 'Inactive'.")

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        

class TestSubmoduleFive(BaseClass):
    def test_re_create_rule(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Searching for 'active test' ruleset.")
        ruleengineoverview.ruleset_search_bar().send_keys("active test")
        time.sleep(1)
        log.info("Opening ruleset.")
        changerulesetpage = ruleengineoverview.ruleset_select_top()
        changerulesetpage.ruleset_rules_tab()
        log.info("Attempting to create a new rule.")
        changerulesetpage.ruleset_create_rule()
        changerulesetpage.ruleset_new_rule_expense_type()
        actions = ActionChains(self.driver)
        actions.send_keys("Other" + Keys.ENTER)
        actions.perform()
        changerulesetpage.ruleset_new_rule_expense_amount().send_keys("15")
        changerulesetpage.ruleset_new_rule_select_days()
        changerulesetpage.ruleset_new_rule_save()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")))
        rulesetactivateemessage = str(changerulesetpage.ruleset_save_message().text)
        assert "rule has successfully been saved" in rulesetactivateemessage
        log.info("Successfully saved new rule.")
        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        

class TestSubmoduleSix (BaseClass):
    def test_re_activate_deactivate_rule(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Searching for 'active test' ruleset.")
        ruleengineoverview.ruleset_search_bar().send_keys("active test")
        time.sleep(1)
        log.info("Opening ruleset.")
        changerulesetpage = ruleengineoverview.ruleset_select_top()
        changerulesetpage.ruleset_rules_tab()
        changerulesetpage.ruleset_rule_activate()
        log.info("Activated rule.")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "//td/span[.='Active']")))
        changerulesetpage.ruleset_rule_deactivate()
        log.info("Deactivated rule.")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, "(//td/span[.='Inactive'])[1]")))

        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        

class TestSubmoduleSeven(BaseClass):
    def test_re_edit_rule(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        log.info("Searching for 'active test' ruleset.")
        ruleengineoverview.ruleset_search_bar().send_keys("active test")
        time.sleep(1)
        log.info("Opening ruleset.")
        changerulesetpage = ruleengineoverview.ruleset_select_top()
        changerulesetpage.ruleset_rules_tab()
        changerulesetpage.ruleset_rule_edit()
        changerulesetpage.ruleset_rule_days_edit()
        changerulesetpage.ruleset_rule_amount_edit().send_keys(Keys.CONTROL, "a")
        changerulesetpage.ruleset_rule_amount_edit().send_keys(Keys.BACK_SPACE)
        changerulesetpage.ruleset_rule_amount_edit().send_keys("20")
        changerulesetpage.ruleset_new_rule_save()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fade.alert.alert-success.alert-dismissible.show")))
        rulesetactivateemessage = str(changerulesetpage.ruleset_save_message().text)

        changerulesetpage.ruleset_settings_tab()
        changerulesetpage.ruleset_name_field().send_keys(Keys.CONTROL, "a")
        changerulesetpage.ruleset_name_field().send_keys(Keys.BACKSPACE)
        timestamp = str(datetime.now())
        changerulesetpage.ruleset_name_field().send_keys(timestamp)
        changerulesetpage.ruleset_save_button()


        generalobjects = GeneralObjects(self.driver)
        generalobjects.sign_out_button()
        
class TestSubmoduleEight(BaseClass):
    def test_re_filter_rulesets(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")

        loginpage = LoginPage(self.driver)

        loginpage.username_box().send_keys(login_data["account"])
        loginpage.password_box().send_keys(login_data["password"])
        homepage = loginpage.login_button()
        log.info("Succesfully logged in.")
        log.info("Navigating to rule engine page.")
        ruleengineoverview = homepage.menu_label_rule_engine()
        ruleengineoverview.ruleset_filter_active()
        time.sleep(1)
        statusbadges = self.driver.find_elements(By.XPATH, "//td/span")
        for statusbadge in statusbadges:
            assert statusbadge.text == "Active"
        ruleengineoverview.ruleset_filter_reset()
        time.sleep(1)
        ruleengineoverview.ruleset_filter_inactive()
        time.sleep(1)
        statusbadges = self.driver.find_elements(By.XPATH, "//td/span")
        for statusbadge in statusbadges:
            assert statusbadge.text == "Inactive"
    








    
