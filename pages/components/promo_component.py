"""Module for PromoComponent UI component."""
from typing import Any

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

    def get_text(self) -> str:
        """Return the text of the promo offer."""
        return WebDriverWait(self.parent, 10).until(EC.presence_of_element_located(self.locators["text"])).text.strip()

    def get_cup(self) -> WebElement:
        """Return the cup component of the promo offer."""
        return WebDriverWait(self.parent, 10).until(EC.presence_of_element_located(self.locators["cup"]))

    def press_yes(self) -> None:
        """Click on 'Yes, of course!' button."""
        self.find_element(self.locators["yes_button"]).click()

    def press_no(self) -> None:
        """Click on 'Nah, I'll skip.' button."""
        self.find_element(self.locators["no_button"]).click()
