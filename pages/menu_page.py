"""Menu page for coffee items."""
from typing import List, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage, DictLocatorType
from pages.components.cup_component.cup_component import CupComponent
from pages.components.promo_component import PromoComponent
from pages.cart_page import CartPage


class MenuPage(BasePage):
    """Coffee menu page."""

    locators: DictLocatorType = {
        "cups": (By.XPATH, "//li/h4/.."),
        "promo": (By.CLASS_NAME, "promo"),
        "add_to_cart_buttons": (By.CSS_SELECTOR, "li .add-to-cart-btn"),
        "total_cart_button": (By.CSS_SELECTOR, "#app > ul > li:nth-child(2)"),
        "total_price_display": (By.CSS_SELECTOR, "#app > div:nth-child(3) > div.pay-container > button"),
        "open_cart_button": (By.CSS_SELECTOR, "#app > ul > li:nth-child(2) > a"),
         }
    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize the MenuPage.

        Args:
            driver: Selenium WebDriver instance.
        """
        super().__init__(driver)



    def add_products_to_cart(self, count: int = 3):
        """
        Click on a specified number of 'Add to Cart' buttons
        """
        add_buttons = self.find_elements(self.locators["add_to_cart_buttons"])

        if not add_buttons:
            self.logger.info("No explicit 'add to cart' buttons found. Clicking on cup components.")
            for i in range(1, min(count, len(self.cups())) + 1):
                self.click_on_cup_by_order(i)
            return

        for i in range(min(count, len(add_buttons))):
            add_buttons[i].click()


    def get_cart_total_price_display(self) -> str:
        """
        Retriev the text of the "Total" price display element
        """
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators["total_price_display"])
        )
        return total_price_element.text

    def open_cart(self) -> CartPage:
        """Clicks the cart icon/Total button and returns the CartPage object."""

        # 1. Чекаємо і клікаємо кнопку кошика
        cart_button = self.wait_for_element_and_click(self.locators["open_cart_button"])

        # 2. ПОВЕРТАЄМО об'єкт CartPage
        return CartPage(self.driver)



    def cups(self) -> List[CupComponent]:
        """
        Get all cup components on the menu page.

        Return:
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
