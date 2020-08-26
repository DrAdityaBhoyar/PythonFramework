from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _connect_ = (By.CSS_SELECTOR, "div[class='as-nav-item as-nav-connect']")
    _calendar_ = (By.LINK_TEXT, "Calendar")

    def test_connectMenu(self):
        return self.driver.find_element(*HomePage._connect_).click()

    def test_calendarPage(self):
        return self.driver.find_element(*HomePage._calendar_).click()




