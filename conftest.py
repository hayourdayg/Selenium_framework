import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):

    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="/Users/ayodeji.babatunde/PycharmProjects/Selenium_framework/drivers/chromedriver")

    elif browser =='firefox':
          driver = webdriver.Firefox(executable_path="/Users/ayodeji.babatunde/PycharmProjects/Selenium_framework/drivers/geckodriver")


    # driver = webdriver.Chrome(executable_path="/Users/ayodeji.babatunde/PycharmProjects/Selenium_framework/drivers/chromedriver")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver =driver
    yield
    driver.close()
    driver.quit()
    print("Test completed")