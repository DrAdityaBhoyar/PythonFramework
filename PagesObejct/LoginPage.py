from selenium.webdriver.common.by import By


class LoginPage:
    def __init__( self, driver):
        self.driver = driver

    # Locators
    _emailTab_ = (By.CSS_SELECTOR, ".email-tab")
    _emailId_ = (By.ID, "signin_username")
    _password_ = (By.ID, "signin_password")
    _loginButton_ = (By.XPATH, "//input[@id='enter-button-location']")

    def test_emailTab(self):
        return self.driver.find_element(*LoginPage._emailTab_).click()

    def test_emailId(self, emailId):
        return self.driver.find_element(*LoginPage._emailId_).send_keys(emailId)

    def test_password(self, password):
        return self.driver.find_element(*LoginPage._password_).send_keys(password)

    def test_loginButton(self):
        return self.driver.find_element(*LoginPage._loginButton_).click()

