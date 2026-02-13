import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER, \
    ERROR_USER, VISUAL_USER, PASSWORD

@pytest.mark.positive
@pytest.mark.parametrize("driver", ["incognito-maximized"], indirect=True)
@pytest.mark.parametrize("username", [STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER,
                                      ERROR_USER, VISUAL_USER])
def test_success_login(driver, username):
    login_page = LoginPage(driver)
    login_page.open_page(login_page.URL)
    login_page.login(username, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_current_url() == inventory_page.URL, "Должна была открыться страница каталога"

@pytest.mark.incognito
@pytest.mark.negative
def test_incorrect_password(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, "incorrect password")

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Username and password do not match any user in this service", "Некорректный текст ошибки"

@pytest.mark.incognito
@pytest.mark.negative
def test_incorrect_username(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login("incorrect username", PASSWORD)

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Username and password do not match any user in this service", "Некорректный текст ошибки"

@pytest.mark.incognito
@pytest.mark.negative
def test_empty_username_field(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login("", PASSWORD)

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Username is required", "Некорректный текст ошибки"

@pytest.mark.incognito
@pytest.mark.negative
def test_empty_password_field(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, "")

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Password is required", "Некорректный текст ошибки"
