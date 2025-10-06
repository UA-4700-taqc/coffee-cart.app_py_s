import pytest
from pages.menu_page import MenuPage


def test_promo_discount_display(driver_menu_page: MenuPage):
    """
    Test the business logic for displaying the promotional discount banner on the menu page
    """
    menu_page = driver_menu_page

    items_to_check = [
        (1, "First"),
        (1, "Second")
    ]

    total_items = 0
    for count, step_name in items_to_check:
        menu_page.add_products_to_cart(count=count)
        total_items += count

        assert not menu_page.is_promo_displayed(timeout=1), \
            f"Step {total_items} Failed: Promo displayed prematurely after {total_items} item(s)."
        print(f"PASS: Step {total_items}. {step_name} item added. Promo is not displayed.")

    menu_page.add_products_to_cart(count=1)
    total_items += 1

    assert menu_page.is_promo_displayed(timeout=5), "Step 3 FAILED: Promo not displayed after 3 items."
    print("PASS: Step 3. Third item added. Discount promo is displayed.")

    menu_page.add_products_to_cart(count=3)
    total_items += 3

    assert menu_page.is_promo_displayed(timeout=1), "Step 4 FAILED: Discount promo disappeared after adding more items."
    print(f"PASS: Step 4. Added another 3 items (Total: {total_items}). Discount promo remains displayed.")

    print("\n--- Test Completed Successfully: Promo Discount Logic Verified ---")