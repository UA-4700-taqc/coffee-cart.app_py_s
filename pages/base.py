"""Base classes for page objects and components using Selenium WebDriver."""

import re
from typing import Dict, List, Tuple

import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        self.logger = Logger.get_logger(self.__class__.__name__)

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

    def _parse_height(self, style: str) -> float:
        """Extract the height percentage from a style string using regex."""
        match = re.search(r"height:\s*(\d+(?:\.\d+)?)%", style)
        if match:
            return float(match.group(1))
        return 0.0

    def get_height_percent(self, element: WebElement) -> float:
        """Return the height percentage of an element from its style."""
        style = element.get_attribute("style") or ""
        return self._parse_height(style)

    def get_classes(self, element: WebElement) -> List[str]:
        """Return list of CSS classes from an element."""
        class_attr = element.get_attribute("class") or ""
        return class_attr.split()

    def fill_input(self, element: WebElement, text: str) -> None:
        """Fill input field with reliable clearing."""
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)


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

    @allure.step("Finding single element by locator: {locator}")
    def find_element(self, locator: LocatorType) -> WebElement:
        """
        Find a single element using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.driver.find_element(*locator)

    @allure.step("Finding multiple elements by locator: {locator}")
    def find_elements(self, locator: LocatorType) -> List[WebElement]:
        """
        Find multiple elements using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            list: List of found WebElements.
        """
        return self.driver.find_elements(*locator)

    def wait_for_element_and_click(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        """Wait for the element to become clickable, clicks it, and returns the element."""
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def wait_for_presence_and_get_element(self, locator: Tuple[str, str], timeout: int = 5) -> WebElement:
        """Wait for the element to appear in the DOM."""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))


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

    def _get_height_style(self) -> str:
        """Return the raw style attribute from this component's parent."""
        return self.parent.get_attribute("style") or ""

    def _get_height_percent(self) -> float:
        """Return height percentage of this component."""
        return super().get_height_percent(self.parent)

    def _get_classes(self) -> List[str]:
        """Return CSS classes applied to this component."""
        return super().get_classes(self.parent)

    def hover_on_element(self, element: WebElement) -> None:
        """Hover over a given element using ActionChains."""
        if element:
            self.logger.debug(f"Hovering over element: {element}")
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        else:
            self.logger.debug("Cannot hover: element is None")

    def hover_on(self) -> None:
        """Hover over self using ActionChains."""
        self.logger.debug(f"Hovering over element: {self}")
        actions = ActionChains(self.driver)
        actions.move_to_element(self.parent).perform()
