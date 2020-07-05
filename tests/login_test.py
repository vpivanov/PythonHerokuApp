import pytest
import allure
import moment

from selenium.webdriver.common.by import By
from utils import utils as utils
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL + "login")

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()

        # Verification:
        # Title verification
        try:
            expected_title = "The Internet"
            actual_title = driver.title
            assert expected_title == actual_title
            # self.assertEquel(expected_title, actual_title)
            print("Title assertion is True")

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            test_name = utils.whoami()
            current_time = moment.now().strftime("%m-%d-%Y_%H_%M_%S")
            screenshot_name = test_name + "_" + current_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users//Vladimir/python/HerokuApp/screenshots/"+screenshot_name+".png")
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No exceptions occurred")
        finally:
            print("I am inside finally block")

        # URL verification:
        expected_url = 'http://the-internet.herokuapp.com/secure'
        actual_url = driver.current_url
        assert expected_url == actual_url
        # self.assertEqual(expected_url, actual_url)
        print("Url assertion is True")

        # Login message verification:
        expected_message = 'You logged into a secure area!\n×'
        actual_message = driver.find_element(By.CSS_SELECTOR, 'div#flash').text
        assert expected_message == actual_message
        # self.assertEqual(expected_message, actual_message)
        print("Message assertion is True")

    def test_logout(self):
        driver = self.driver
        home_page = HomePage(driver)
        home_page.click_logout_link()
