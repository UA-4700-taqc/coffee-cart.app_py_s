"""Base classes for page objects and components using Selenium WebDriver."""

from typing import Dict, List, Tuple

from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utilities.logger import Logger

__all__ = ["BasePage", "BaseComponent", "LocatorType", "DictLocatorType"]

LocatorType = Tuple[ByType, str]
DictLocatorType = Dict[str, LocatorType]


class Base:
    """Utility class for CSS style-related operations."""

    def __init__(self, driver: WebDriver):
        """Initialize Base with a WebDriver instance.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.logger = Logger.get_logger("Base")

    def _get_computed_style(self, element: WebElement, property_name: str) -> str:
        """Get computed CSS style value for an element.

        Args:
            element: WebElement to check
            property_name: CSS property name (use camelCase format)

        Returns:
            str: Computed style value
        """
        self.logger.debug(f"Getting computed style: {property_name}")
        script = "return window.getComputedStyle(arguments[0])[arguments[1]];"
        return self.driver.execute_script(script, element, property_name)

    def get_styles(self, element: WebElement, properties: dict) -> dict:
        """Get multiple computed CSS styles for an element.

        Args:
            element: WebElement to check
            properties: Iterable of property names (camelCase) to retrieve

        Returns:
            dict: Dictionary of property names and their values
        """
        if not element:
            self.logger.debug("Cannot get styles: element is None")
            return {}

        self.logger.debug("Getting multiple styles")
        styles = {}
        for prop in properties:
            styles[prop] = self._get_computed_style(element, prop)
        self.logger.debug(f"Styles retrieved: {styles}")
        return styles


class BasePage(Base):
    """Base class for all page objects."""

    locators: DictLocatorType = {"header": (By.CSS_SELECTOR, "#app > ul")}

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage.

        Args:
            driver: Selenium WebDriver instance.
        """
        from pages.components.header_component import HeaderComponent

        super().__init__(driver)
        header_we = self.driver.find_element(By.CSS_SELECTOR, "#app > ul")
        self._header: HeaderComponent = HeaderComponent(driver, header_we)

    def get_header(self) -> "HeaderComponent":  # noqa=F821
        """Return the Header component."""
        from pages.components.header_component import HeaderComponent

        header_we = self.driver.find_element(By.CSS_SELECTOR, "#app > ul")
        return HeaderComponent(self.driver, header_we)

    def go_to_menu_page(self) -> "MenuPage":  # noqa=F821
        """Navigate to the Menu page and return its page object."""
        self.get_header().click_menu()
        from pages.menu_page import MenuPage

        return MenuPage(self.driver)

    def go_to_cart_page(self) -> "CartPage":  # noqa=F821
        """Navigate to the Cart page and return its page object."""
        self.get_header().click_cart()
        from pages.cart_page import CartPage

        return CartPage(self.driver)

    def go_to_github_page(self) -> "GitHubPage":  # noqa=F821
        """Navigate to the GitHub page and return its page object."""
        self._header.click_github()
        from pages.githab_page import GitHubPage

        return GitHubPage(self.driver)

    def find_element(self, locator: LocatorType) -> WebElement:
        """
        Find a single element using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: LocatorType) -> List[WebElement]:
        """
        Find multiple elements using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            list: List of found WebElements.
        """
        return self.driver.find_elements(*locator)


class BaseComponent(Base):
    """Base class for all page components."""

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """
        Initialize the BaseComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent page or component.
        """
        super().__init__(driver)
        self.parent = parent

    def find_element(self, locator: LocatorType) -> WebElement:
        """
        Find a single element within the parent using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.parent.find_element(*locator)

    def find_elements(self, locator: LocatorType) -> List[WebElement]:
        """
        Find multiple elements within the parent using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            list: List of found WebElements.
        """
        return self.parent.find_elements(*locator)
