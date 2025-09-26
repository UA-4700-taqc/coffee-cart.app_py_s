"""Module for CupBodyComponent UI component."""
from typing import Any, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent
from pages.components.cup_component.ingredient_component import IngredientComponent


class CupBodyComponent(BaseComponent):
    """Represents ingredient section inside a cup."""

    locators = {
        "ingredients": (By.CSS_SELECTOR, ".ingredient"),
    }

    def __init__(self, driver: WebDriver, parent: Any) -> None:
        """
        Keyword arguments.

            driver: Selenium WebDriver instance.
            parent: WebElement representing the <div class='cup-body'>.
        """
        super().__init__(driver, parent)
        self.element: WebElement = parent

        self.label: str = self.element.get_attribute("aria-label") or ""

        self.ingredients: List[IngredientComponent] = self._collect_ingredients()

    def _collect_ingredients(self) -> List[IngredientComponent]:
        """Collect all IngredientComponents inside this cup body."""
        try:
            elements = self.find_elements(self.locators["ingredients"])
        except Exception:
            return []

        return [IngredientComponent(self.driver, el) for el in elements]
