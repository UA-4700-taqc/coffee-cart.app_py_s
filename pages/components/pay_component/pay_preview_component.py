"""Module for PayPreviewComponent UI component."""

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, DictLocatorType
from pages.components.pay_component.pay_preview_item_component import PayPreviewItemComponent


class PayPreviewComponent(BaseComponent):
    """Empty PayPreviewComponent class for payment preview logic."""

    locators: DictLocatorType = {
        "ROOT_PREVIEW": (By.XPATH, "//ul[contains(@class, 'cart-preview')]"),
        "VISIBLE_ROOT_PREVIEW": (
            By.XPATH,
            "//ul[contains(@class, 'cart-preview') and contains(@class, 'show')]",
        ),
        "ITEMS": (By.XPATH, ".//li[contains(@class, 'list-item')]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement = None):
        """Initialize the PayPreviewComponent.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            parent (WebElement, optional): Parent element that triggers the preview on hover.
        """
        super().__init__(driver, parent)
        self.logger.debug("Initializing PayPreviewComponent")

        self.parent = self.find_element(self.locators["ROOT_PREVIEW"])

    def is_visible(self) -> bool:
        """Check if the cart preview is visible (has the 'show' class).

        Returns:
            bool: True if the preview is visible, False otherwise.
        """
        self.logger.debug("Checking if preview is visible")

        if not self.parent:
            self.logger.debug("Preview not visible: root element is None")
            return False

        visible_preview = self.find_element(self.locators["VISIBLE_ROOT_PREVIEW"])
        result = visible_preview is not None
        self.logger.debug(f"Preview visibility check result: {result}")
        return result

    def get_items(self) -> list:
        """Get all items in the cart preview.

        Returns:
            list: List of PayPreviewItemComponent objects, empty list if none found.
        """
        self.logger.debug("Getting preview items")

        item_elements = self.find_elements(self.locators["ITEMS"])
        items_list = []

        for item in item_elements:
            try:
                items_list.append(PayPreviewItemComponent(self.driver, item))
            except StaleElementReferenceException:
                self.logger.debug("Skipping stale item element in preview")

        self.logger.debug(f"Found {len(items_list)} items in preview")
        return items_list

    def get_item_count(self) -> int:
        """Get the number of items in the cart preview.

        Returns:
            int: Number of items in the preview, 0 if none or preview not visible.
        """
        self.logger.debug("Getting item count")

        items = self.get_items()
        count = len(items)
        self.logger.debug(f"Item count: {count}")
        return count

    def get_preview_styles(self) -> dict:
        """Get all relevant CSS styles of the cart preview.

        Returns:
            dict: Dictionary of CSS properties and their values
        """
        if not self.parent:
            self.logger.debug("Cannot get preview styles: root element is None")
            return {}

        properties = {
            "padding": "padding",
            "background": "background",
            "marginBottom": "marginBottom",
            "border": "border",
            "listStyle": "listStyle",
            "minWidth": "minWidth",
        }
        return self.get_styles(self.parent, properties)
