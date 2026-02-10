from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutStepOnePage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last-name']")
    POSTAL_CODE_INPUT = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")

    def fill_form(self, first_name, last_name, postal_code):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)


