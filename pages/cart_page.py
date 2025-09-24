"""Cart page module."""

from selenium.webdriver.remote.webdriver import WebDriver

from pages.base import BasePage


class CartPage(BasePage):
    """Cart page object."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the CartPage.

        Args:
            driver: Selenium WebDriver instance.
        """
        super().__init__(driver)
