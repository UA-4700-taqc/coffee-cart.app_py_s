import pytest
import allure

# List of drink names, which will also serve as the expected values
test_data = [
    "Espresso",
    "Espresso Macchiato",
    "Cappuccino",
    "Mocha",
    "Flat White",
    "Americano",
    "Cafe Latte",
    "Espresso Con Panna",
    "Cafe Breve",
]

@allure.step("Find drink by name: {drink_name}")
def find_drink(menu_page, drink_name):
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' was not found"
    return cup

@allure.step("Verify displayed name '{actual_name}' matches expected '{expected_name}'")
def verify_name(actual_name, expected_name):
    assert actual_name == expected_name, (
        f"Expected: '{expected_name}', but got: '{actual_name}'"
    )

@pytest.mark.parametrize("drink_name", test_data)
@allure.issue("57", "Issue #57")
@allure.label("author", "Ruslana Feigina")
@allure.label("priority", "high")
def test_drink_name_matches_expected(driver_menu_page, drink_name):
    with allure.step("Open Menu Page"):
        menu_page = driver_menu_page

    cup = find_drink(menu_page, drink_name)

    with allure.step(f"Check displayed name for drink '{drink_name}'"):
        actual_name = cup.name
        verify_name(actual_name, drink_name)