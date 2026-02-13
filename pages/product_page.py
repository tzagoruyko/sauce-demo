from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart']")
    CART_HEADER_COUNTER = (By.XPATH, "//*[@class='shopping_cart_badge']")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def cart_counter_text(self):
        return self.element_text(self.CART_HEADER_COUNTER)
