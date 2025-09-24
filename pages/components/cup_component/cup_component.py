"""Module for CupComponent UI component."""

from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class CupComponent(BaseComponent):
    """Component representing a single cup item on the menu."""

    locators = {"name": (By.XPATH, ".//h4"), "price": (By.XPATH, ".//h4/small"), "body": (By.CLASS_NAME, "cup")}

    def __init__(self, driver: WebDriver, parent: Any) -> None:
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

    def click(self):
        """Click on cup's body."""
        self.body.click()
