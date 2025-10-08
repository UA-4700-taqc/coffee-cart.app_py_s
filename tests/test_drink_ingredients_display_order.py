import pytest


@pytest.mark.parametrize("drink_name, expected_ingredients", [
    ("Espresso", ["espresso"]),
    ("Espresso Macchiato", ["milk foam", "espresso"]),
    ("Cappuccino", ["milk foam", "steamed milk", "espresso"]),
    ("Mocha", ["whipped cream", "steamed milk", "chocolate syrup", "espresso"]),
    ("Flat White", ["steamed milk", "espresso"]),
    ("Americano", ["water", "espresso"]),
    ("Cafe Latte", ["milk foam", "steamed milk", "espresso"]),
    ("Espresso Con Panna", ["whipped cream", "espresso"]),
    ("Cafe Breve", ["milk foam", "steamed cream", "steamed milk", "espresso"]),
])
def test_ingredients_displayed_correctly(driver_menu_page, drink_name, expected_ingredients):
    menu_page = driver_menu_page
    cup = menu_page.get_cup_by_name(drink_name)

    assert cup is not None, f"Drink '{drink_name}' not found"
    actual_ingredients = cup.get_ingredients_text()

    # Compare the lists of ingredients
    expected_ingredients_list = [ingredient.strip() for ingredient in expected_ingredients]

    assert actual_ingredients == expected_ingredients_list, (
        f"Expected ingredients {expected_ingredients_list}, but got {actual_ingredients}"
    )