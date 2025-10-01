"""Module for CartItemComponent UI component."""
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class CartItemComponent(BaseComponent):
    """Empty CartItemComponent class for cart item logic."""

    locators = {
        "name": (By.XPATH, ".//div"),
        "quantity": (By.XPATH, './/div/span[@class="unit-desc"]'),
        "plus_button": (By.XPATH, ".//div/div[@class='unit-controller']/button[1]"),
        "minus_button": (By.XPATH, ".//div/div[@class='unit-controller']/button[2]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the CartItemComponent with the web driver."""
        super().__init__(driver, parent)
        self.name = self.find_element(self.locators["name"]).text
        self.quantity: int = int(parent.find_element(*self.locators["quantity"]).text.split("x")[1].strip())

    def increment_click(self) -> None:
        """Click on the plus button to increase quantity."""
        self.find_element(self.locators["plus_button"]).click()

    def decrement_click(self) -> None:
        """Click on the minus button to decrease quantity."""
        self.find_element(self.locators["minus_button"]).click()
