"""Module for HeaderComponent UI component."""
from selenium.webdriver.common.by import By


class HeaderComponent:
    """Class to represent the header UI component and its logic."""

    def __init__(self, driver):
        """Initializes the HeaderComponent with the web driver."""
        self.driver = driver


        self.menu_link = (By.CSS_SELECTOR, 'a[aria-label="Menu page"]')
        self.cart_link = (By.CSS_SELECTOR, 'a[aria-label="Cart page"]')
        self.github_link = (By.CSS_SELECTOR, 'a[aria-label="GitHub page"]')

    def click_menu(self):
        """Clicks the 'Menu' link."""
        self.driver.find_element(*self.menu_link).click()

    def click_cart(self):
        """Clicks the 'Cart' link."""
        self.driver.find_element(*self.cart_link).click()

    def click_github(self):
        """Clicks the 'GitHub' link."""
        self.driver.find_element(*self.github_link).click()


