"""Module for HeaderComponent UI component."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base import BaseComponent
from pages.menu_page import MenuPage
from pages.cart_page import CartPage
from pages.githab_page import GitHubPage


class HeaderComponent(BaseComponent):
    """Class to represent the header UI component and its logic."""
    locators = {
    "menu_link" : (By.CSS_SELECTOR, 'a[aria-label="Menu page"]'),
    "cart_link" : (By.CSS_SELECTOR, 'a[aria-label="Cart page"]'),
    "github_link" : (By.CSS_SELECTOR, 'a[aria-label="GitHub page"]'),

    }

    def __init__(self, driver : WebDriver, parent: WebElement) -> None:
        """Initializes the HeaderComponent with the web driver."""
        super().__init__(driver , parent)



    def click_menu(self):
        """Clicks the 'Menu' link."""
        self.find_element(*self.locators["menu_link"]).click()
        return  MenuPage(self.driver)

    def click_cart(self):
        """Clicks the 'Cart' link."""
        self.find_element(*self.locators["cart_link"]).click()
        return CartPage(self.driver)

    def click_github(self):
        """Clicks the 'GitHub' link."""
        self.find_element(*self.locators["github_link"]).click()
        return GitHubPage(self.driver)




