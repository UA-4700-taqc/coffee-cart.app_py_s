import csv
import os
import allure
import pytest

CSV_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'drinks_prices.csv')

def load_test_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['drink_name'], float(row['expected_price'])) for row in reader]

test_data = load_test_data_from_csv(CSV_FILE_PATH)

@allure.step("Find drink by name: {drink_name}")
def find_drink(menu_page, drink_name):
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' not found"
    return cup

@allure.step("Verify price of drink '{drink_name}' matches expected")
def verify_price(actual_price, expected_price, drink_name):
    assert actual_price == expected_price, (
        f"Expected price for '{drink_name}' to be {expected_price}, but got {actual_price}"
    )

@pytest.mark.parametrize("drink_name, expected_price", test_data)
@allure.issue("58", "Issue #58")
@allure.label("author", "Ruslana Feigina")
@allure.label("priority", "high")
def test_drink_price_matches_expected(driver_menu_page, drink_name, expected_price):
    with allure.step("Open Menu Page"):
        menu_page = driver_menu_page

    cup = find_drink(menu_page, drink_name)

    with allure.step(f"Get and verify price of drink '{drink_name}'"):
        actual_price = float(cup.get_price())
        verify_price(actual_price, expected_price, drink_name)