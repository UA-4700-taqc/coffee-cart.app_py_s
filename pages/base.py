"""Base classes for page objects and components using Selenium WebDriver."""

from typing import List, Tuple

from selenium.webdriver.common.by import By, ByType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.cart_page import CartPage
from pages.components.header_component import HeaderComponent
from pages.githab_page import GithabPage
from pages.menu_page import MenuPage


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the BasePage.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self._header = HeaderComponent(driver, driver.find_element(By.CSS_SELECTOR, "#app > ul"))

    def go_to_menu_page(self) -> "MenuPage":
        """Navigate to the Menu page and return its page object."""
        self._header.click_menu()
        return MenuPage(self.driver)

    def go_to_cart_page(self) -> "CartPage":
        """Navigate to the Cart page and return its page object."""
        self._header.click_cart()
        return CartPage(self.driver)

    def go_to_github_page(self) -> "GithabPage":
        """Navigate to the GitHub page and return its page object."""
        self._header.click_github()
        return GithabPage(self.driver)

    def find_element(self, locator: Tuple[ByType, str]) -> WebElement:
        """
        Find a single element using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Tuple[ByType, str]) -> List[WebElement]:
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

    def find_element(self, locator: Tuple[ByType, str]) -> WebElement:
        """
        Find a single element within the parent using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            WebElement: The found element.
        """
        return self.parent.find_element(*locator)

    def find_elements(self, locator: Tuple[ByType, str]) -> List[WebElement]:
        """
        Find multiple elements within the parent using the given locator.

        Args:
            locator: Tuple of (By, selector).

        Returns:
            list: List of found WebElements.
        """
        return self.parent.find_elements(*locator)
