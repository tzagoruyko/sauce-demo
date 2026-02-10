from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    CART_ITEM = (By.XPATH, "//*[@class='cart_item']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")

    def cart_item_is_displayed(self):
        return self.is_displayed(self.CART_ITEM)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)