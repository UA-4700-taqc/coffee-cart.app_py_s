"""Module for GithabPage UI component."""
from selenium.webdriver.common.by import By

from pages.base import BasePage
from pages.menu_page import MenuPage


class GitHubPage(BasePage):
    """GitHubPage class."""

    locators = {
        "repo_link": (By.LINK_TEXT, "jecfish/coffee-cart"),
        "extra_action_link": (By.LINK_TEXT, "usual add to cart flows."),
        "simulate_ads_link": (By.LINK_TEXT, "https://coffee-cart.app/?ad=1"),
        "simulate_error_link": (By.LINK_TEXT, "https://coffee-cart.app/?breakable=1"),
        "recorder_panel_link": (By.XPATH, "//li[contains(normalize-space(.), 'Recorder panel (link)')]//a"),
        "performance_insights_panel_link": (
            By.XPATH,
            "//li[contains(normalize-space(.), 'Performance insights panel (link)')]//a",
        ),
    }

    def open_repo(self) -> None:
        """Open GitHub repository."""
        self.find_element(self.locators["repo_link"]).click()

    def open_extra_action(self) -> None:
        """Open video tutorial."""
        self.find_element(self.locators["extra_action_link"]).click()

    def click_on_simulate_ads_link(self) -> "MenuPage":
        """Switch to Menu page with ad=1."""
        self.find_element(self.locators["simulate_ads_link"]).click()
        return MenuPage(self.driver)

    def click_on_simulate_errors_link(self) -> "MenuPage":
        """Switch to Menu page with ad=1."""
        self.find_element(self.locators["simulate_error_link"]).click()
        return MenuPage(self.driver)

    def click_on_recorder_panel_link(self) -> None:
        """Open documentation about add-to-cart flow."""
        self.find_element(self.locators["recorder_panel_link"]).click()

    def click_on_open_performance_insights_panel_link(self) -> None:
        """Open documentation about perfomance overview."""
        self.find_element(self.locators["performance_insights_panel_link"]).click()
