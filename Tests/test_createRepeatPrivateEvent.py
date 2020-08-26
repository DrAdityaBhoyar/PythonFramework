from Driver.BaseClass import BaseClass
from BaseFunctionality.CalendarViewPageFunctionality import CalendarViewPageFunctionality
from BaseFunctionality.EventPageFunctionality import EventPageFunctionality
from BaseFunctionality.HomepageFunctionality import HomePageFunctionality
from BaseFunctionality.LoginFunctionality import LoginPageFunctionality


class TestCreateRepeatPrivateEventFlow(BaseClass):

    def test_validLogin(self):
        lp = LoginPageFunctionality(self.driver)
        lp.test_validLogin("directoraa.daytonastate@hpadvise.com", "Welcome123")

    def test_pageNavigator(self):
        pn = HomePageFunctionality(self.driver)
        pn.test_pageNavigatorToCalendar()

    def test_calendarPage(self):
        cp = CalendarViewPageFunctionality(self.driver)
        cp.test_createByMonthView()

    def test_eventCreationPage(self):
        ep = EventPageFunctionality(self.driver)
        ep.test_repeatDailyEventAsPrivate()                 # repeating event on daily basic as Private

