from selenium.webdriver.common.by import By


class EventPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _announcementTab_ = (By.XPATH, "//div[@class='fmwk-tabbed-widget-nav-body']/div[1]")
    _appointmentTab_ = (By.XPATH, "//div[@class='fmwk-tabbed-widget-nav-body']/div[3]")
    _eventTab_ = (By.XPATH, "//div[@class='fmwk-tabbed-widget-nav-body']/div[4]")
    _AdviserDropdown_ = (By.CSS_SELECTOR, "#impersonated_advisor_id-button")
    _getAdviser_ = (By.LINK_TEXT, "My Calendar")
    _RepeatOptionDropdown_ = (By.CSS_SELECTOR, "#repeat_type-button")
    _getRepeatNeverValue_ = (By.LINK_TEXT, "Repeat Never")
    _getRepeatDailyValue_ = (By.LINK_TEXT, "Repeats Daily")
    _getRepeatWeeklyValue_ = (By.LINK_TEXT, "Repeats Weekly")
    _getRepeatMonthlyValue_ = (By.LINK_TEXT, "Repeats Monthly")
    _getRepeatEOWValue_ = (By.LINK_TEXT, "Repeats Every Other Week")
    _selectGroup_ = (By.ID, "multi_autocomplete_to_user_id")
    _selectGroupValue_ = (By.LINK_TEXT, "test static")
    _eventTitle_ = (By.ID, "event_title")
    _eventLocation_ = (By.ID, "event_location")
    _allDayEvent_ = (By.CSS_SELECTOR, "#checkbox_all_day")
    _eventDescription_ = (By.CSS_SELECTOR, "#note_user")
    _createButton_ = (By.CSS_SELECTOR, "#calendar_form_add")
    _startDateDropDown_ = (By.ID, "alt_start_date_time_date")
    _stopOccurringOnDate_ = (By.ID, "alt_daily_option_2")
    _startDateValue_ = (By.CLASS_NAME, "ui-datepicker-today")
    _endDateValue_ = (By.CLASS_NAME, "ui-datepicker-today+td")
    _publicEvent_ = (By.XPATH, "//div[text()='public']")
    _privateEvent_ = (By.XPATH, "//div[text()='private']")

    def test_eventTab(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._eventTab_).click()

    def test_selectCalendar(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._AdviserDropdown_).click()
        return self.driver.find_element(*EventPage._getAdviser_).click()

    def test_repeatOptionAsNever(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._RepeatOptionDropdown_).click()
        return self.driver.find_element(*EventPage._getRepeatNeverValue_).click()

    def test_repeatOptionAsDaily(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._RepeatOptionDropdown_).click()
        return self.driver.find_element(*EventPage._getRepeatDailyValue_).click()

    def test_repeatOptionAsWeekly(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._RepeatOptionDropdown_).click()
        return self.driver.find_element(*EventPage._getRepeatWeeklyValue_).click()

    def test_repeatOptionAsMonthly(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._RepeatOptionDropdown_).click()
        return self.driver.find_element(*EventPage._getRepeatMonthlyValue_).click()

    def test_repeatEveryOtherWeek(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._RepeatOptionDropdown_).click()
        return self.driver.find_element(*EventPage._getRepeatEOWValue_).click()

    def test_groupName(self, groupName):
        self.driver.implicitly_wait(30)
        self.driver.find_element(*EventPage._selectGroup_).send_keys(groupName)
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._selectGroupValue_).click()

    def test_eventTitle(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._eventTitle_).send_keys("Test Event Title Demo")

    def test_eventLocation(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._eventLocation_).send_keys("My Office Address")

    def test_selectAllDayEvent(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._allDayEvent_).click()

    def test_eventDescription (self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._eventDescription_).send_keys("Test Event Description")

    def test_selectStartDateDropDown(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._startDateDropDown_).click()

    def test_selectEndDateDropDown(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._stopOccurringOnDate_).click()

    def test_selectStartDate(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._startDateValue_).click()

    def test_selectEndDate(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._endDateValue_).click()

    def test_createButton(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._createButton_).click()

    def test_publicEvent(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._publicEvent_).click()

    def test_privateEvent(self):
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*EventPage._privateEvent_).click()
