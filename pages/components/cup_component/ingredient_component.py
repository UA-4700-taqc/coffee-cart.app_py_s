"""Module for IngredientComponent UI component."""
from typing import Any, List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class IngredientComponent:
    """Represents a single ingredient inside a cup."""

    def __init__(self, driver: WebDriver, parent: Any) -> None:
        """Initialize ingredient component.

        Keyword arguments:
        driver -- Selenium WebDriver instance
        parent -- WebElement representing the ingredient <div>

        Return: None
        """
        super().__init__(driver, parent)
        self.element: WebElement = parent

        self.name: str = self.element.text.strip()
        self.height_style: str = self.element.get_attribute("style") or ""

        self.height_percent: float = self._parse_height(self.height_style)

        class_attr = self.element.get_attribute("class") or ""
        self.classes: List[str] = class_attr.split()

    @staticmethod
    def _parse_height(style: str) -> float:
        if "height" in style:
            num = style.split(":")[1].strip().replace(";", "").replace("%", "")
            try:
                return float(num)
            except ValueError:
                return 0.0
        return 0.0
