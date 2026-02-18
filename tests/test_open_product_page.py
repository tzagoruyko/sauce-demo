import pytest
from pages.product_page import ProductPage

@pytest.mark.incognito
def test_open_product_page(logged_in_standard_user):
    inventory_page = logged_in_standard_user

    catalog_name = inventory_page.product_name_text()
    catalog_description = inventory_page.product_description_text()
    catalog_price = inventory_page.product_price_text()

    inventory_page.open_product_page()

    product_page = ProductPage(inventory_page.driver)

    assert product_page.product_name_text() == catalog_name, "Название товара отличается от того, что указано в каталоге"
    assert product_page.product_description_text() == catalog_description, "Описание товара отличается от того, что указано в каталоге"
    assert product_page.product_price_text() == catalog_price, "Цена товара отличается от той, что указана в каталоге"