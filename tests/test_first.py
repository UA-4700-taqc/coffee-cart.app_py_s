from config.resources import BASE_URL
from pages.menu_page import MenuPage


def test_open_coffe_cart_page(driver):
    driver.get(BASE_URL)
    title = driver.title
    assert title == "Coffee cart"


def test_name_cup(driver):
    driver.get(BASE_URL)
    cups = MenuPage(driver).cups()

    assert cups[0].name == "Espresso"
    assert cups[0].price == "$10.00"
    assert cups[1].name == "Espresso Macchiato"
    assert cups[1].price == "$12.00"
