"""Component model for the total amount and payment button."""
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PayComponent:
    """Component responsible for the total amount and payment button."""

    def __init__(self, driver: WebDriver, parent_element: WebElement):
        """
        Initialize the PayComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent_element: The root WebElement for the pay component.
        """
        self.driver: WebDriver = driver
        self.parent_element: WebElement = parent_element
        self.total_button_locator: Tuple[By, str] = (By.CSS_SELECTOR, "button")

    def get_total_amount(self) -> str:
        """Return the total order amount (as a string, excluding 'Total: $')."""
        total_button_text: str = self.parent_element.find_element(*self.total_button_locator).text
        return total_button_text.replace("Total: $", "")

    def click_pay(self) -> None:
        """Click the 'Pay' button to proceed with the payment."""
        self.parent_element.find_element(*self.total_button_locator).click()