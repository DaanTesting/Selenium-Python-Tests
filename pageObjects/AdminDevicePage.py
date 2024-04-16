import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.AdhocPaymentPageTab import AdhocPaymentPageTab


class AdminDevicePage:
    def __init__(self, driver):
        self.driver = driver
    
    