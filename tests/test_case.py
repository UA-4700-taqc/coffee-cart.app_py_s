import logging

import pytest

from utilities.logger import Logger


def test_case(driver_menu_page):
    """Test adding 3 drinks and a promo drink, then deleting one drink and verify the promo drink isn't in the cart."""
    menu_page = driver_menu_page
    logger = Logger.get_logger(__name__, console_level=logging.ERROR)
    try:
        cart_page = (
            menu_page.click_on_cup_by_name("Cafe Breve")
            .click_on_cup_by_name("Espresso")
            .click_on_cup_by_name("Espresso Con Panna")
            .promo()
            .press_yes()
            .go_to_cart_page()
        )
        items = cart_page.items()
        item_names = [item.get_name() for item in items]
        assert "(Discounted) Mocha" in item_names, "Expected discounted Mocha not found"

        items[0].remove_item()
        item_names = [item.get_name() for item in cart_page.items()]
        assert "(Discounted) Mocha" not in item_names, "Discounted Mocha still present after removal"

    except AssertionError as e:
        logger.error(f"Assertion failed: {e}")
        raise
