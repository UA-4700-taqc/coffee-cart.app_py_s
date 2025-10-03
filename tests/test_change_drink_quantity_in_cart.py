def test_change_drink_quantity_in_cart(driver_menu_page):
    """Test adding a drink to the cart and verify increasing/decreasing its quantity using buttons in the cart."""
    menu_page = driver_menu_page
    cart_page = menu_page.click_on_cup_by_name("Espresso").go_to_cart_page()
    item = cart_page.items()[0]

    assert item.increase_quantity().quantity == 2
    assert item.decrease_quantity().quantity == 1
