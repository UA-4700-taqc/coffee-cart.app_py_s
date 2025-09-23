"""Cart page module."""
from distlib.locators import Page
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage(Page):
    """Cart page object."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the CartPage.

        Args:
            driver: Selenium WebDriver instance.
        """
        super().__init__(driver)
