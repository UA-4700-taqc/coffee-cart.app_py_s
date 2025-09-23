"""Menu page for coffee items."""
from typing import Any, List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, BasePage


class CupComponent(BaseComponent):
    """Component representing a single cup item on the menu."""

    locators = {"name": (By.XPATH, ".//h4"), "price": (By.XPATH, ".//h4/small"), "body": (By.CLASS_NAME, "cup")}

    def __init__(self, driver: WebDriver, parent: Any) -> None:
        """
        Initialize the CupComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent: Parent WebElement representing the cup.
        """
        super().__init__(driver, parent)
        self.body: WebElement = self.find_element(self.locators["body"])
        self.name: str = self.find_element(self.locators["name"]).text.split("\n")[0].strip()
        self.price: str = self.find_element(self.locators["price"]).text.strip()


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
            list: List of CupComponent instances.
        """
        cups = self.find_elements(self.locators["cups"])
        return [CupComponent(self.driver, cup) for cup in cups]
