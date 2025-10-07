"""Module for CupComponent UI component."""

from typing import List, Optional

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, DictLocatorType
from pages.components.cup_component.ingredient_component import IngredientComponent


class CupComponent(BaseComponent):
    """Component representing a single cup item on the menu."""

    locators: DictLocatorType = {
        "name": (By.XPATH, ".//h4"),
        "price": (By.XPATH, ".//h4/small"),
        "body": (By.CLASS_NAME, "cup-body"),
        "ingredients": (By.CLASS_NAME, "ingredient"),
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
        self.name: str = self.find_element(self.locators["name"]).text.split("\n")[0].strip()
        self.price: str = self.find_element(self.locators["price"]).text.strip()
        self.ingredients: List[IngredientComponent] = self.get_ingredients()

    @allure.step("click on cup")
    def click(self):
        """Click on cup's body."""
        self.body.click()

    def get_ingredients(self) -> List[IngredientComponent]:
        """Return list of ingredient components for this cup."""
        ingredients_elements = self.body.find_elements(*self.locators["ingredients"])
        return [IngredientComponent(self.driver, el) for el in ingredients_elements]

    def get_ingredient_by_name(self, ingredient_name: str) -> Optional["IngredientComponent"]:
        """Return ingredient component by its name, or None if not found."""
        for ingredient in self.ingredients:
            if ingredient.get_name().lower() == ingredient_name.lower():
                return ingredient
        return None
