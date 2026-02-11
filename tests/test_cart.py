from pages.cart_page import CartPage

def test_add_to_cart(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.add_to_cart()

    assert inventory_page.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"

    cart_page = CartPage(inventory_page.driver)
    cart_page.open_page(cart_page.URL)

    assert cart_page.cart_item_is_displayed(), "Добавленный товар не отображается в корзине"

