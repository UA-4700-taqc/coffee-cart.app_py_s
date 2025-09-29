"""Implement UI component for the Add Cup Modal dialog."""

from enum import Enum

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

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
        if parent is None:
            parent = driver.find_element(self.locators["ROOT"])
        super().__init__(driver, parent)
        try:
            self.root_element = self.find_element(self.locators["ROOT"])
        except NoSuchElementException:
            self.root_element = None

    def is_open(self) -> bool:
        """Return True if the dialog is displayed and has the 'open' attribute."""
        if not self.root_element:
            return False
        return self.root_element.is_displayed() and self.root_element.get_attribute("open") is not None

    def get_message_text(self) -> str:
        """
        Return the full dialog message text.

        Returns:
            str: The message text or empty string if element not found.

        Raises:
            NoSuchElementException: If modal is not present in DOM.
        """
        if not self.root_element:
            return ""

        try:
            return self.root_element.find_element(By.XPATH, self.locators["MESSAGE"][1]).text
        except NoSuchElementException:
            return ""

    def get_product_name(self) -> str:
        """
        Return only the product name from the dialog.

        Returns:
            str: The product name or empty string if element not found.

        Raises:
            NoSuchElementException: If modal is not present in DOM.
        """
        if not self.root_element:
            return ""

        try:
            return self.root_element.find_element(By.XPATH, self.locators["PRODUCT_NAME"][1]).text
        except NoSuchElementException:
            return ""

    def _get_button_element(self, button_type: ButtonType) -> WebElement:
        """
         Implement a helper method to get a button element.

        Args:
            button_type: Type of button to retrieve

        Returns:
            WebElement: The button element

        Raises:
            NoSuchElementException: If modal is not present or button not found
            ValueError: If invalid button_type provided
        """
        if not self.root_element:
            raise NoSuchElementException("Modal is not present in DOM")

        if not isinstance(button_type, ButtonType):
            raise ValueError(f"button_type must be a ButtonType enum, got {type(button_type)}")

        return self.root_element.find_element(By.XPATH, self.locators[button_type.value][1])

    def confirm(self) -> "AddCupModal":
        """
        Click 'Yes' button to add item to cart.

        Returns:
        AddCupModal: Self reference for method chaining.
        """
        if self.root_element:
            try:
                self._get_button_element(ButtonType.YES).click()
            except NoSuchElementException:
                pass
        return self

    def cancel(self) -> "AddCupModal":
        """Click 'No' to dismiss. Returns self."""
        if self.root_element:
            try:
                self._get_button_element(ButtonType.NO).click()
            except NoSuchElementException:
                pass
        return self

    def get_computed_style(self, element: WebElement, property_name: str) -> str:
        """
        Get computed CSS style value for an element.

        Args:
            element: WebElement to check
            property_name: CSS property name (use camelCase format)

        Returns:
            str: Computed style value
        """
        script = f"return window.getComputedStyle(arguments[0]).{property_name};"
        return self.driver.execute_script(script, element)

    def get_dialog_styles(self) -> dict:
        """
        Get all relevant CSS styles of the dialog.

        Returns:
            dict: Dictionary of CSS properties and their values

        Raises:
            NoSuchElementException: If modal is not present in DOM
        """
        if not self.root_element:
            raise NoSuchElementException("Modal is not present in DOM")

        return {
            "width": self.get_computed_style(self.root_element, "width"),
            "height": self.get_computed_style(self.root_element, "height"),
            "backgroundColor": self.get_computed_style(self.root_element, "backgroundColor"),
            "color": self.get_computed_style(self.root_element, "color"),
            "margin": self.get_computed_style(self.root_element, "margin"),
            "borderWidth": self.get_computed_style(self.root_element, "borderWidth"),
            "padding": self.get_computed_style(self.root_element, "padding"),
        }
