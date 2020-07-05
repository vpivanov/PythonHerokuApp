from selenium.webdriver.common.by import By
from utils import utils as utils


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = 'username'
        self.password_textbox_id = 'password'
        self.login_button_xpath = "//form[@id='login']//i[@class='fa fa-2x fa-sign-in']"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(utils.USERNAME)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(utils.PASSWORD)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()