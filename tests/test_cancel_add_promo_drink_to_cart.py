from pages.menu_page import MenuPage


def test_cancel_add_promo_drink_to_cart(driver_menu_page):
    """Test adding 3 drinks and canceling a promo drink, then verify the promo drink isn`t in the cart."""
    menu_page = driver_menu_page
    cart_page = (
        menu_page.click_on_cup_by_name("Cafe Breve")
        .click_on_cup_by_name("Espresso")
        .click_on_cup_by_name("Espresso Con Panna")
        .promo()
        .press_no()
        .go_to_cart_page()
    )
    item_names = [item.get_name() for item in cart_page.items()]
    assert "(Discounted) Mocha" not in item_names
