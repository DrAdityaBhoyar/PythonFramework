from PagesObejct.CalendarViewPage import CalendarViewPage


class CalendarViewPageFunctionality:
    def __init__(self, driver):
        self.driver = driver

    def test_createByMonthView(self):
        cp = CalendarViewPage(self.driver)
        #cp.test_monthView()
        cp.test_createButton()

    def test_createByWeekView(self):
        cp = CalendarViewPage(self.driver)
        cp.test_weekView()
        cp.test_createButton()

    def test_createByDayView(self):
        cp = CalendarViewPage(self.driver)
        cp.test_dayView()
        cp.test_createButton()

    def test_createByTodayView(self):
        cp = CalendarViewPage(self.driver)
        cp.test_todayView()
        cp.test_createButton()

