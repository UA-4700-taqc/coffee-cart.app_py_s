"""Module for PayPreviewComponent UI component."""

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from utilities.logger import Logger
from utilities.styles_getter import StylesGetter

from pages.base import BaseComponent
from pages.components.pay_component.pay_preview_item_component import PayPreviewItemComponent


class PayPreviewComponent(BaseComponent):
    """Empty PayPreviewComponent class for payment preview logic."""

    locators = {
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
            driver: Selenium WebDriver instance.
            parent: Parent element (button) that triggers the preview on hover.
        """
        self.logger = Logger.get_logger("PayPreviewComponent")
        self.logger.debug("Initializing PayPreviewComponent")

        super().__init__(driver, parent)
        self.styles_getter = StylesGetter(self.driver)

        try:
            self.root_element = self.find_element(self.locators["ROOT_PREVIEW"])
            self.logger.debug("Root preview element found")
        except NoSuchElementException:
            self.logger.error("Root preview element not found - component may not function correctly")
            self.root_element = None

    def is_visible(self) -> bool:
        """Check if the cart preview is visible (has the 'show' class).

        Returns:
            bool: True if the preview is visible, False otherwise.
        """
        self.logger.debug("Checking if preview is visible")

        if not self.root_element:
            self.logger.debug("Preview not visible: root element is None")
            return False

        try:
            visible_preview = self.find_element(self.locators["VISIBLE_ROOT_PREVIEW"])
            result = visible_preview is not None
            self.logger.debug(f"Preview visibility check result: {result}")
            return result
        except NoSuchElementException:
            self.logger.debug("Preview not visible: no element with 'show' class")
            return False

    def get_items(self) -> list:
        """Get all items in the cart preview.

        Returns:
            list: List of PayPreviewItemComponent objects, empty list if none found.
        """
        self.logger.debug("Getting preview items")

        if not self.is_visible():
            self.logger.debug("Cannot get items: preview is not visible")
            return []

        try:
            item_elements = self.find_elements(self.locators["ITEMS"])
            items_list = []

            for item in item_elements:
                try:
                    items_list.append(PayPreviewItemComponent(self.driver, item))
                except StaleElementReferenceException:
                    self.logger.debug("Skipping stale item element in preview")

            self.logger.debug(f"Found {len(items_list)} items in preview")
            return items_list
        except StaleElementReferenceException:
            self.logger.warning("Root element became stale when finding preview items")
            return []

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
        if not self.root_element:
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
        return self.styles_getter.get_styles(self.root_element, properties)
