"""Base classes for page objects and components using Selenium WebDriver."""

from typing import List, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver

    def find_element(self, locator: Tuple[By, str]) -> WebElement:
        """
        Find a single element using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Tuple[By, str]) -> List[WebElement]:
        """
        Find multiple elements using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            list: List of found WebElements.
        """
        return self.driver.find_elements(*locator)


class BaseComponent:
    """Base class for all page components."""

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """
        Initialize the BaseComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent page or component.
        """
        self.parent = parent
        self.driver = driver

    def find_element(self, locator: Tuple[By, str]) -> WebElement:
        """
        Find a single element within the parent using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.parent.find_element(*locator)

    def find_elements(self, locator: Tuple[By, str]) -> List[WebElement]:
        """
        Find multiple elements within the parent using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            list: List of found WebElements.
        """
        return self.parent.find_elements(*locator)
