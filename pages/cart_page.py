"""Cart page module."""

from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BasePage, DictLocatorType
from pages.components.cart_item_component import CartItemComponent
from pages.components.pay_component.pay_component import PayComponent


class CartPage(BasePage):
    """Cart page object."""

    locators: DictLocatorType = {
        "cart_root": (By.CSS_SELECTOR, "div.list"),
        "items": (By.CSS_SELECTOR, "div.list ul:not(.cart-preview) > li.list-item"),
        "pay_container": (By.CSS_SELECTOR, "div.pay-container"),
        "empty_cart": (By.XPATH, "//p[text()='No coffee, go add some.']"),
    }

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the CartPage.

        Args:
            driver: Selenium WebDriver instance.
        """
        super().__init__(driver)

    def _root(self) -> WebElement:
        """Return the root container for the cart page content."""
        return self.find_element(self.locators["cart_root"])

    def items(self) -> List[CartItemComponent]:
        """Return list of cart item components."""
        root = self._root()
        elements = root.find_elements(*self.locators["items"])
        return [CartItemComponent(self.driver, el) for el in elements]

    def pay(self) -> PayComponent:
        """Return the pay component for the cart page."""
        root = self._root()
        pay_element = root.find_element(*self.locators["pay_container"])
        return PayComponent(self.driver, pay_element)

    def clear_cart(self) -> "CartPage":
        """Delete all cart elements if there are any."""
        for item in self.items():
            item.remove_item()
        return self

    def get_empty_cart_we(self) -> WebElement | None:
        """Return empty cart web element if found or None."""
        try:
            return self.find_element(self.locators["empty_cart"])
        except NoSuchElementException:
            return None

    def is_empty_cart_displayed(self) -> bool:
        """Return True if empty cart web element is displayed."""
        if self.get_empty_cart_we():
            if self.get_empty_cart_we().is_displayed():
                return True
        return False
