from pages.base_page import BasePage
from pages.components.header import Header
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart']")
    PRODUCT_NAME = (By.XPATH, "//*[@class='inventory_details_name large_size']")
    PRODUCT_DESCRIPTION = (By.XPATH, "//*[@class='inventory_details_desc large_size']")
    PRODUCT_PRICE = (By.XPATH, "//*[@class='inventory_details_price']")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def product_name_text(self):
        return self.element_text(self.PRODUCT_NAME)

    def product_description_text(self):
        return self.element_text(self.PRODUCT_DESCRIPTION)

    def product_price_text(self):
        return self.element_text(self.PRODUCT_PRICE)
