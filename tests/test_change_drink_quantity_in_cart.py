import pytest
from selenium import webdriver

from config.resources import BASE_URL
from pages.cart_page import CartPage
from pages.menu_page import MenuPage


@pytest.fixture()
def menu_page(driver):
    """Return the MenuPage object for the base URL."""
    driver.get(BASE_URL)
    return MenuPage(driver)


@pytest.fixture()
def cart_page(driver):
    """Return the CartPage object for the base URL."""
    driver.get(BASE_URL)
    return CartPage(driver)


def test_change_drink_quantity_in_cart(driver, menu_page, cart_page):
    """Test adding a drink to the cart and verify increasing/decreasing its quantity using buttons in the cart."""
    menu_page.click_on_cup_by_name("Espresso")
    menu_page.go_to_cart_page()
    cart_page.items()[0].increment_click()
    quantity = cart_page.items()[0].quantity
    assert quantity == 2
    cart_page.items()[0].decrement_click()
    quantity = cart_page.items()[0].quantity
    assert quantity == 1
