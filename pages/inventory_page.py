from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    INVENTORY_LIST = (By.XPATH, "//*[@class='inventory_list']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")

    def inventory_list_is_displayed(self):
        return self.is_displayed(self.INVENTORY_LIST)


