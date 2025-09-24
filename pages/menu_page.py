"""Menu page for coffee items."""
from typing import Any, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base import BasePage
from pages.components.cup_component.cup_component import CupComponent


class MenuPage(BasePage):
    """Coffee menu page."""

    locators = {"cups": (By.XPATH, "//li/h4/..")}

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the MenuPage.

        Args:
            driver: Selenium WebDriver instance.
        """
        super().__init__(driver)

    def cups(self) -> List[CupComponent]:
        """
        Get all cup components on the menu page.

        Returns:
            list: List of cup_component instances.
        """
        cups = self.find_elements(self.locators["cups"])
        return [CupComponent(self.driver, cup) for cup in cups]
