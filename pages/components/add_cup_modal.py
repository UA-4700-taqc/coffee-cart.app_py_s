"""Implement UI component for the Add Cup Modal dialog."""

from enum import Enum

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from utilities.logger import Logger

from pages.base import BaseComponent


class ButtonType(Enum):
    """Enum for modal button types."""

    YES = "YES_BUTTON"
    NO = "NO_BUTTON"


class AddCupModal(BaseComponent):
    """AddCupModal class for modal functionality."""

    locators = {
        "ROOT": (By.XPATH, "//dialog[@data-cy='add-to-cart-modal']"),
        "MESSAGE": (By.XPATH, ".//p"),
        "PRODUCT_NAME": (By.XPATH, ".//p/strong"),
        "YES_BUTTON": (By.XPATH, ".//form/button[normalize-space()='Yes']"),
        "NO_BUTTON": (By.XPATH, ".//form/button[normalize-space()='No']"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement = None):
        """Initialize the AddCupModal.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent element containing the modal. If None, the body element is used.
        """
        self.logger = Logger.get_logger("AddCupModal")
        self.logger.debug("Initializing AddCupModal component")

        if parent is None:
            try:
                parent = driver.find_element(*self.locators["ROOT"])
                self.logger.debug("Found modal root element for parent")
            except NoSuchElementException:
                self.logger.debug("Modal root element not found for parent")

        super().__init__(driver, parent)

        try:
            self.root_element = self.find_element(self.locators["ROOT"])
            self.logger.debug("Root element found")
        except NoSuchElementException:
            self.logger.debug("Root element not found")
            self.root_element = None

    def is_open(self) -> bool:
        """Return True if the dialog is displayed and has the 'open' attribute."""
        if not self.root_element:
            self.logger.debug("Modal not open: root element is None")
            return False

        is_displayed = self.root_element.is_displayed()
        has_open_attr = self.root_element.get_attribute("open") is not None
        is_open = is_displayed and has_open_attr

        self.logger.debug(f"Modal open status: {is_open}")
        return is_open

    def get_message_text(self) -> str:
        """Return the full dialog message text.

        Returns:
            str: The message text or empty string if element not found.
        """
        if not self.root_element:
            self.logger.debug("Cannot get message: root element is None")
            return ""

        try:
            message = self.root_element.find_element(By.XPATH, self.locators["MESSAGE"][1]).text
            self.logger.debug(f"Found message text: '{message}'")
            return message
        except NoSuchElementException:
            self.logger.debug("Message element not found")
            return ""

    def get_product_name(self) -> str:
        """Return only the product name from the dialog.

        Returns:
            str: The product name or empty string if element not found.
        """
        if not self.root_element:
            self.logger.debug("Cannot get product name: root element is None")
            return ""

        try:
            product_name = self.root_element.find_element(By.XPATH, self.locators["PRODUCT_NAME"][1]).text
            self.logger.debug(f"Found product name: '{product_name}'")
            return product_name
        except NoSuchElementException:
            self.logger.debug("Product name element not found")
            return ""

    def _get_button_element(self, button_type: ButtonType) -> WebElement:
        """Implement a helper method to get a button element.

        Args:
            button_type: Type of button to retrieve

        Returns:
            WebElement: The button element
        """
        self.logger.debug(f"Getting {button_type.name} button")
        return self.root_element.find_element(By.XPATH, self.locators[button_type.value][1])

    def confirm(self) -> "AddCupModal":
        """
        Click 'Yes' button to add item to cart.

        Returns:
            AddCupModal: Self reference for method chaining.
        """
        self.logger.debug("Attempting to confirm modal")

        if self.root_element:
            try:
                self._get_button_element(ButtonType.YES).click()
                self.logger.debug("Modal confirmed")
            except NoSuchElementException:
                self.logger.debug("Yes button not found")
        else:
            self.logger.debug("Cannot confirm: root element is None")

        return self

    def cancel(self) -> "AddCupModal":
        """
        Click 'No' button to dismiss the modal.

        Returns:
            AddCupModal: Self reference for method chaining.
        """
        self.logger.debug("Attempting to cancel modal")

        if self.root_element:
            try:
                self._get_button_element(ButtonType.NO).click()
                self.logger.debug("Modal canceled")
            except NoSuchElementException:
                self.logger.debug("No button not found")
        else:
            self.logger.debug("Cannot cancel: root element is None")

        return self

    def get_dialog_styles(self) -> dict:
        """
        Get all relevant CSS styles of the dialog.

        Returns:
            dict: Dictionary of CSS properties and their values
        """
        if not self.root_element:
            self.logger.debug("Cannot get dialog styles: root element is None")
            return {}

        properties = {
            "width": "width",
            "height": "height",
            "backgroundColor": "backgroundColor",
            "color": "color",
            "margin": "margin",
            "borderWidth": "borderWidth",
            "padding": "padding",
        }
        return self.get_styles(self.root_element, properties)
