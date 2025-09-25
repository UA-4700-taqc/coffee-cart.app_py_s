"""Component model for the total amount and payment button."""
from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PayComponent:
    """Component responsible for the total amount and payment button."""

    def __init__(self, driver: WebDriver):
        """
        Initialize the PayComponent.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver: WebDriver = driver
        # Locator for the entire PayComponent block, which acts as the total/pay button
        self.total_button_locator: Tuple[By, str] = (By.CSS_SELECTOR, "div.pay-container > button")

    def get_total_amount(self) -> str:
        """Return the total order amount (as a string, excluding 'Total: $')."""
        total_button_text: str = self.driver.find_element(*self.total_button_locator).text
        return total_button_text.replace("Total: $", "")

    def click_pay(self) -> None:
        """Click the 'Pay' button to proceed with the payment."""
        self.driver.find_element(*self.total_button_locator).click()
