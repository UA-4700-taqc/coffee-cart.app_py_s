from config.resources import BASE_URL


def test_open_coffe_cart_page(driver):
    driver.get(BASE_URL)
    title = driver.title
    assert title == "Coffee cart"
