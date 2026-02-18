import pytest
import allure
from pages.cart_page import CartPage
from pages.product_page import ProductPage

@allure.parent_suite("Добавление в корзину")
@allure.feature("Добавление товара в корзину")
@allure.title("Добавление товара в корзину со страницы каталога")
@pytest.mark.incognito
@pytest.mark.add_to_cart
def test_add_to_cart_from_inventory_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    with allure.step("Нажать кнопку Добавить в корзину"):
        inventory_page.add_to_cart()

    assert inventory_page.header.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"

    with allure.step("Нажать на иконку корзины в хедере"):
        inventory_page.header.open_cart_page()

    cart_page = CartPage(inventory_page.driver)
    assert cart_page.cart_item_is_displayed(), "Добавленный товар не отображается в корзине"

@allure.parent_suite("Добавление в корзину")
@allure.feature("Добавление товара в корзину")
@allure.title("Добавление товара в корзину со страницы товара")
@pytest.mark.incognito
@pytest.mark.add_to_cart
def test_add_to_cart_from_product_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user
    inventory_page.open_product_page()

    product_page = ProductPage(inventory_page.driver)
    product_page.add_to_cart()

    assert product_page.header.cart_counter_text() == "1", "Счетчик корзины должен показывать 1"

    product_page.header.open_cart_page()

    cart_page = CartPage(product_page.driver)

    assert cart_page.cart_item_is_displayed(), "Добавленный товар не отображается в корзине"