from selenium.webdriver.common.action_chains import ActionChains

from pages.menu_page import MenuPage


def test_menu_pay_component(driver_menu_page):
    menu_page = driver_menu_page
    total_sum = menu_page.pay().get_total_amount()
    assert total_sum == 0.0


def test_total_button_information_is_correct(driver_menu_page):
    menu_page = driver_menu_page
    assert menu_page.pay().get_total_amount() == 0.0
    menu_page.click_on_cup_by_name("Espresso")
    assert menu_page.pay().get_total_amount() == 10.0
    menu_page.click_on_cup_by_name("Mocha")
    assert menu_page.pay().get_total_amount() == 18.0
    menu_page.pay().hover_on()
    menu_page.pay().pay_preview().decrement_click(1)
    assert menu_page.pay().get_total_amount() == 8.0
    menu_page.pay().pay_preview().decrement_click(1)
    assert menu_page.pay().get_total_amount() == 0.0
