from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutComplitePage
from selenium.webdriver.common.by import By

class CheckoutStepTwoPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    CART_ITEM = (By.XPATH, "//*[@class='cart_item']")
    SUMMARY_INFO = (By.XPATH, "//*[@class='summary_info']")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")

    def cart_item_is_displayed(self):
        return self.is_displayed(self.CART_ITEM)

    def summary_info_is_displayed(self):
        return self.is_displayed(self.SUMMARY_INFO)

    def create_order(self):
        self.click(self.FINISH_BUTTON)
        return CheckoutComplitePage(self.driver)



