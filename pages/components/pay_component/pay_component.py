"""Component model for the total amount and payment button."""
from typing import Tuple
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent



class PayComponent(BaseComponent):  # Успадкування від BaseComponent
    """Component responsible for the total amount and payment button."""


    locators = {

        "total_pay_button": (By.CSS_SELECTOR, ".pay-btn"),
    }


    def __init__(self, driver: WebDriver, parent: WebElement):
        """
        Initialize the PayComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent: The root WebElement for the pay component.
        """

        super().__init__(driver, parent)
        self.driver: WebDriver = driver


    def get_total_amount(self) -> str:
        """
        Return the total order amount (as a string).
        The method uses the Pay/Total button text.
        """

        total_button_text: str = self.find_element(*self.locators["total_pay_button"]).text


        prefix = "Total: $"
        if total_button_text.startswith(prefix):
             return total_button_text.replace(prefix, "", 1)

        return total_button_text.replace(prefix, "")

    def click_pay(self) -> None:
        """
        Click the Pay/Total button to proceed with the payment.
        This button also displays the total amount.
        """

        self.find_element(*self.locators["total_pay_button"]).click()