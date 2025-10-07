"""Module for PayPreviewItemComponent UI component."""
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class PayPreviewItemComponent(BaseComponent):
    """Component representing a single item in the pay preview list."""

    locators = {
        "pay_preview_container": (By.XPATH, "//ul[contains(@class, 'cart-preview')]"),
        "name": (By.XPATH, "//div/span"),
        "quantity": (By.XPATH, '//div/span[@class="unit-desc"]'),
        "plus_button": (By.XPATH, "//div/button[1]"),
        "minus_button": (By.XPATH, "//div/button[2]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)

    def increment_click(self, order) -> None:
        """Click on the plus button to increase quantity."""
        increment_button = self.find_element((By.XPATH, f"//li[{order}]//div/button[1]"))
        increment_button.click()

    def decrement_click(self, order) -> None:
        """Click on the minus button to decrease quantity."""
        decrement_button = self.find_element((By.XPATH, f"//li[{order}]//div/button[2]"))
        decrement_button.click()
