import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import STANDARD_USER, PASSWORD

@pytest.fixture
def driver(request):
    options = Options()

    if getattr(request, "param", None) == "incognito-headless":
        options.add_argument("--incognito")
        options.add_argument("--headless")

    print("\nstart browser for test..")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture
def driver_incognito(request):
    options = Options()

    if request.node.get_closest_marker("incognito"):
        options.add_argument("--incognito")
        options.add_argument("--headless")

    print("\nstart browser for test..")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()

@pytest.fixture
def logged_in_standard_user(driver_incognito):
    login_page = LoginPage(driver_incognito)
    login_page.open_page(login_page.URL)
    login_page.login(STANDARD_USER, PASSWORD)
    return InventoryPage(driver_incognito)
