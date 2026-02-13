import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage

@pytest.mark.add_to_cart
def test_add_to_cart_from_inventory_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.add_to_cart()

    assert inventory_page.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"

    cart_page = CartPage(inventory_page.driver)
    cart_page.open_page(cart_page.URL)

    assert cart_page.cart_item_is_displayed(), "Добавленный товар не отображается в корзине"

@pytest.mark.add_to_cart
def test_add_to_cart_from_product_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.open_product_page()

    product_page = ProductPage(inventory_page.driver)
    product_page.add_to_cart()

    assert product_page.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"

    cart_page = CartPage(product_page.driver)
    cart_page.open_page(cart_page.URL)

    assert cart_page.cart_item_is_displayed(), "Добавленный товар не отображается в корзине"