"""Module for PaymentDetailsModal UI component."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import BaseComponent, DictLocatorType
from pages.menu_page import MenuPage
from test_data.users import User


class PaymentDetailsModal(BaseComponent):
    """PaymentDetailsModal class for payment details modal logic."""

    locators: DictLocatorType = {
        "header": (By.CSS_SELECTOR, "h1"),
        "name_input": (By.CSS_SELECTOR, "input#name"),
        "email_input": (By.CSS_SELECTOR, "input#email"),
        "submit_button": (By.CSS_SELECTOR, "button#submit-payment"),
    }

    def __init__(self, driver: WebDriver, parent: WebElement) -> None:
        """Initialize PaymentDetailsModal."""
        super().__init__(driver, parent)

    def is_open_modal(self) -> bool:
        """Return True if payment modal is displayed."""
        return self.parent.is_displayed()

    def fill_credentials(self, user: User) -> "PaymentDetailsModal":
        """Fill name and email input fields."""
        name_input = self.find_element(self.locators["name_input"])
        email_input = self.find_element(self.locators["email_input"])
        self.fill_input(name_input, user.name)
        self.fill_input(email_input, user.email)
        return self

    def click_submit_successfully(self) -> "MenuPage":
        """Click submit and return MenuPage."""
        self.find_element(self.locators["submit_button"]).click()
        return MenuPage(self.driver)

    def click_submit_unsuccessfully(self) -> "PaymentDetailsModal":
        """Click submit and return self."""
        self.find_element(self.locators["submit_button"]).click()
        return self
