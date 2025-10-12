import allure
import pytest


@allure.step("Find drink by name: {drink_name}")
def find_drink(menu_page, drink_name):
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' not found"
    return cup

@allure.step("Verify ingredients for drink '{drink_name}'")
def verify_ingredients(actual_ingredients, expected_ingredients, drink_name):
    expected_ingredients_list = [ingredient.strip() for ingredient in expected_ingredients]
    assert actual_ingredients == expected_ingredients_list, (
        f"Expected ingredients {expected_ingredients_list}, but got {actual_ingredients}"
    )

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
@allure.issue("56", "Issue #56")
@allure.label("author", "Ruslana Feigina")
@allure.label("priority", "high")
def test_ingredients_displayed_correctly(driver_menu_page, drink_name, expected_ingredients):
    with allure.step("Open Menu Page"):
        menu_page = driver_menu_page

    cup = find_drink(menu_page, drink_name)

    with allure.step(f"Get and verify ingredients of drink '{drink_name}'"):
        actual_ingredients = cup.get_ingredients_text()
        verify_ingredients(actual_ingredients, expected_ingredients, drink_name)