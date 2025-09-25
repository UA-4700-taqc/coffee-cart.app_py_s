"""Module for PayPreviewComponent UI component."""

from typing import List, Optional, Tuple

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent
from pages.components.pay_component.pay_preview_item_component import PayPreviewItemComponent


class PayPreviewComponent(BaseComponent):
    """Component representing the cart preview that displays items in the cart."""

    locators = {
        "ROOT": (By.XPATH, "//ul[contains(@class, 'cart-preview')]"),
        "VISIBLE_ROOT": (
            By.XPATH,
            "//ul[contains(@class, 'cart-preview') and contains(@class, 'show')]",
        ),
        "ITEMS": (By.XPATH, ".//li[contains(@class, 'list-item')]"),
    }

    EXPECTED_STYLES = {
        "background_color": "beige",
        "border_color": "black",
        "border_width": "4px",
    }

    def __init__(self, driver: WebDriver, parent: WebElement):
        """
        Initialize the PayPreviewComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent element containing this component.
        """
        super().__init__(driver, parent)

    def is_visible(self) -> bool:
        """
        Check if the cart preview component is currently visible.

        Returns:
            bool: True if component is visible, False otherwise.
        """
        try:
            return self.find_element(self.locators["VISIBLE_ROOT"]).is_displayed()
        except NoSuchElementException:
            return False

    def exists(self) -> bool:
        """
        Check if the cart preview component exists in the DOM.

        Returns:
            bool: True if component exists, False otherwise.
        """
        try:
            self.find_element(self.locators["ROOT"])
            return True
        except NoSuchElementException:
            return False

    def get_all_items(self) -> List[PayPreviewItemComponent]:
        """
        Get all items in the cart preview as PayPreviewItemComponent objects.

        Returns:
            List[PayPreviewItemComponent]: List of cart item components.
        """
        if not self.is_visible():
            return []

        items = []
        try:
            item_elements = self.find_elements(self.locators["ITEMS"])
            for item_element in item_elements:
                items.append(PayPreviewItemComponent(self.driver, item_element))
            return items
        except NoSuchElementException:
            return []

    def get_item_count(self) -> int:
        """
        Get the total number of unique items in the cart.

        Returns:
            int: The number of unique items.
        """
        if not self.is_visible():
            return 0

        try:
            items = self.find_elements(self.locators["ITEMS"])
            return len(items)
        except NoSuchElementException:
            return 0

    def get_item_by_name(self, product_name: str) -> Optional[PayPreviewItemComponent]:
        """
        Find a specific item in the cart by its product name.

        Args:
            product_name: Name of the product to find.

        Returns:
            Optional[PayPreviewItemComponent]: The item component if found, None otherwise.
        """
        for item in self.get_all_items():
            if item.get_product_name() == product_name:
                return item
        return None

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all items in the cart.

        Returns:
            int: Total number of items (sum of all quantities).
        """
        total = 0
        for item in self.get_all_items():
            quantity = item.get_quantity()
            if quantity:
                total += quantity
        return total

    def is_empty(self) -> bool:
        """
        Check if the cart is empty.

        Returns:
            bool: True if the cart is empty, False otherwise.
        """
        return not self.is_visible() or self.get_item_count() == 0

    def get_background_color(self) -> str:
        """
        Get the background color of the cart preview.

        Returns:
            str: The background color value or empty string if element not found.
        """
        try:
            element = self.find_element(self.locators["ROOT"])
            return element.value_of_css_property("background-color")
        except NoSuchElementException:
            return ""

    def get_border_color(self) -> str:
        """
        Get the border color of the cart preview.

        Returns:
            str: The border color value or empty string if element not found.
        """
        try:
            element = self.find_element(self.locators["ROOT"])
            return element.value_of_css_property("border-color")
        except NoSuchElementException:
            return ""

    def get_border_width(self) -> str:
        """
        Get the border width of the cart preview.

        Returns:
            str: The border width value or empty string if element not found.
        """
        try:
            element = self.find_element(self.locators["ROOT"])
            return element.value_of_css_property("border-width")
        except NoSuchElementException:
            return ""

    def has_expected_styling(self) -> Tuple[bool, dict]:
        """
        Check if the cart preview has the expected styling (background and border).

        Returns:
            Tuple[bool, dict]:
                - Boolean indicating if all styles match expected values
                - Dictionary with details of style checks (for debugging)
        """
        if not self.exists():
            return False, {"error": "Component not found"}

        actual_styles = {
            "background_color": self.get_background_color(),
            "border_color": self.get_border_color(),
            "border_width": self.get_border_width(),
        }

        # Note: Browsers may return colors in different formats (rgb, rgba, hex)
        # For robust testing, consider using color conversion utilities
        # or checking if expected values are contained within actual values

        results = {}
        all_match = True

        # Check each style property
        for key, expected in self.EXPECTED_STYLES.items():
            actual = actual_styles[key]
            match = expected in actual
            results[key] = {"expected": expected, "actual": actual, "match": match}
            if not match:
                all_match = False

        return all_match, results
