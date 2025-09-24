"""Module for AddCupModal UI component."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddCupModal:
    """Empty AddCupModal class for modal functionality."""

    ROOT = (By.XPATH, "//dialog[@data-cy='add-to-cart-modal']")
    MESSAGE = (By.XPATH, "//dialog[@data-cy='add-to-cart-modal']/p")
    PRODUCT_NAME = (By.XPATH, "//dialog[@data-cy='add-to-cart-modal']/p/strong")
    YES_BUTTON = (
        By.XPATH,
        "//dialog[@data-cy='add-to-cart-modal']//button[normalize-space()='Yes']",
    )
    NO_BUTTON = (
        By.XPATH,
        "//dialog[@data-cy='add-to-cart-modal']//button[normalize-space()='No']",
    )

    def __init__(self, driver: WebDriver):
        """Initialize the AddCupModal component."""
        self.driver = driver

    def is_open(self) -> bool:
        """Return True if the dialog is displayed and has the 'open' attribute."""
        try:
            el = self.driver.find_element(*self.ROOT)
            return el.is_displayed() and el.get_attribute("open") is not None
        except Exception:
            return False

    def get_message_text(self) -> str:
        """Full message text inside the dialog."""
        return self.driver.find_element(*self.MESSAGE).text

    def get_product_name(self) -> str:
        """Product name shown in the dialog."""
        return self.driver.find_element(*self.PRODUCT_NAME).text

    def confirm(self) -> None:
        """Click 'Yes' to add to cart."""
        self.driver.find_element(*self.YES_BUTTON).click()

    def cancel(self) -> None:
        """Click 'No' to dismiss."""
        self.driver.find_element(*self.NO_BUTTON).click()
