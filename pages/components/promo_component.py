"""Module for PromoComponent UI component."""
from typing import Any

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BaseComponent
from pages.components.cup_component.cup_component import CupComponent
from pages.components.cup_component.cup_component_promo import CupComponentPromo


class PromoComponent(BaseComponent):
    """Component representing the promo offer with cup and buttons."""

    locators = {
        "text": (By.XPATH, ".//span"),
        "cup": (By.XPATH, ".//div"),
        "yes_button": (By.XPATH, './/div[@class="buttons"]/button[1]'),
        "no_button": (By.XPATH, './/div[@class="buttons"]/button[2]'),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize the component."""
        super().__init__(driver, parent)

    @allure.step("Get promo offer text")
    def get_text(self) -> str:
        """Return the text of the promo offer."""
        return WebDriverWait(self.parent, 10).until(EC.presence_of_element_located(self.locators["text"])).text.strip()

    @allure.step("Get text of Add button on promo")
    def get_yes_button_text(self) -> str:
        """Return the text of the Add button on the promo offer."""
        return (
            WebDriverWait(self.parent, 10)
            .until(EC.presence_of_element_located(self.locators["yes_button"]))
            .text.strip()
        )

    @allure.step("Get text of Cancel button on promo")
    def get_no_button_text(self) -> str:
        """Return the text of the Cancel button on the promo offer."""
        return (
            WebDriverWait(self.parent, 10)
            .until(EC.presence_of_element_located(self.locators["no_button"]))
            .text.strip()
        )

    @allure.step("Get cup on promo")
    def get_cup(self) -> "CupComponentPromo":
        """Return the cup component of the promo offer."""
        return CupComponentPromo(
            self, WebDriverWait(self.parent, 10).until(EC.visibility_of_element_located(self.locators["cup"]))
        )

    @allure.step("Click Add button on promo")
    def press_yes(self) -> "MenuPage":  # noqa: F821
        """Click on 'Yes, of course!' button."""
        from pages.menu_page import MenuPage

        self.find_element(self.locators["yes_button"]).click()
        return MenuPage(self.driver)

    @allure.step("Click Cancel button on promo")
    def press_no(self) -> "MenuPage":  # noqa: F821
        """Click on 'Nah, I'll skip.' button."""
        from pages.menu_page import MenuPage

        self.find_element(self.locators["no_button"]).click()
        return MenuPage(self.driver)
