"""Module for PayPreviewItemComponent UI component."""
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class PayPreviewItemComponent(BaseComponent):
    """Component representing a single item in the pay preview list."""

    locators = {
        "root": (By.CLASS_NAME, "list-item"),
        "name": (By.XPATH, ".//div/span"),
        "quantity": (By.XPATH, './/div/span[@class, "unit-desc"]'),
        "plus_button": (By.XPATH, ".//div/button[1]"),
        "minus_button": (By.XPATH, ".//div/button[2]"),
    }

    def __init__(self, driver: WebDriver, parent: Any) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)
        self.root: WebElement = self.find_element(*self.locators["root"])
        self.name: str = self.root.find_element(*self.locators["name"]).text.strip()
        self.quantity: int = int(self.root.find_element(*self.locators["quantity"]).text[2:])

    def increment(self) -> None:
        """Click on the plus button to increase quantity."""
        self.root.find_element(*self.locators["plus_button"]).click()
        # self.quantity += 1

    def decrement(self) -> None:
        """Click on the minus button to decrease quantity."""
        self.root.find_element(*self.locators["minus_button"]).click()
        # self.quantity -= 1
