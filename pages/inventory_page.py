from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    INVENTORY_LIST = (By.XPATH, "//*[@class='inventory_list']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_HEADER_ICON = (By.XPATH, "//*[@class='shopping_cart_link']")
    CART_HEADER_COUNTER = (By.XPATH, "//*[@class='shopping_cart_badge']")
    PRODUCT_LINK = (By.XPATH, "//*[@id='item_0_title_link']")

    def inventory_list_is_displayed(self):
        return self.is_displayed(self.INVENTORY_LIST)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def cart_counter_text(self):
        return self.element_text(self.CART_HEADER_COUNTER)

    def open_product_page(self):
        self.click(self.PRODUCT_LINK)




