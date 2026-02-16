from pages.base_page import BasePage
from pages.components.header import Header
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    CART_ITEM = (By.XPATH, "//*[@class='cart_item']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")
    REMOVE_FROM_CART_BUTTON = (By.XPATH, "//button[@id='remove-sauce-labs-backpack']")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
    def cart_item_is_displayed(self):
        return self.is_displayed(self.CART_ITEM)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def remove_from_cart(self):
        self.click(self.REMOVE_FROM_CART_BUTTON)