"""Module for CupComponent UI component."""

from typing import Any, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent
from pages.components.cup_component.ingredient_component import IngredientComponent


class CupComponent(BaseComponent):
    """Component representing a single cup item on the menu."""

    locators = {
        "name": (By.XPATH, ".//h4"),
        "price": (By.XPATH, ".//h4/small"),
        "body": (By.CLASS_NAME, "cup"),
        "ingredients": (By.CSS_SELECTOR, ".ingredients li"),
    }

    def __init__(self, driver: WebDriver, parent: Any) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)
        self.body: WebElement = self.find_element(self.locators["body"])
        self.name: str = self.find_element(self.locators["name"]).text.split("\n")[0].strip()
        self.price: str = self.find_element(self.locators["price"]).text.strip()
        # Expose ingredients as a field to match the diagram
        self.ingredients: List[IngredientComponent] = self._collect_ingredients()

    def _collect_ingredients(self) -> List[IngredientComponent]:
        """Return list of ingredient components for this cup."""
        try:
            elements = self.find_elements(self.locators["ingredients"])
        except Exception:
            return []

        if not hasattr(IngredientComponent, "__init__") or IngredientComponent.__init__ is object.__init__:
            return []

        try:
            return [IngredientComponent(self.driver, el) for el in elements]
        except Exception:
            return []
