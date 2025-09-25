"""Component model for a single item in the shopping cart."""
from typing import Any, List, Tuple  # Added for comprehensive type hinting

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement  # Added for type hinting


class CartItemComponent:
    """Component representing a single product item within the cart list (e.g., a <li> element)."""

    def __init__(self, parent_element: WebElement):
        """
        Initialize the cart item component.

        Args:
            parent_element: The parent WebElement (the <li> element) containing the item details.
        """
        self.parent_element: WebElement = parent_element
        # Locators (all searches are relative to the parent_element)
        self.name_locator: Tuple[By, str] = (By.CSS_SELECTOR, "div:nth-child(1)")
        self.item_total_locator = (By.XPATH, "./div[3]")
        self.quantity_plus_locator: Tuple[By, str] = (By.CSS_SELECTOR, "button[aria-label^='Add one']")
        self.quantity_minus_locator: Tuple[By, str] = (By.CSS_SELECTOR, "button[aria-label^='Remove one']")
        self.remove_locator: Tuple[By, str] = (By.CSS_SELECTOR, "button.delete")

    def get_name(self) -> str:
        """Return the name of the product."""
        return self.parent_element.find_element(*self.name_locator).text

    def get_total_price(self) -> str:
        """Return the total price of the item (as a string)."""
        return self.parent_element.find_element(*self.item_total_locator).text.replace("$", "")

    def increase_quantity(self) -> None:
        """Click the '+' button to increase the item quantity."""
        self.parent_element.find_element(*self.quantity_plus_locator).click()

    def decrease_quantity(self) -> None:
        """Click the '-' button to decrease the item quantity."""
        self.parent_element.find_element(*self.quantity_minus_locator).click()

    def remove_item(self) -> None:
        """Click the 'x' button to remove the item from the cart."""
        self.parent_element.find_element(*self.remove_locator).click()
