from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.XPATH, "//input[@id='user-name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//*[@class='error-message-container error']")

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def error_message_is_displayed(self):
        return self.is_displayed(self.ERROR_MESSAGE)

