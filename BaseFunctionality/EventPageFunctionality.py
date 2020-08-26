from PagesObejct.EventPage import EventPage


class EventPageFunctionality:
    def __init__(self, driver):
        self.driver = driver

    def test_eventWithoutPrivacyWithoutRepeatOption(self):
        ep = EventPage(self.driver)
        ep.test_eventTab()
        ep.test_selectCalendar()
        ep.test_publicEvent()
        ep.test_eventTitle()
        ep.test_eventLocation()
        ep.test_selectAllDayEvent()
        ep.test_eventDescription()
        ep.test_selectStartDateDropDown()
        ep.test_selectStartDate()

    def test_eventCreationPublic(self, groupName):
        ep = EventPage(self.driver)
        self.test_eventWithoutPrivacyWithoutRepeatOption()
        ep.test_repeatOptionAsNever()
        ep.test_groupName(groupName)
        ep.test_createButton()

    def test_eventCreationPrivate(self):
        ep = EventPage(self.driver)
        self.test_eventWithoutPrivacyWithoutRepeatOption()
        ep.test_repeatOptionAsNever()
        ep.test_privateEvent()
        ep.test_createButton()

    def test_repeatDailyEventAsPublic(self, groupName):
        ep = EventPage(self.driver)
        self.test_eventWithoutPrivacyWithoutRepeatOption()
        ep.test_repeatOptionAsDaily()
        ep.test_selectEndDateDropDown()
        ep.test_selectEndDate()
        ep.test_groupName(groupName)
        ep.test_createButton()

    def test_repeatDailyEventAsPrivate(self):
        ep = EventPage(self.driver)
        self.test_eventWithoutPrivacyWithoutRepeatOption()
        ep.test_repeatOptionAsDaily()
        ep.test_selectEndDateDropDown()
        ep.test_selectEndDate()
        ep.test_createButton()

