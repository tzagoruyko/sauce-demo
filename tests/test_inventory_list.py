# Шаги логина заменены фикстурой

def test_inventory_list_is_displayed(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    assert inventory_page.inventory_list_is_displayed(), "Список товаров не отображается на странице"