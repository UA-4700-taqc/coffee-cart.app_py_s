"""Module for IngredientComponent UI component."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class IngredientComponent(BaseComponent):
    """Component representing a single ingredient in a cup."""

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)

    def _get_name(self) -> str:
        """Return the ingredient name (text inside the element)."""
        return self.parent.text.strip()

    def get_name(self) -> str:
        """Public method to get the ingredient name."""
        return self._get_name()

    def _get_height_style(self) -> str:
        """Return the value of the 'style' attribute from the parent element."""
        return self.parent.get_attribute("style") or ""

    def _parse_height(self, style: str) -> float:
        """Extract numeric height percentage from style string."""
        import re

        match = re.search(r"height\s*:\s*([\d.]+)%", style)
        if match:
            return float(match.group(1))
        return 0.0

    def _get_height_percent(self) -> float:
        """Return the height percentage parsed from the style attribute."""
        style = self._get_height_style()
        return self._parse_height(style)

    def get_color(self) -> str:
        """Return the background color of the ingredient."""
        return self.parent.value_of_css_property("background-color")