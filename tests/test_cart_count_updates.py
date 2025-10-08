import allure
from selenium.webdriver.common.by import By


@allure.feature("Cart")
@allure.issue("TEST-1", "Cart count updates when adding items")
def test_cart_count_updates(driver_menu_page):
    """Verify cart count in header updates when adding items."""
    menu_page = driver_menu_page
    driver = menu_page.driver

    def get_cart_count():
        cart_text = driver.find_element(By.CSS_SELECTOR, "#app ul li:nth-child(2) a").text
        return int(cart_text.strip().split("(")[1].split(")")[0])

    menu_page.click_on_cup_by_name("Espresso")
    assert get_cart_count() == 1

    menu_page.click_on_cup_by_name("Cappuccino")
    assert get_cart_count() == 2


@allure.feature("Cart")
@allure.issue("TEST-2", "Empty cart message")
def test_cart_empty_message_after_clear(driver_menu_page):
    """Verify empty cart message is displayed after clearing cart."""
    menu_page = driver_menu_page
    cart_page = (
        menu_page.click_on_cup_by_name("Cappuccino").click_on_cup_by_name("Espresso").go_to_cart_page().clear_cart()
    )
    assert cart_page.is_empty_cart_displayed()


@allure.feature("Cart")
@allure.issue("TEST-3", "Initially empty cart message")
def test_initially_empty_cart(driver_menu_page):
    """Verify empty cart message is displayed when cart is initially empty."""
    menu_page = driver_menu_page
    cart_page = menu_page.go_to_cart_page().clear_cart()
    assert cart_page.is_empty_cart_displayed()


@allure.feature("Cart")
@allure.issue("TEST-4", "Non-empty cart message")
def test_non_empty_cart(driver_menu_page):
    """Verify empty cart message is not displayed when cart has items."""
    menu_page = driver_menu_page
    cart_page = menu_page.click_on_cup_by_name("Cappuccino").click_on_cup_by_name("Espresso").go_to_cart_page()
    assert not cart_page.is_empty_cart_displayed()
