import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import STANDARD_USER, PASSWORD

@pytest.fixture
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture
def logged_in_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, PASSWORD)
    return InventoryPage(driver)
