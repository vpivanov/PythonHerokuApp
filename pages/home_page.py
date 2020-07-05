from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def click_logout_link(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()