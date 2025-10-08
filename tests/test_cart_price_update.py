
def test_tc_002_verify_price_update_and_empty_cart_message(driver_menu_page):
    menu_page = driver_menu_page
    (
        menu_page
        .click_on_cup_by_name("Espresso")
        .click_on_cup_by_name("Espresso Macchiato")
    )
    menu_page.wait_for_total_update("$22.00")
    assert menu_page.get_checkout_button_text() == "Total: $22.00", "Precondition Failed: Initial total price should be $22.00."

    cart_page = menu_page.go_to_cart_page()
    print("Successful transition to CartPage.")

    items = cart_page.items()
    macchiato_item = next(
        (item for item in items if item.get_name() == "Espresso Macchiato"),
        None
    )
    assert macchiato_item is not None, "Step 1 Failed: Espresso Macchiato not found on CartPage."

    macchiato_item.decrease_quantity()

    assert cart_page.pay().get_total_amount() == 10.00, "Step 3 Failed: Total amount should be $10.00."
    # Step 4: Verify only one item remains (Espresso)
    assert len(cart_page.items()) == 1, "Step 4 Failed: Only one item should remain in the cart list."

    remaining_item = cart_page.items()[0]
    assert remaining_item.get_name() == "Espresso", "Step 5 Failed: Espresso not the remaining item."

    remaining_item.decrease_quantity()

    assert cart_page.is_empty_cart_displayed(), "Step 7 Failed: 'No coffee' message should be displayed."
