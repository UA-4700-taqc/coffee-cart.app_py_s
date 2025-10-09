import time


def test_name_double_click_translation(driver_menu_page, driver):
    expected = {
        "Espresso": "特浓咖啡",
        "Espresso Macchiato": "浓缩玛奇朵",
        "Cappuccino": "卡布奇诺",
        "Mocha": "摩卡",
        "Flat White": "平白咖啡",
        "Americano": "美式咖啡",
        "Cafe Latte": "拿铁",
        "Espresso Con Panna": "浓缩康宝蓝",
        "Cafe Breve": "半拿铁",
    }

    for i, (key, value) in enumerate(expected.items()):
        cup = driver_menu_page.cups()[i]
        cup.double_click_on_cup_name()
        assert cup.get_name() == value, (
            f"Expected translation for '{key}' to be '{value}', " f"but got '{cup.get_name()}'"
        )
