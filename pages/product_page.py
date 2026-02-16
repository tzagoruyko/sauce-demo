from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart']")
    CART_HEADER_ICON = (By.XPATH, "//*[@class='shopping_cart_link']")
    CART_HEADER_COUNTER = (By.XPATH, "//*[@class='shopping_cart_badge']")
    PRODUCT_NAME = (By.XPATH, "//*[@class='inventory_details_name large_size']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//*[@class='inventory_details_desc large_size']")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='inventory_details_price']")

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def cart_counter_text(self):
        return self.element_text(self.CART_HEADER_COUNTER)

    def product_name_text(self):
        return self.element_text(self.PRODUCT_NAME)

    def product_description_text(self):
        return self.element_text(self.PRODUCT_DESCRIPTION)

    def product_price_text(self):
        return self.element_text(self.PRODUCT_PRICE)

    def open_cart_page(self):
        self.click(self.CART_HEADER_ICON)