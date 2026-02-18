import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER, \
    ERROR_USER, VISUAL_USER, PASSWORD

@allure.parent_suite("Авторизация")
@allure.feature("Авторизация")
@allure.story("Валидные данные")
@allure.title("Успешная авторизации")
@allure.description("Пользователь может войти с валидными данными")
@pytest.mark.login
@pytest.mark.parametrize("driver", ["incognito-headless"], indirect=True)
@pytest.mark.parametrize("username", [STANDARD_USER, PROBLEM_USER, PERFORMANCE_GLITCH_USER,
                                      ERROR_USER, VISUAL_USER])
def test_success_login(driver, username):
    login_page = LoginPage(driver)
    login_page.open_page(login_page.URL)
    login_page.login(username, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_current_url() == inventory_page.URL, "Должна была открыться страница каталога"

@allure.parent_suite("Авторизация")
@allure.feature("Авторизация")
@allure.story("Невалидные данные")
@allure.title("Авторизация с невалидным паролем")
@allure.description("Пользователь не может войти с невалидным паролем")
@pytest.mark.incognito
@pytest.mark.login
def test_incorrect_password(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, "incorrect password")

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Username and password do not match any user in this service", "Некорректный текст ошибки"

@allure.parent_suite("Авторизация")
@allure.feature("Авторизация")
@allure.story("Невалидные данные")
@allure.title("Авторизация с невалидным username")
@allure.description("Пользователь не может войти с невалидным username")
@pytest.mark.incognito
@pytest.mark.login
def test_incorrect_username(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login("incorrect username", PASSWORD)

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Username and password do not match any user in this service", "Некорректный текст ошибки"

@allure.parent_suite("Авторизация")
@allure.feature("Авторизация")
@allure.story("Невалидные данные")
@allure.title("Авторизация с пустым полем username")
@allure.description("Поле username является обязательным")
@pytest.mark.incognito
@pytest.mark.login
def test_empty_username_field(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login("", PASSWORD)

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Username is required", "Некорректный текст ошибки"

@allure.parent_suite("Авторизация")
@allure.feature("Авторизация")
@allure.story("Невалидные данные")
@allure.title("Авторизация с пустым полем password")
@allure.description("Поле password является обязательным")
@pytest.mark.incognito
@pytest.mark.login
def test_empty_password_field(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, "")

    assert login_page.get_current_url() == login_page.URL, "Должна была остаться открытой страница логина"
    assert login_page.error_message_text() == "Epic sadface: Password is required", "Некорректный текст ошибки"
