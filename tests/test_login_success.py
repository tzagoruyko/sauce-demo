from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_success_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_current_url() == inventory_page.URL, "Должна была открыться страница каталога"



