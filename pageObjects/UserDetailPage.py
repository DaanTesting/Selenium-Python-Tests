from selenium.webdriver.common.by import By


class UserDetailPage:
    def __init__(self, driver):
        self.driver = driver

    def userdetail_verify_presence_personal_elements(self):
        selector1 = (By.XPATH, "//div[.='Auto 10 User 10']")
        selector2 = (By.XPATH, "//h5[.='User info']")
        selector3 = (By.XPATH, "//span[.='DETAILS']")
        selector4 = (By.XPATH, "//span[.='SUSPENSION']")
        selector5 = (By.XPATH, "//span[.='CONTACT']")
        selector6 = (By.XPATH, "//div[.='Mobility policies']")
        selector7 = (By.XPATH, "//h5[.='Tags']")

        titlename = self.driver.find_element(*selector1).text
        assert titlename == "Auto 10 User 10"
        titleuserinfo = self.driver.find_element(*selector2).text
        assert titleuserinfo == "User info"
        subtitledetails = self.driver.find_element(*selector3).text
        assert subtitledetails == "DETAILS"
        subtitlesuspension = self.driver.find_element(*selector4).text
        assert subtitlesuspension == "SUSPENSION"
        subtitlecontact = self.driver.find_element(*selector5).text
        assert subtitlecontact == "CONTACT"
        titlemobilitypolicies = self.driver.find_element(*selector6).text
        assert titlemobilitypolicies == "Mobility policies"
        titletags = self.driver.find_element(*selector7).text
        assert titletags == "Tags"

    def userdetail_select_employment_tab(self):
        selector1 = (
            By.XPATH,
            "//button[@class='custom-toggle-button dropdown-toggle btn btn-default']",
        )
        selector2 = (By.XPATH, "//a[.='Employment']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def userdetail_select_financialinfo_tab(self):
        selector1 = (
            By.XPATH,
            "//button[@class='custom-toggle-button dropdown-toggle btn btn-default']",
        )
        selector2 = (By.XPATH, "//a[.='Financial info']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def userdetail_select_securex_tab(self):
        selector1 = (
            By.XPATH,
            "//button[@class='custom-toggle-button dropdown-toggle btn btn-default']",
        )
        selector2 = (By.XPATH, "//a[.='Securex']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()

    def userdetail_verify_presence_employment_elements(self):
        selector1 = (By.XPATH, "//span[.='CONTRACT']")

        subtitlecontract = self.driver.find_element(*selector1).text
        assert subtitlecontract == "CONTRACT"

    def userdetail_verify_presence_financialinfo_elements(self):
        selector1 = (By.XPATH, "//span[.='PERSONAL BANK INFO']")
        selector2 = (By.XPATH, "//span[.='FINANCE INFO']")
        subtitlebank = self.driver.find_element(*selector1).text
        assert subtitlebank == "PERSONAL BANK INFO"
        subtitlefinanceinfo = self.driver.find_element(*selector2).text
        assert subtitlefinanceinfo == "FINANCE INFO"

    def userdetail_verify_presence_securex_elements(self):
        selector1 = (By.XPATH, "//span[.='DETAILS']")
        selector2 = (By.XPATH, "//span[.='ID INFO']")
        subtitledetails = self.driver.find_element(*selector1).text
        assert subtitledetails == "DETAILS"
        subtitleIDinfo = self.driver.find_element(*selector2).text
        assert subtitleIDinfo == "ID INFO"

    def userdetail_next_previous(self):
        selector1 = (By.XPATH, "//a[.='Next']")
        selector2 = (By.XPATH, "//a[.='Prev']")
        selector3 = (By.CSS_SELECTOR, ".title-with-button")
        self.driver.find_element(*selector1).click()
        titlename = self.driver.find_element(*selector3).text
        assert titlename != "Auto 10 User 10"
        self.driver.find_element(*selector2).click()

    def userdetail_return_to_overview(self):
        selector1 = (By.CSS_SELECTOR, "a[class='breadcrumb-item']")
        self.driver.find_element(*selector1).click()

    def profile_overview_view_profile(self):
        selector1 = (By.XPATH, "(//*[name()='svg'])[2]")
        selector2 = (By.XPATH, "//a[.='View']")
        self.driver.find_element(*selector1).click()
        self.driver.find_element(*selector2).click()
