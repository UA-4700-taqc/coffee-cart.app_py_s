"""Module for AddCupModal UI component."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class AddCupModal(BaseComponent):
    """AddCupModal class for modal functionality."""

    locators = {
        "ROOT": (By.XPATH, "//dialog[@data-cy='add-to-cart-modal']"),
        "MESSAGE": (By.XPATH, ".//p"),
        "PRODUCT_NAME": (By.XPATH, ".//p/strong"),
        "YES_BUTTON": (By.XPATH, ".//button[normalize-space()='Yes']"),
        "NO_BUTTON": (By.XPATH, ".//button[normalize-space()='No']"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement = None):
        """Initialize the AddCupModal.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent element containing the modal. If None, the body element is used.
        """
        if parent is None:
            parent = driver.find_element(By.TAG_NAME, "body")
        super().__init__(driver, parent)
        self.root_element = self.find_element(self.locators["ROOT"])

    def exists(self) -> bool:
        """Return True if the dialog element is present in DOM."""
        try:
            self.find_element(self.locators["ROOT"])
            return True
        except NoSuchElementException:
            return False

    def is_open(self) -> bool:
        """Return True if the dialog is displayed and has the 'open' attribute."""
        try:
            el = self.find_element(self.locators["ROOT"])
            return el.is_displayed() and el.get_attribute("open") is not None
        except NoSuchElementException:
            return False

    def get_message_text(self) -> str:
        """
        Return the full dialog message text.

        Returns:
            str: The message text or empty string if element not found.

        Raises:
            NoSuchElementException: If modal is not present in DOM.
        """
        try:
            # First check if modal exists
            if not self.exists():
                raise NoSuchElementException("Modal is not present in DOM")

            return self.find_element(self.locators["MESSAGE"]).text
        except NoSuchElementException as e:
            # Log the error or handle differently if needed
            print(f"Could not get message text: {str(e)}")
            return ""  # Return empty string if element not found

    def get_product_name(self) -> str:
        """
        Return only the product name from the dialog.

        Returns:
            str: The product name or empty string if element not found.

        Raises:
            NoSuchElementException: If modal is not present in DOM.
        """
        try:
            # First check if modal exists
            if not self.exists():
                raise NoSuchElementException("Modal is not present in DOM")

            return self.find_element(self.locators["PRODUCT_NAME"]).text
        except NoSuchElementException as e:
            # Log the error or handle differently if needed
            print(f"Could not get product name: {str(e)}")
            return ""  # Return empty string if element not found

    def confirm(self) -> "AddCupModal":
        """Click 'Yes' to add to cart. Returns self."""
        return self.find_element(self.locators["YES_BUTTON"]).click()

    def cancel(self) -> "AddCupModal":
        """Click 'No' to dismiss. Returns self."""
        return self.find_element(self.locators["NO_BUTTON"]).click()
