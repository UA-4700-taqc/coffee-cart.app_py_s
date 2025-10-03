from pages.menu_page import MenuPage


def test_deletion_items(driver_menu_page):
    """Test verify empty cart message is displayed after items deletion."""
    menu_page = driver_menu_page
    cart_page = (
        menu_page.click_on_cup_by_name("Cappuccino").click_on_cup_by_name("Espresso").go_to_cart_page().clear_cart()
    )
    assert cart_page.is_empty_cart_displayed()


def test_initially_empty_cart(driver_menu_page):
    """Test verify empty cart message is displayed when initially empty cart."""
    menu_page = driver_menu_page
    cart_page = menu_page.go_to_cart_page().clear_cart()
    assert cart_page.is_empty_cart_displayed()


def test_non_empty_cart(driver_menu_page):
    """Test verify empty cart message is not displayed when non-empty cart."""
    menu_page = driver_menu_page
    cart_page = menu_page.click_on_cup_by_name("Cappuccino").click_on_cup_by_name("Espresso").go_to_cart_page()
    assert not cart_page.is_empty_cart_displayed()
