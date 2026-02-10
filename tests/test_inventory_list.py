from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# В этом варианте явный логин, который будет повторяться во всех тестах. Ниже тоже самое, но через фикстуру для чистоты
# def test_inventory_list_is_displayed(driver):
#     login_page = LoginPage(driver)
#     login_page.open_page(login_page.URL)
#     login_page.login("standard_user", "secret_sauce")
#
#     inventory_page = InventoryPage(driver)
#
#     assert inventory_page.inventory_list_is_displayed(), "Список товаров не отображается на странице"

def test_inventory_list_is_displayed(logged_in_user):
    inventory_page = logged_in_user
    assert inventory_page.inventory_list_is_displayed(), "Список товаров не отображается на странице"