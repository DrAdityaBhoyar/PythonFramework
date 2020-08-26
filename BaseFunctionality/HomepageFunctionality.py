from PagesObejct.HomePage import HomePage


class HomePageFunctionality:
    def __init__(self, driver):
        self.driver = driver

    def test_pageNavigatorToCalendar(self):
        pn = HomePage(self.driver)
        pn.test_connectMenu()
        pn.test_calendarPage()



