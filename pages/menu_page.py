"""Menu page for coffee items."""
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from pages.base import BasePage, DictLocatorType
from pages.components.cup_component.cup_component import CupComponent
from pages.components.promo_component import PromoComponent


class MenuPage(BasePage):
    """Coffee menu page."""

    locators: DictLocatorType = {"cups": (By.XPATH, "//li/h4/.."), "promo": (By.CLASS_NAME, "promo")}

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

    def get_cup_by_name(self, cup_name: str) -> Optional[CupComponent]:
        """
        Find cup by its name from the list of cups.

        Args:
            cup_name: name of cup to find.

        Return:
            Instance of CupComponent with specific cup's name.
        """
        for cup in self.cups():
            if cup.name == cup_name:
                return cup

    def click_on_cup_by_name(self, cup_name: str) -> "MenuPage":
        """
        Click on cup with specific name.

        Args:
            cup_name: name of cup to click on.
        """
        cup = self.get_cup_by_name(cup_name)
        cup.click()
        return self

    def click_on_cup_by_order(self, order: int) -> "MenuPage":
        """
        Click on cup with specific number on the page.

        Args:
            order: cup to click on.
        """
        cups = self.cups()
        cups[order - 1].click()
        return self

    def promo(self) -> PromoComponent:
        """
        Get the promo banner component.

        Returns:
            PromoComponent: The promo banner.
        """
        promo = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators["promo"]))
        return PromoComponent(self.driver, promo)



    def is_promo_displayed(self, timeout: int = 5) -> bool:
        """
       Check if the promo element is visible
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.locators["promo"])
            )
            return True
        except TimeoutException:
            return False