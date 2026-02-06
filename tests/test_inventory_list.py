from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory_list_is_displayed(driver):
    login_page = LoginPage(driver)
    login_page.open_page(login_page.URL)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert inventory_page.inventory_list_is_displayed(), "Список товаров не отображается на странице"