def test_promo_drink_in_cart_for_less_than_3_drinks(driver_menu_page):
    """Verify if the promo drink is in the basket when less than 3 drinks are ordered."""
    menu_page = driver_menu_page
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

    items[1].remove_item()
    item_names = [item.get_name() for item in cart_page.items()]
    assert "(Discounted) Mocha" not in item_names, "Discounted Mocha still present after removal"
