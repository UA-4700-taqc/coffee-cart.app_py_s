"""Module for CartItemComponent UI component."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class CartItemComponent(BaseComponent):
    """Empty CartItemComponent class for cart item logic."""

    locators = {"name": (By.XPATH, ".//div")}

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the CartItemComponent with the web driver."""
        super().__init__(driver, parent)
        self.name = self.find_element(self.locators["name"]).text
