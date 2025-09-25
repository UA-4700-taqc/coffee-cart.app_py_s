"""Page object model for the main shopping cart view."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base import BasePage
from pages.components.cart_item_component import CartItemComponent
from pages.components.pay_component import PayComponent


class CartPage(BasePage):
    """Cart page object."""

    URL = "https://coffee-cart.app/cart"

    # Використовуйте словник 'locators' для централізованого зберігання
    locators = {"item_list": (By.CSS_SELECTOR, "ul.list > li.list-item")}

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the CartPage.

        Args:
            driver: Selenium WebDriver instance.
        """
        super().__init__(driver)
        # зберігаємо локатор у змінній екземпляра
        self.item_list_locator = self.locators["item_list"]
        # iніціалізуємо компонент PayComponent на сторінці
        self.pay_component = PayComponent(driver)

    def open(self) -> "CartPage":
        """Open the cart page."""
        self.driver.get(self.URL)
        return self

    def get_all_cart_items(self):
        """Find all cart item elements and wrap them in CartItemComponent objects."""
        # 1. Find all <li> elements
        item_elements = self.driver.find_elements(*self.item_list_locator)

        # 2. Create CartItemComponent objects from these elements
        return [CartItemComponent(el) for el in item_elements]

    def get_pay_component(self) -> PayComponent:
        """Return the PayComponent object."""
        return self.pay_component
