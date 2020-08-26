from PagesObejct.LoginPage import LoginPage


class LoginPageFunctionality:
    def __init__( self, driver):
        self.driver = driver

    def test_validLogin(self, email, password):
        lp = LoginPage(self.driver)
        lp.test_emailTab()
        lp.test_emailId(email)
        lp.test_password(password)
        lp.test_loginButton()
