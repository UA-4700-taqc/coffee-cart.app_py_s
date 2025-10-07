from pages.menu_page import MenuPage


def test_menu_pay_component(driver_menu_page):
    menu_page = driver_menu_page
    total_sum = menu_page.pay().get_total_amount()
    assert total_sum == 0.0
