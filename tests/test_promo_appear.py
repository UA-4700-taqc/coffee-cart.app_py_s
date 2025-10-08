import allure

from pages.menu_page import MenuPage


@allure.issue("7")
def test_promo_discount_display(driver_menu_page: MenuPage):
    """Test the business logic for displaying the promotional discount banner on the menu page."""
    menu_page = driver_menu_page

    menu_page.click_on_cup_by_order(1)
    assert not menu_page.is_promo_displayed(), "Step 1 FAILED: Promo displayed after adding 1 item."

    menu_page.click_on_cup_by_order(1)
    assert not menu_page.is_promo_displayed(), "Step 2 FAILED: Promo displayed after adding 2 items."

    menu_page.click_on_cup_by_order(1)
    assert menu_page.is_promo_displayed(), "Step 3 FAILED: Promo not displayed after adding 3 items."

    menu_page.click_on_cup_by_order(1)
    assert not menu_page.is_promo_displayed(), "Step 4 FAILED: Promo displayed after adding 4 items."
