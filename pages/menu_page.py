"""Menu page for coffee items."""
from typing import List, Optional

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.resources import IMPLICIT_WAIT
from pages.base import BasePage, DictLocatorType
from pages.components.cup_component.cup_component import CupComponent
from pages.components.pay_component.pay_component import PayComponent
from pages.components.promo_component import PromoComponent


class MenuPage(BasePage):
    """Coffee menu page."""

    locators: DictLocatorType = {
        "cups": (By.XPATH, "//li/h4/.."),
        "promo": (By.CLASS_NAME, "promo"),
        "pay_container": (By.CSS_SELECTOR, "div.pay-container"),
        "pay_button": (By.CSS_SELECTOR, "button.pay"),
        "pay_modal": (By.CSS_SELECTOR, "div.modal"),
        "success_snackbar": (By.CSS_SELECTOR, "div.snackbar"),
    }

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

    def pay(self) -> PayComponent:
        """
        Get the pay component.

        Returns:
            PayComponent.
        """
        pay = self.find_element(self.locators["pay_container"])
        return PayComponent(self.driver, pay)
    def click_pay_button(self) -> "PaymentDetailsModal":  # noqa=F821
        """
        Click on pay button.

        Returns:
            Instance of PaymentDetailsModal.
        """
        from pages.components.payment_details_modal import PaymentDetailsModal

        self.find_element(self.locators["pay_button"]).click()
        pay_modal_we = self.find_element(self.locators["pay_modal"])
        return PaymentDetailsModal(self.driver, pay_modal_we)

    def get_snackbar_success_we(self) -> WebElement | None:
        """
        Wait until the success snack bar becomes visible (style='') and return it.

        Returns:
            WebElement | None: if not visible.
        """
        try:
            self.driver.implicitly_wait(0)
            WebDriverWait(self.driver, 5).until(
                lambda wd: (wd.find_element(*self.locators["success_snackbar"]).get_attribute("style") or "") == ""
            )
            return self.find_element(self.locators["success_snackbar"])
        except (NoSuchElementException, TimeoutException):
            return None
        finally:
            self.driver.implicitly_wait(IMPLICIT_WAIT)
