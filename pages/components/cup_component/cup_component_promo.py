"""Module for CupComponent UI component."""

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, DictLocatorType
from pages.components.cup_component.ingredient_component import IngredientComponent


class CupComponentPromo(BaseComponent):
    """Component representing a single cup item on the menu."""

    locators: DictLocatorType = {
        "body": (By.CSS_SELECTOR, ".cup-body.disabled-hover"),
        "ingredient": (By.XPATH, ".//div[starts-with(@class, 'ingredient')]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """
        Initialize the cup_component.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent WebElement representing the cup.
        """
        super().__init__(driver, parent)
        self.body: WebElement = self.find_element(self.locators["body"])
        self.ingredients: List[IngredientComponent] = self.get_ingredients()

    def get_ingredients(self) -> List[IngredientComponent]:
        """Return list of ingredient components for this cup."""
        elements = self.find_elements(self.locators["ingredient"])
        return [IngredientComponent(self.driver, el) for el in elements]
