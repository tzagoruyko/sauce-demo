from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutComplitePage(BasePage):
    URL = "https://www.saucedemo.com/checkout-complete.html"

    CHECKOUT_COMPLETE_CONTAINER = (By.XPATH, "//*[@class='checkout_complete_container']")
    COMPLETE_HEADER = (By.XPATH, "//*[@class='complete-header']")
    COMPLETE_TEXT = (By.XPATH, "//*[@class='complete-text']")


    def checkout_complete_container_is_displayed(self):
        return self.is_displayed(self.CHECKOUT_COMPLETE_CONTAINER)

    def complete_header_text(self):
        return self.element_text(self.COMPLETE_HEADER)

    def complete_text(self):
        return self.element_text(self.COMPLETE_TEXT)