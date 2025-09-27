"""Module for PromoComponent UI component."""
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent
from pages.components.cup_component.cup_component import CupComponent


class PromoComponent(BaseComponent):
    """Component representing the promo offer with cup and buttons."""

    locators = {
        "text": (By.XPATH, ".//span[@class='promo-text']"),
        "cup": (By.XPATH, './/div[@class="cup-body"]'),
        "yes_button": (By.XPATH, './/div[@class="buttons"]/button[1]'),
        "no_button": (By.XPATH, './/div[@class="buttons"]/button[2]'),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)
        self.text: str = parent.find_element(*self.locators["text"]).text.strip()
        self.cup: CupComponent = CupComponent(driver, parent.find_element(*self.locators["cup"]))

    def press_yes(self, parent: WebElement) -> None:
        """Click on 'Yes, of course!' button."""
        parent.find_element(*self.locators["yes_button"]).click()

    def press_no(self, parent: WebElement) -> None:
        """Click on 'Nah, I'll skip.' button."""
        parent.find_element(*self.locators["no_button"]).click()
