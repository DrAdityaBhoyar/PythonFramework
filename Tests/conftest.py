from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    chromeDriver = "/Users/adityabhoyar/PycharmProjects/PythonFramework/Driver/chromedriver"
    driver = webdriver.Chrome(chromeDriver)
    driver.get("http://sumedhg.hpadvise.com/index_daytonastate_dev.php/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
