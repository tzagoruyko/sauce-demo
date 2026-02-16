from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Header(BasePage):
    CART_HEADER_ICON = (By.XPATH, "//*[@class='shopping_cart_link']")
    CART_HEADER_COUNTER = (By.XPATH, "//*[@class='shopping_cart_badge']")

    def __init__(self, driver):
        super().__init__(driver)

    def cart_counter_text(self):
        return self.element_text(self.CART_HEADER_COUNTER)

    def open_cart_page(self):
        self.click(self.CART_HEADER_ICON)
