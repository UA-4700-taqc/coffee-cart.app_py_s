import pytest


def test_promo_banner_information(driver_menu_page):
    """Test promo banner information and ingredients with percentages."""
    promobaner = (
        driver_menu_page.click_on_cup_by_name("Cafe Breve")
        .click_on_cup_by_name("Espresso")
        .click_on_cup_by_order(6)
        .promo()
    )
    assert promobaner.get_text() == "It's your lucky day! Get an extra cup of Mocha for $4."
    assert promobaner.get_yes_button_text() == "Yes, of course!"
    assert promobaner.get_no_button_text() == "Nah, I'll skip."

    cup_element = promobaner.get_cup()
    cup_class = cup_element.body.get_attribute("class")
    assert "cup-body" in cup_class
    assert "disabled-hover" in cup_class

    ingredients = {ing._get_name(): ing._get_height_percent() for ing in cup_element.get_ingredients()}
    expected = {
        "espresso": 30,
        "chocolate syrup": 20,
        "steamed milk": 25,
        "whipped cream": 25,
    }
    for name, percent in expected.items():
        assert name in ingredients
        assert ingredients[name] == pytest.approx(percent)
