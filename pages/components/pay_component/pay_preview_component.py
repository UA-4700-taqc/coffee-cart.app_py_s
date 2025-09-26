"""Implement UI component for the PayPreview cart display."""

import logging
import re
from typing import List, Optional, Tuple

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent
from pages.components.pay_component.pay_preview_item_component import PayPreviewItemComponent

# Initialize logger
logger = logging.getLogger(__name__)


class PayPreviewComponent(BaseComponent):
    """Implement Page Object Model for the cart preview that displays items."""

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
        logger.debug("PayPreviewComponent initialized")

    def get_root_element(self) -> Optional[WebElement]:
        """
        Find and return the root element of the cart preview.

        Returns:
            Optional[WebElement]: Root element or None if not found
        """
        try:
            return self.find_element(self.locators["ROOT"])
        except NoSuchElementException:
            logger.debug("Cart preview root element not found")
            return None
        except StaleElementReferenceException:
            logger.debug("Stale reference to cart preview element, retrying")
            try:
                return self.find_element(self.locators["ROOT"])
            except NoSuchElementException:
                logger.debug("Cart preview root element not found on retry")
                return None

    def get_visible_root_element(self) -> Optional[WebElement]:
        """
        Find and return the visible root element of the cart preview.

        Returns:
            Optional[WebElement]: Visible root element or None if not found
        """
        try:
            return self.find_element(self.locators["VISIBLE_ROOT"])
        except NoSuchElementException:
            logger.debug("Visible cart preview element not found")
            return None
        except StaleElementReferenceException:
            logger.debug("Stale reference to visible cart preview element, retrying")
            try:
                return self.find_element(self.locators["VISIBLE_ROOT"])
            except NoSuchElementException:
                logger.debug("Visible cart preview element not found on retry")
                return None

    def is_visible(self) -> bool:
        """
        Check if the cart preview component is currently visible.

        Returns:
            bool: True if component is visible, False otherwise.
        """
        root_element = self.get_visible_root_element()
        if not root_element:
            logger.debug("Cart preview visibility check: False (element not found)")
            return False

        try:
            is_visible = root_element.is_displayed()
            logger.debug(f"Cart preview visibility check: {is_visible}")
            return is_visible
        except StaleElementReferenceException:
            logger.debug("Stale reference when checking cart visibility, retrying")
            root_element = self.get_visible_root_element()
            is_visible = root_element is not None and root_element.is_displayed()
            logger.debug(f"Cart preview visibility check on retry: {is_visible}")
            return is_visible

    def exists(self) -> bool:
        """
        Check if the cart preview component exists in the DOM.

        Returns:
            bool: True if component exists, False otherwise.
        """
        exists = self.get_root_element() is not None
        logger.debug(f"Cart preview existence check: {exists}")
        return exists

    def get_all_items(self) -> List[PayPreviewItemComponent]:
        """
        Get all items in the cart preview as PayPreviewItemComponent objects.

        Returns:
            List[PayPreviewItemComponent]: List of cart item components.
        """
        if not self.is_visible():
            logger.debug("Cart preview not visible, returning empty item list")
            return []

        root_element = self.get_visible_root_element()
        if not root_element:
            logger.debug("Visible cart preview element not found for items retrieval")
            return []

        # find_elements doesn't throw NoSuchElementException, it returns empty list
        # so we don't need a try/except here
        try:
            item_elements = root_element.find_elements(By.XPATH, self.locators["ITEMS"][1])
            items = []

            for item in item_elements:
                try:
                    items.append(PayPreviewItemComponent(self.driver, item))
                except StaleElementReferenceException:
                    logger.debug("Skipping stale item element in cart")

            logger.debug(f"Found {len(items)} items in cart preview")
            return items
        except StaleElementReferenceException:
            logger.warning("Root element became stale when finding cart items")
            return []

    def get_item_count(self) -> int:
        """
        Get the total number of unique items in the cart.

        Returns:
            int: The number of unique items.
        """
        count = len(self.get_all_items())
        logger.debug(f"Cart contains {count} unique items")
        return count

    def get_item_by_name(self, product_name: str) -> Optional[PayPreviewItemComponent]:
        """
        Find a specific item in the cart by its product name.

        Args:
            product_name: Name of the product to find.

        Returns:
            Optional[PayPreviewItemComponent]: The item component if found, None otherwise.
        """
        for item in self.get_all_items():
            try:
                if item.get_product_name() == product_name:
                    logger.debug(f"Found product '{product_name}' in cart")
                    return item
            except StaleElementReferenceException:
                logger.debug("Stale reference when checking product name")
                continue

        logger.debug(f"Product '{product_name}' not found in cart")
        return None

    def get_total_quantity(self) -> int:
        """
        Get the total quantity of all items in the cart.

        Returns:
            int: Total number of items (sum of all quantities).
        """
        total = 0
        for item in self.get_all_items():
            try:
                quantity = item.get_quantity()
                if quantity:
                    total += quantity
            except StaleElementReferenceException:
                logger.debug("Skipping stale item when calculating total quantity")
                continue

        logger.debug(f"Total quantity of all items in cart: {total}")
        return total

    def is_empty(self) -> bool:
        """
        Check if the cart is empty.

        Returns:
            bool: True if the cart is empty, False otherwise.
        """
        # Performance optimization: First check visibility
        if not self.is_visible():
            logger.debug("Cart empty check: True (not visible)")
            return True

        # If visible, get the root element only once
        root_element = self.get_visible_root_element()
        if not root_element:
            logger.debug("Cart empty check: True (visible root not found)")
            return True

        # Now check for items directly from the root element
        try:
            items = root_element.find_elements(By.XPATH, self.locators["ITEMS"][1])
            is_empty = len(items) == 0
            logger.debug(f"Cart empty check: {is_empty}")
            return is_empty
        except StaleElementReferenceException:
            # If element became stale, fall back to the original method
            logger.debug("Stale element during empty check, using fallback")
            return self.get_item_count() == 0

    def _get_css_property(self, property_name: str) -> str:
        """
        Get CSS property of the root element with stale element handling.

        Args:
            property_name: CSS property name

        Returns:
            str: Property value or empty string if element not found
        """
        root_element = self.get_root_element()
        if not root_element:
            logger.debug(f"Cannot get {property_name} - element not found")
            return ""

        try:
            value = root_element.value_of_css_property(property_name)
            logger.debug(f"Cart preview {property_name}: {value}")
            return value
        except StaleElementReferenceException:
            logger.debug(f"Stale element when getting {property_name}, retrying")
            root_element = self.get_root_element()
            if not root_element:
                return ""
            value = root_element.value_of_css_property(property_name)
            logger.debug(f"Cart preview {property_name} on retry: {value}")
            return value

    def get_background_color(self) -> str:
        """
        Get the background color of the cart preview.

        Returns:
            str: The background color value or empty string if element not found.
        """
        return self._get_css_property("background-color")

    def get_border_color(self) -> str:
        """
        Get the border color of the cart preview.

        Returns:
            str: The border color value or empty string if element not found.
        """
        return self._get_css_property("border-color")

    def get_border_width(self) -> str:
        """
        Get the border width of the cart preview.

        Returns:
            str: The border width value or empty string if element not found.
        """
        return self._get_css_property("border-width")

    def _color_matches(self, actual: str, expected: str) -> bool:
        """
        Check if colors match, handling various formats.

        Args:
            actual: Actual CSS color (could be rgb, rgba, hex, etc.)
            expected: Expected color name or partial value

        Returns:
            bool: True if colors match
        """
        # For empty values
        if not actual or not expected:
            return False

        # Convert expected color name to lower case for comparison
        expected_lower = expected.lower()

        # Direct match for rgb/rgba/hex values
        if expected_lower in actual.lower():
            return True

        # Common color name mappings (add more as needed)
        color_mappings = {
            "beige": ["rgb(245, 245, 220)", "#f5f5dc"],
            "black": ["rgb(0, 0, 0)", "#000000", "#000"],
            "white": ["rgb(255, 255, 255)", "#ffffff", "#fff"],
            # Add other color mappings as needed
        }

        # Check if expected color name has known RGB equivalents
        if expected_lower in color_mappings:
            for color_value in color_mappings[expected_lower]:
                if color_value.lower() in actual.lower():
                    return True

        # Extract RGB values if it's in rgb()/rgba() format
        rgb_match = re.search(r"rgb\((\d+),\s*(\d+),\s*(\d+)", actual)
        if rgb_match and expected_lower in color_mappings:
            for color_value in color_mappings[expected_lower]:
                rgb_expected = re.search(r"rgb\((\d+),\s*(\d+),\s*(\d+)", color_value)
                if rgb_expected:
                    # Allow some tolerance in RGB values (±5)
                    tolerance = 5
                    r1, g1, b1 = map(int, rgb_match.groups())
                    r2, g2, b2 = map(int, rgb_expected.groups())
                    if abs(r1 - r2) <= tolerance and abs(g1 - g2) <= tolerance and abs(b1 - b2) <= tolerance:
                        return True

        return False

    def has_expected_styling(self) -> Tuple[bool, dict]:
        """
        Check if the cart preview has the expected styling (background and border).

        Returns:
            Tuple[bool, dict]:
                - Boolean indicating if all styles match expected values
                - Dictionary with details of style checks (for debugging)
        """
        if not self.exists():
            logger.warning("Cannot check styling - component not found")
            return False, {"error": "Component not found"}

        actual_styles = {
            "background_color": self.get_background_color(),
            "border_color": self.get_border_color(),
            "border_width": self.get_border_width(),
        }

        results = {}
        all_match = True

        # Check each style property
        for key, expected in self.EXPECTED_STYLES.items():
            actual = actual_styles[key]

            # Use improved color matching for color properties
            if "color" in key:
                match = self._color_matches(actual, expected)
            else:
                # For non-color properties like width, use the original containment check
                match = expected in actual

            results[key] = {"expected": expected, "actual": actual, "match": match}
            if not match:
                logger.warning(f"Style mismatch for {key}: expected '{expected}' not in '{actual}'")
                all_match = False

        if all_match:
            logger.debug("All styling checks passed")
        else:
            logger.warning("Some styling checks failed")

        return all_match, results
