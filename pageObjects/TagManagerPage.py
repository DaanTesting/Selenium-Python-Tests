from selenium.webdriver.common.by import By


class TagManagerPage:
    def __init__(self, driver):
        self.driver = driver

    def create_tag_button(self):
        selector1 = (By.XPATH, "//a[.='Create tag']")
        self.driver.find_element(*selector1).click()

    def choose_tag_name_field(self):
        selector1 = (By.CSS_SELECTOR, "input[placeholder='Type your tag name here']")
        return self.driver.find_element(*selector1)

    def select_available_user(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.driver.find_element(*selector1).click()

    def move_all_users_right(self):
        selector1 = (By.XPATH, "(//button[@type='button'])[3]")
        self.driver.find_element(*selector1).click()

    def tag_save_button(self):
        selector1 = (By.XPATH, "//button[.='Save']")
        self.driver.find_element(*selector1).click()

    def message_succes(self):
        selector1 = (
            By.CSS_SELECTOR,
            ".fade.alert.alert-success.alert-dismissible.show",
        )
        return self.driver.find_element(*selector1)

    def delete_tag(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
        self.driver.find_element(*selector1).click()
        selector2 = (By.XPATH, "//small[.='Actions']")
        self.driver.find_element(*selector2).click()
        selector3 = (By.XPATH, "//div/a[text()='Delete']")
        self.driver.find_element(*selector3).click()
        selector4 = (By.XPATH, "//div/button[.='Delete']")
        self.driver.find_element(*selector4).click()

    def page_title(self):
        selector1 = (By.XPATH, "//h1[contains(.,'Tag manager')]")
        return self.driver.find_element(*selector1)

    def edit_tag(self):
        selector1 = (By.XPATH, "(//*[name()='svg'])[2]")
        self.driver.find_element(*selector1).click()
        selector2 = (By.XPATH, "//a[.='View details']")
        self.driver.find_element(*selector2).click()

    def select_all_linked_users(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[12]")
        self.driver.find_element(*selector1).click()
    
    def select_all_linked_users_local(self):
        selector1 = (By.XPATH, "(//input[@type='checkbox'])[2]")
        self.driver.find_element(*selector1).click()

    def unlink_users(self):
        selector1 = (By.XPATH, "(//button[@type='button'])[4]")
        self.driver.find_element(*selector1).click()
