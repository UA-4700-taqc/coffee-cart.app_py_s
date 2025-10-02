"""Component model for a single item in the shopping cart."""
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class CartItemComponent(BaseComponent):  # Успадкування від BaseComponent
    """Component representing a single product item within the cart list."""

    locators = {
        "name_locator": (By.CSS_SELECTOR, "div:nth-child(1)"),
        "item_total_locator": (By.XPATH, "./div[3]"),
        "quantity_plus_locator": (By.CSS_SELECTOR, "button[aria-label^='Add one']"),
        "quantity_minus_locator": (By.CSS_SELECTOR, "button[aria-label^='Remove one']"),
        "remove_locator": (By.CSS_SELECTOR, "button.delete"),
        "name": (By.XPATH, ".//div"),
        "quantity": (By.XPATH, './/div/span[@class="unit-desc"]'),
        "plus_button": (By.XPATH, ".//div/div[@class='unit-controller']/button[1]"),
        "minus_button": (By.XPATH, ".//div/div[@class='unit-controller']/button[2]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """
        Initialize the cart item component.

        Args:
            driver: The WebDriver instance.
            parent: The parent WebElement (the <li> element) containing the item details.
        """
        super().__init__(driver, parent)
        self.driver = driver
        self.name = self.find_element(self.locators["name"]).text
        self.quantity: int = int(parent.find_element(*self.locators["quantity"]).text.split("x")[1].strip())

    def get_name(self) -> str:
        """Return the name of the product."""
        return self.find_element(self.locators["name_locator"]).text

    def get_total_price(self) -> str:
        """Return the total price of the item."""
        price_text = self.find_element(self.locators["item_total_locator"]).text

        return price_text[1:]

    def increase_quantity(self) -> None:
        """Click the '+' button to increase the item quantity."""
        self.find_element(*self.locators["quantity_plus_locator"]).click()

    def decrease_quantity(self) -> None:
        """Click the '-' button to decrease the item quantity."""
        self.find_element(*self.locators["quantity_minus_locator"]).click()

    def remove_item(self) -> None:
        """Click the 'x' button to remove the item from the cart."""
        self.find_element(*self.locators["remove_locator"]).click()

    def increment_click(self) -> None:
        """Click on the plus button to increase quantity."""
        self.find_element(self.locators["plus_button"]).click()

    def decrement_click(self) -> None:
        """Click on the minus button to decrease quantity."""
        self.find_element(self.locators["minus_button"]).click()
