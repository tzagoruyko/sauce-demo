import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.remove_from_cart
@pytest.mark.incognito
def test_remove_from_cart_from_inventory_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.add_to_cart()
    assert inventory_page.header.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"
    inventory_page.remove_from_cart()
    assert inventory_page.header.cart_counter_is_not_displayed(),  "Счётчик корзины должен исчезнуть"

@pytest.mark.remove_from_cart
@pytest.mark.incognito
def test_remove_from_cart_from_product_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.open_product_page()
    product_page = ProductPage(inventory_page.driver)
    product_page.add_to_cart()
    assert product_page.header.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"
    product_page.remove_from_cart()
    assert product_page.header.cart_counter_is_not_displayed(),  "Счётчик корзины должен исчезнуть"

@pytest.mark.remove_from_cart
@pytest.mark.incognito
def test_remove_from_cart_from_cart_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.add_to_cart()
    assert inventory_page.header.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"
    inventory_page.header.open_cart_page()

    cart_page = CartPage(inventory_page.driver)
    cart_page.remove_from_cart()
    assert cart_page.cart_item_is_not_displayed(), "Карточка товара должна мсчезнуть"
    assert cart_page.header.cart_counter_is_not_displayed(),  "Счётчик корзины должен исчезнуть"


