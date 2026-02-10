from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutComplitePage

def test_create_order(logged_in_user):
    inventory_page = logged_in_user
    inventory_page.add_to_cart()

    cart_page = CartPage(inventory_page.driver)
    cart_page.open_page(cart_page.URL)
    cart_page.click_checkout()

    checkout_step_one_page = CheckoutStepOnePage(cart_page.driver)
    checkout_step_one_page.fill_form("Anna", "Ivanova", "12345")
    checkout_step_one_page.click_continue_checkout()

    checkout_step_two_page = CheckoutStepTwoPage(checkout_step_one_page.driver)
    assert checkout_step_two_page.cart_item_is_displayed(), "Карточка товара не отображается"
    assert checkout_step_two_page.summary_info_is_displayed(), "Данные о заказе не отображаются"
    checkout_step_two_page.create_order()

    checkout_complite_page = CheckoutComplitePage(checkout_step_two_page.driver)
    assert checkout_complite_page.checkout_complete_container_is_displayed(), "Блок с информацией об успешном оформлении заказа не отображается"
    assert checkout_complite_page.complete_header_text() == "Thank you for your order!", "Текст заголовка некорректный"
    assert checkout_complite_page.complete_text() == "Your order has been dispatched, and will arrive just as fast as the pony can get there!", "Текст под заголовком некорректный"