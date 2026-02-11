import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import STANDARD_USER, PASSWORD

def test_success_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_current_url() == inventory_page.URL, "Должна была открыться страница каталога"

@pytest.mark.negative
def test_incorrect_password(driver):
    login_page = LoginPage(driver)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, "incorrect password")

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_is_displayed(), "Должна выводиться ошибка логина"



