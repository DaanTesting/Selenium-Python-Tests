import datetime
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pageObjects.RouteplannerLogin import RouteplannerLogin
from pageObjects.RouteplannerMain import RouteplannerMain
from PyTests.TestData.LoginPageData import LoginPageData
from utilities.BaseClass import BaseClass


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
        routeplannermain.scenario_dropdown().select_by_visible_text(
            "TestCase1"
        )
        routeplannermain.use_button()
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector1 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[1]",
        )
        transportmethod1 = wait.until(EC.element_to_be_clickable(selector1))
        transportmethod1.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector2 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[2]",
        )

        transportmethod2 = wait.until(EC.element_to_be_clickable(selector2))
        transportmethod2.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector3 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[3]",
        )

        transportmethod3 = wait.until(EC.element_to_be_clickable(selector3))
        transportmethod3.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)

        selector4 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[4]",
        )

        transportmethod4 = wait.until(EC.element_to_be_clickable(selector4))
        transportmethod4.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector5 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[5]",
        )

        transportmethod5 = wait.until(EC.element_to_be_clickable(selector5))
        transportmethod5.click()
        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)

        try:
            selector6 = (
                By.XPATH,
                "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[6]",
            )
            transportmethod6 = wait.until(
                EC.element_to_be_clickable(selector6)
            )
            transportmethod6.click()
        except:
            print("6th option not present")
            pass

        time.sleep(2)

        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'De Lijn']")
        
        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'DonkeyRepublic']") 

        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'BlueBike']")
        

class TestSubModuleTwo(BaseClass):
    def test_routeplanner_testcase2(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        routeplannerlogin = RouteplannerLogin(self.driver)
        routeplannerlogin.username_field().send_keys(login_data["account"])
        routeplannerlogin.password_field().send_keys(login_data["password"])
        routeplannermain = routeplannerlogin.login_button()
        routeplannermain.scenario_dropdown().select_by_visible_text(
            "TestCase2"
        )
        routeplannermain.use_button()
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector1 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[1]",
        )
        transportmethod1 = wait.until(EC.element_to_be_clickable(selector1))
        transportmethod1.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector2 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[2]",
        )

        transportmethod2 = wait.until(EC.element_to_be_clickable(selector2))
        transportmethod2.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector3 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[3]",
        )

        transportmethod3 = wait.until(EC.element_to_be_clickable(selector3))
        transportmethod3.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)

        selector4 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[4]",
        )

        transportmethod4 = wait.until(EC.element_to_be_clickable(selector4))
        transportmethod4.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector5 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[5]",
        )

        transportmethod5 = wait.until(EC.element_to_be_clickable(selector5))
        transportmethod5.click()
        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(2)

        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'De Lijn']")
        
        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'NMBS/SNCB']")
        
        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'Cambio']")
        




class TestSubModuleThree(BaseClass):
    def test_routeplanner_testcase3(self, setup, login_data):
        log = self.get_logger()
        log.info(login_data["account"])
        log.info("Attempting login.")
        routeplannerlogin = RouteplannerLogin(self.driver)
        routeplannerlogin.username_field().send_keys(login_data["account"])
        routeplannerlogin.password_field().send_keys(login_data["password"])
        routeplannermain = routeplannerlogin.login_button()
        routeplannermain.scenario_dropdown().select_by_visible_text(
            "TestCase3"
        )
        routeplannermain.use_button()
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector1 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[1]",
        )
        transportmethod1 = wait.until(EC.element_to_be_clickable(selector1))
        transportmethod1.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector2 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[2]",
        )

        transportmethod2 = wait.until(EC.element_to_be_clickable(selector2))
        transportmethod2.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)
        selector3 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[3]",
        )

        transportmethod3 = wait.until(EC.element_to_be_clickable(selector3))
        transportmethod3.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(1)

        selector4 = (
            By.XPATH,
            "(//i[@class='fa-sharp fa-solid fa-chevron-down'])[4]",
        )

        transportmethod4 = wait.until(EC.element_to_be_clickable(selector4))
        transportmethod4.click()

        time.sleep(1)
        actions.key_down(Keys.END).key_up(Keys.END).perform()
        time.sleep(2)

        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'De Lijn']")
        
        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'NMBS/SNCB']")
        
        assert self.driver.find_elements(By.XPATH, "//tr/td[text() = 'Cambio']")
        

        
