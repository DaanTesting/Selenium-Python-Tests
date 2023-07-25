import time
import pytest
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.RouteplannerLogin import RouteplannerLogin
from pageObjects.RouteplannerMain import RouteplannerMain
from PyTests.TestData.LoginPageData import LoginPageData

@pytest.fixture(params=LoginPageData.plannertest_data)
def login_data(request):
    return request.param


class TestSubModuleOne(BaseClass):
    def test_routeplanner_testcase1(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        routeplannerlogin = RouteplannerLogin(self.driver)
        routeplannerlogin.username_field().send_keys(login_data["account"])
        routeplannerlogin.password_field().send_keys(login_data["password"])
        routeplannermain = routeplannerlogin.login_button()
        routeplannermain.scenario_dropdown().select_by_visible_text("TestCase1")
        routeplannermain.use_button()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[3]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[4]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[5]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[6]").click()


        time.sleep(15)

class TestSubModuleTwo(BaseClass):
    def test_routeplanner_testcase2(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        routeplannerlogin = RouteplannerLogin(self.driver)
        routeplannerlogin.username_field().send_keys(login_data["account"])
        routeplannerlogin.password_field().send_keys(login_data["password"])
        routeplannermain = routeplannerlogin.login_button()
        routeplannermain.scenario_dropdown().select_by_visible_text("TestCase2")
        routeplannermain.use_button()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[3]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[4]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[5]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[6]").click()

        time.sleep(15)

class TestSubModuleThree(BaseClass):
    def test_routeplanner_testcase3(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        routeplannerlogin = RouteplannerLogin(self.driver)
        routeplannerlogin.username_field().send_keys(login_data["account"])
        routeplannerlogin.password_field().send_keys(login_data["password"])
        routeplannermain = routeplannerlogin.login_button()
        routeplannermain.scenario_dropdown().select_by_visible_text("TestCase3")
        routeplannermain.use_button()
        time.sleep(3)

        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[1]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[2]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[3]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[4]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[5]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[6]").click()
        
        time.sleep(15)