"""Module for IngredientComponent UI component."""
import re
from typing import Any, List

from selenium.webdriver.remote.webdriver import WebDriver

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
        self.height_percent: float = self._get_height_percent()
        self.classes: List[str] = self._get_classes()

    def _get_name(self) -> str:
        """Return the ingredient name (text inside the element)."""
        return self.parent.text.strip()
