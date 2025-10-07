# This test checks that the prices of coffee drinks on the menu match the expected values from the CSV file.
# The CSV file should be located at 'test_data/drinks_prices.csv' relative to this test file.

import csv
import os
import pytest

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'drinks_prices.csv')

def load_test_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['drink_name'], float(row['expected_price'])) for row in reader]

test_data = load_test_data_from_csv(CSV_FILE_PATH)

@pytest.mark.parametrize("drink_name, expected_price", test_data)
def test_drink_price_matches_expected(driver_menu_page, drink_name, expected_price):
    menu_page = driver_menu_page

    # Find the drink by name
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' not found"

    # Get the actual price using the get_price() method
    actual_price = float(cup.get_price())  # Convert to float for accurate comparison

    # Check if the price matches the expected value
    assert actual_price == expected_price, (
        f"Expected price for '{drink_name}' to be {expected_price}, but got {actual_price}"
    )