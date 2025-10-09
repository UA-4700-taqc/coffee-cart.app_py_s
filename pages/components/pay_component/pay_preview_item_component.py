"""Module for PayPreviewItemComponent UI component."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent


class PayPreviewItemComponent(BaseComponent):
    """Component representing a single item in the pay preview list."""

    locators = {
        "pay_preview_container": (By.XPATH, ".//ul[contains(@class, 'cart-preview')]"),
        "name": (By.XPATH, ".//div/span"),
        "quantity": (By.XPATH, './/div/span[@class="unit-desc"]'),
        "plus_button": (By.XPATH, ".//div/button[1]"),
        "minus_button": (By.XPATH, ".//div/button[2]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)

    @allure.step("Click pay preview '+' button on Menu page")
    def increment_click(self, order) -> None:
        """Click on the plus button to increase quantity."""
        increment_button = self.find_element((By.XPATH, f"//li[{order}]//div/button[1]"))
        increment_button.click()

    @allure.step("Click pay preview '-' button on Menu page")
    def decrement_click(self, order) -> None:
        """Click on the minus button to decrease quantity."""
        decrement_button = self.find_element((By.XPATH, f"//li[{order}]//div/button[2]"))
        decrement_button.click()

    @allure.step("Get item name")
    def get_name(self) -> str:
        """Get the name of the item."""
        name = self.find_element(self.locators["name"]).text
        self.logger.debug(f"Item name: {name}")
        return name

    @allure.step("Get item quantity")
    def get_quantity(self) -> str:
        """Get the quantity description of the item."""
        quantity = self.find_element(self.locators["quantity"]).text
        self.logger.debug(f"Item quantity: {quantity}")
        return quantity
