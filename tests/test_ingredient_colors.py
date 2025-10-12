import csv
import os
import re
import allure
import pytest

# Convert rgba(...) → rgb(...) for exact comparison
def normalize_color(color_str: str) -> str:
    match = re.match(r'rgba?\((\d+),\s*(\d+),\s*(\d+)', color_str)
    if match:
        r, g, b = match.groups()
        return f"rgb({r}, {g}, {b})"
    return color_str.strip()

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'drink_ingredient_colors.csv')

# Read data from CSV
def load_test_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['drink_name'], row['ingredient_name'], row['expected_color']) for row in reader]
test_data = load_test_data_from_csv(CSV_FILE_PATH)

@allure.step("Find drink by name: {drink_name}")
def find_drink(menu_page, drink_name):
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' not found"
    return cup

@allure.step("Find ingredient '{ingredient_name}' in drink '{drink_name}'")
def find_ingredient(cup, ingredient_name, drink_name):
    ingredient = cup.get_ingredient_by_name(ingredient_name)
    assert ingredient is not None, f"Ingredient '{ingredient_name}' not found in drink '{drink_name}'"
    return ingredient

@allure.step("Verify ingredient color matches expected")
def verify_color(actual_color, expected_color):
    normalized_actual = normalize_color(actual_color)
    normalized_expected = normalize_color(expected_color)
    assert normalized_actual == normalized_expected, (
        f"Expected color '{normalized_expected}', but got '{normalized_actual}'"
    )
@pytest.mark.parametrize("drink_name, ingredient_name, expected_color", test_data)
@allure.issue("59", "Issue #59")
@allure.label("author", "Ruslana Feigina")
@allure.label("priority", "medium")
def test_ingredient_color_matches_expected(driver_menu_page, drink_name, ingredient_name, expected_color):
    with allure.step("Open Menu Page"):
        menu_page = driver_menu_page

    cup = find_drink(menu_page, drink_name)
    ingredient = find_ingredient(cup, ingredient_name, drink_name)

    with allure.step(f"Get and verify color of ingredient '{ingredient_name}'"):
        actual_color = ingredient.get_color()
        verify_color(actual_color, expected_color)