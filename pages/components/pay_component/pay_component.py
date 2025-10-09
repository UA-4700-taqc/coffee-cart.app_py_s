"""Component model for the total amount and payment button."""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, DictLocatorType
from pages.components.pay_component.pay_preview_item_component import PayPreviewItemComponent


class PayComponent(BaseComponent):
    """Component responsible for the total amount and payment button."""

    locators: DictLocatorType = {
        "total_pay_button": (By.CLASS_NAME, "pay"),
        "preview_modal": (By.XPATH, "//ul[contains(@class, 'cart-preview')]"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement):
        """Initialize the PayComponent.

        Args:
            driver: Selenium WebDriver instance.
            parent: The root WebElement for the pay component.
        """
        super().__init__(driver, parent)
        self.driver: WebDriver = driver

    @allure.step("Get total price text from Pay button on Menu page")
    def get_total_price_text(self) -> str:
        """Return the raw text of the total amount displayed on the Pay button.

        This is used to verify the displayed price is responsive (Step 3).
        :return: The full text string from the 'Total' button (e.g., "Total: $10.50").
        """
        return self.find_element(self.locators["total_pay_button"]).text

    @allure.step("Get total amount as float from Pay button on Menu page")
    def get_total_amount(self) -> float:
        """Return the total order amount as a float.

        The method uses the Pay/Total button text.
        """
        total_button_text: str = self.get_total_price_text()  # Use the new method
        prefix = "Total: $"
        if total_button_text.startswith(prefix):
            total_button_text = total_button_text.replace(prefix, "", 1)
        return float(total_button_text)

    @allure.step("Click Pay/Total button on Menu page")
    def click_pay(self) -> None:
        """Click the Pay/Total button to proceed with the payment.

        This button also displays the total amount.
        """
        self.find_element(*self.locators["total_pay_button"]).click()

    def pay_preview(self) -> PayPreviewItemComponent:
        """Get the PayPreviewItemComponent for the current pay preview item."""
        pay_preview = self.find_element(self.locators["preview_modal"])
        return PayPreviewItemComponent(self.driver, pay_preview)
