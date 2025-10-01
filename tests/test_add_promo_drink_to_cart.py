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


def test_add_promo_drink_to_cart(driver, menu_page, cart_page):
    """Test adding 3 drinks and a promo drink, then verify the promo drink is in the cart."""
    menu_page.click_on_cup_by_name("Cafe Breve")
    menu_page.click_on_cup_by_name("Espresso")
    menu_page.click_on_cup_by_name("Espresso Con Panna")
    menu_page.promo().press_yes()
    menu_page.go_to_cart_page()
    item_names = [item.name for item in cart_page.items()]
    assert "(Discounted) Mocha" in item_names
