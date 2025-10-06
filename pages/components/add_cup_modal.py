"""Implement UI component for the Add Cup Modal dialog."""

from enum import Enum
from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, DictLocatorType

if TYPE_CHECKING:
    from pages.menu_page import MenuPage


class ButtonType(Enum):
    """Enum for modal button types."""

    YES = "YES_BUTTON"
    NO = "NO_BUTTON"


class AddCupModal(BaseComponent):
    """AddCupModal class for modal functionality."""

    locators: DictLocatorType = {
        "ROOT": (By.XPATH, "//dialog[@data-cy='add-to-cart-modal']"),
        "MESSAGE": (By.XPATH, ".//p"),
        "PRODUCT_NAME": (By.XPATH, ".//p/strong"),
        "YES_BUTTON": (By.XPATH, ".//form/button[normalize-space()='Yes']"),
        "NO_BUTTON": (By.XPATH, ".//form/button[normalize-space()='No']"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement = None):
        """Initialize AddCupModal.

        Args:
            driver (WebDriver): Selenium WebDriver instance.
            parent (WebElement, optional): Parent element containing the modal.
        """
        if parent is None:
            parent = driver.find_element(*self.locators["ROOT"])
        super().__init__(driver, parent)
        self.logger.debug("Initializing AddCupModal component")

    def is_open(self) -> bool:
        """Check if the dialog is open.

        Returns:
            bool: True if the dialog is displayed and has the 'open' attribute.
        """
        if not self.parent:
            self.logger.debug("Modal not open: root element is None")
            return False

        is_displayed = self.parent.is_displayed()
        has_open_attr = self.parent.get_attribute("open")
        is_open = is_displayed and has_open_attr

        self.logger.debug(f"Modal open status: {is_open}")
        return is_open

    def get_message_text(self) -> str:
        """Get the full dialog message text.

        Returns:
            str: Message text, or empty string if not found.
        """
        message = self.parent.find_element(By.XPATH, self.locators["MESSAGE"][1]).text
        self.logger.debug(f"Found message text: '{message}'")
        return message

    def get_product_name(self) -> str:
        """Get the product name from the dialog.

        Returns:
            str: Product name, or empty string if not found.
        """
        product_name = self.parent.find_element(By.XPATH, self.locators["PRODUCT_NAME"][1]).text
        self.logger.debug(f"Found product name: '{product_name}'")
        return product_name

    def _get_button_element(self, button_type: ButtonType) -> WebElement:
        """Get a button element by type.

        Args:
            button_type (ButtonType): Type of button to retrieve.

        Returns:
            WebElement: The button element.
        """
        self.logger.debug(f"Getting {button_type.name} button")
        return self.parent.find_element(By.XPATH, self.locators[button_type.value][1])

    def confirm(self) -> "MenuPage":
        """Click 'Yes' to add item to cart.

        Returns:
            MenuPage: The menu page after confirming.
        """
        from pages.menu_page import MenuPage

        self.logger.debug("Attempting to confirm modal")

        self._get_button_element(ButtonType.YES).click()
        self.logger.debug("Modal confirmed")
        return MenuPage(driver=self.driver)

    def cancel(self) -> "MenuPage":
        """Click 'No' to dismiss the modal.

        Returns:
            MenuPage: The menu page after canceling.
        """
        from pages.menu_page import MenuPage

        self.logger.debug("Attempting to cancel modal")

        self._get_button_element(ButtonType.NO).click()
        self.logger.debug("Modal canceled")

        return MenuPage(driver=self.driver)

    def get_dialog_styles(self) -> dict:
        """Get CSS styles of the dialog.

        Returns:
            dict: CSS properties and their values.
        """
        properties = {
            "position": "position",
            "display": "display",
            "backgroundColor": "background-color",
            "borderStyle": "border-style",
            "borderColor": "border-color",
            "borderWidth": "border-width",
            "padding": "padding",
        }
        return self.get_styles(self.parent, properties)

    def get_yes_button_styles(self) -> dict:
        """Get CSS styles of Yes button.

        Returns:
            dict: CSS properties and their values.
        """
        properties = {
            "cursor": "cursor",
            "backgroundColor": "background-color",
            "color": "color",
            "borderRadius": "border-radius",
            "padding": "padding",
        }
        yes_button = self._get_button_element(ButtonType.YES)
        styles = self.get_styles(yes_button, properties)
        self.logger.debug(f"Yes button styles: {styles}")
        return styles

    def get_no_button_styles(self) -> dict:
        """Get CSS styles of No button.

        Returns:
            dict: CSS properties and their values.
        """
        properties = {
            "cursor": "cursor",
            "backgroundColor": "background-color",
            "color": "color",
            "borderRadius": "border-radius",
            "padding": "padding",
        }
        no_button = self._get_button_element(ButtonType.NO)
        styles = self.get_styles(no_button, properties)
        self.logger.debug(f"No button styles: {styles}")
        return styles
