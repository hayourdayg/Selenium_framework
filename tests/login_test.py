

from selenium import webdriver
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import utils as utils
import allure

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        driver.implicitly_wait(10)
        driver.maximize_window()

        login =LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()



        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.implicitly_wait(10)
        # driver.find_element_by_id("btnLogin").click()

    def test_logout(self):
       try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x =driver.title
            assert x =="orange"


       except AssertionError as error:
           print("Assertion error occurred")
           print(error)
           allure.attach(self.driver.get_as_screenshot_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)

       except:
           print("Some exception occurred")
           raise
       else:
           print("No exceptions occurred")
       finally:
           print("This block will always execute | Close DB")

