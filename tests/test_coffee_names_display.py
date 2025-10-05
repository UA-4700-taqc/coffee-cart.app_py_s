import pytest

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

@pytest.mark.parametrize("drink_name", test_data)
def test_drink_name_matches_expected(driver_menu_page, drink_name):
    """
    Test to verify the correct display of drink names.
    Checks that the displayed drink name matches the expected name from the test data.
    """

    menu_page = driver_menu_page

    # Find the cup/drink on the page by its name
    cup = menu_page.get_cup_by_name(drink_name)
    assert cup is not None, f"Drink '{drink_name}' was not found"

    # Get the displayed name of the drink
    actual_name = cup.name

    # Check if the displayed name matches the expected one
    assert actual_name == drink_name, (
        f"Expected: '{drink_name}', but got: '{actual_name}'"
    )