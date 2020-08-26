from selenium.webdriver.common.by import By


class CalendarViewPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _monthView_ = (By.XPATH, "//div[text()='month']")
    _weekView_ = (By.XPATH, "//div[text()='week']")
    _dayView_ = (By.XPATH, "//div[text()='day']")
    _todayView_ = (By.XPATH, "//div[text()='today']")
    _createButton_ = (By.ID, "calendar_grid_view_add_event")

    def test_monthView(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*CalendarViewPage._monthView_).click()

    def test_weekView(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*CalendarViewPage._weekView_).click()

    def test_dayView(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*CalendarViewPage._dayView_).click()

    def test_todayView(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*CalendarViewPage._todayView_).click()

    def test_createButton(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*CalendarViewPage._createButton_).click()

