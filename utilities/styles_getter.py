"""Utility module for handling CSS style operations."""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from utilities.logger import Logger


class StylesGetter:
    """Utility class for CSS style-related operations."""

    def __init__(self, driver: WebDriver):
        """Initialize StylesGetter with a WebDriver instance.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.logger = Logger.get_logger("StylesGetter")

    def get_computed_style(self, element: WebElement, property_name: str) -> str:
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
            properties: Dict where keys are property names (camelCase) to retrieve

        Returns:
            dict: Dictionary of property names and their values
        """
        if not element:
            self.logger.debug("Cannot get styles: element is None")
            return {}

        self.logger.debug("Getting multiple styles")
        styles = {}
        for prop in properties:
            styles[prop] = self.get_computed_style(element, prop)
        self.logger.debug(f"Styles retrieved: {styles}")
        return styles
