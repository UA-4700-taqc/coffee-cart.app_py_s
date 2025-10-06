import pytest
import re
from pages.menu_page import MenuPage
from pages.cart_page import CartPage
import time

def parse_price(price_text: str) -> float:
    """
    Utility function to clean and convert price string
    (e.g., "Total: $10.50" or "$10.50") to float.
    """
    cleaned_price = re.sub(r'(Total:|\s|\$|€|₴|,)', '', price_text).strip()
    try:
        return float(cleaned_price)
    except ValueError:
        return 0.0


def test_product_add_and_removal_flow(driver_menu_page: MenuPage):
    """
    Automate the test case for adding products, verifying cart content/total,
    removing all products, and verifying the cart is empty
    """
    menu_page = driver_menu_page

    PRODUCTS_TO_ADD = 3
    print(f"\n--- Starting Cart Removal Test with {PRODUCTS_TO_ADD} products ---")

    menu_page.add_products_to_cart(count=PRODUCTS_TO_ADD)

    print("PASS: Step 1. Products added. Moving to cart.")

    cart_page: CartPage = menu_page.open_cart()

    initial_item_count = cart_page.get_number_of_items()
    assert initial_item_count == PRODUCTS_TO_ADD, f"Step 2 Failed: Expected {PRODUCTS_TO_ADD} items, found {initial_item_count}."
    print(f"PASS: Step 2. Cart opened. Items displayed: {initial_item_count}")

    cart_total_text = cart_page.pay().get_total_price_text()
    initial_total_price = parse_price(cart_total_text)

    assert initial_total_price > 0.0, "Step 3 Failed: Cart total price is zero or invalid on cart page."
    print(f"PASS: Step 3. Cart total price validated: {cart_total_text}")

    cart_page.clear_cart()

    remaining_items = cart_page.get_number_of_items()
    assert remaining_items == 0, f"Step 4 Failed: Expected 0 remaining items, found {remaining_items} after removal."
    print("PASS: Step 4. All products successfully removed from the cart.")

    is_empty = cart_page.is_empty_cart_displayed()
    assert is_empty, "Step 5 Failed: Cart is not confirmed empty."
    print("PASS: Step 5. Cart is successfully confirmed empty.")

    print("--- Test Completed Successfully ---")