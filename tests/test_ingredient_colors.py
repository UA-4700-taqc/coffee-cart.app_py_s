import csv
import os
import re

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

@pytest.mark.parametrize("drink_name, ingredient_name, expected_color", test_data)
def test_ingredient_color_matches_expected(driver_menu_page, drink_name, ingredient_name, expected_color):
    menu_page = driver_menu_page

    # Find drink by name
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' not found"

    # Find ingredient in the drink
    ingredient = cup.get_ingredient_by_name(ingredient_name)
    assert ingredient is not None, f"Ingredient '{ingredient_name}' not found in drink '{drink_name}'"

    # Get color using get_color() method
    actual_color = ingredient.get_color()

    # Normalize to standard rgb(...) format
    normalized_actual = normalize_color(actual_color)
    normalized_expected = normalize_color(expected_color)

    assert normalized_actual == normalized_expected, (
        f"Expected color '{normalized_expected}', but got '{normalized_actual}'"
    )