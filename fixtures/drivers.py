"""Fixture for WebDriver instance."""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.resources import BASE_URL, IMPLICIT_WAIT
from pages.cart_page import CartPage
from pages.menu_page import MenuPage

__all__ = ["driver", "driver_menu_page", "driver_cart_page"]


@pytest.fixture(scope="session")
def driver():
    """Fixture to initialize and quit the WebDriver instance."""
    service = Service(ChromeDriverManager(driver_version="140.0.7339.207").install())
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def driver_menu_page(driver):
    """Return the MenuPage object for the base URL."""
    driver.get(BASE_URL)
    return MenuPage(driver)


@pytest.fixture()
def driver_cart_page(driver):
    """Return the CartPage object for the base URL."""
    driver.get(BASE_URL)
    return CartPage(driver)
