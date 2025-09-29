"""Module for IngredientComponent UI component."""
import re
from typing import Any, List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class IngredientComponent(BaseComponent):
    """Represents a single ingredient inside a cup."""

    def __init__(self, driver: WebDriver, parent: Any) -> None:
        """Initialize ingredient component.

        Keyword arguments:
        driver -- Selenium WebDriver instance
        parent -- WebElement representing the ingredient <div>

        Return: None
        """
        super().__init__(driver, parent)

        self.name: str = self._get_name()
        self.height_style: str = self._get_height_style()
        self.height_percent: float = self._get_height_percent()
        self.classes: List[str] = self._get_classes()

    def _get_name(self) -> str:
        """Return the ingredient name (text inside the element)."""
        return self.parent.text.strip()

    def _get_height_style(self) -> str:
        """Return the style attribute of the ingredient."""
        return self.parent.get_attribute("style") or ""

    def _get_height_percent(self) -> float:
        """Return the height percentage parsed from the style attribute."""
        return self._parse_height(self._get_height_style())

    def _get_classes(self) -> List[str]:
        """Return the list of CSS classes applied to the ingredient."""
        class_attr = self.parent.get_attribute("class") or ""
        return class_attr.split()

    def _parse_height(self, style: str) -> float:
        """Extract the height percentage from a style string using regex."""
        match = re.search(r"height:\s*(\d+(?:\.\d+)?)%", style)
        if match:
            return float(match.group(1))
        return 0.0
