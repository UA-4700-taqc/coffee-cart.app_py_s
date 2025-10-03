def test_verify_total_amount_in_cart(driver_menu_page):
    menu_page = driver_menu_page
    cart_page = (
        menu_page.click_on_cup_by_name("Cafe Breve").click_on_cup_by_name("Espresso Con Panna").go_to_cart_page()
    )

    item1 = cart_page.items()[0]
    item2 = cart_page.items()[1]
    assert item1.get_total_price() == item1.quantity * item1.price
    assert item2.get_total_price() == item2.quantity * item2.price
    assert cart_page.pay().get_total_amount() == item1.get_total_price() + item2.get_total_price()

    item1.increase_quantity()
    assert item1.get_total_price() == item1.quantity * item1.price
    assert cart_page.pay().get_total_amount() == item1.get_total_price() + item2.get_total_price()
