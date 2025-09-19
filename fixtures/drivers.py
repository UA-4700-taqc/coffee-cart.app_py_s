"""Fixture for WebDriver instance."""
import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.resources import BASE_URL, IMPLICIT_WAIT

__all__ = ["driver"]


@pytest.fixture()
def driver():
    """Fixture to initialize and quit the WebDriver instance."""
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.maximize_window()
    yield driver
    driver.quit()
