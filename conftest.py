"""Pytest configuration file with Allure reporting and screenshot on failure."""

import allure
import pytest
from allure_commons.types import AttachmentType

from fixtures import *


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attaches a screenshot to the Allure report on test failure.

    This is a pytest hook that wraps the test reporting process. It specifically
    captures a screenshot if a test fails during the 'call' phase (when the test
    function is executed). The screenshot is then attached to the test's Allure
    report for debugging purposes.

    The function attempts to locate the WebDriver instance by first checking for
    a 'driver' fixture in the test's function arguments and then by checking
    if the test class instance has a 'driver' attribute.

    Args:
        item: The test item object.
        call: The execution call object. This contains information about the
              phase of the test run (e.g., 'setup', 'call', 'teardown').

    Yields:
        The outcome of the wrapped hook.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Assuming 'driver' is available in the test item's fixture scope
        # Replace 'driver' with your WebDriver instance (e.g., self.driver in a class)
        # Or pass it as an argument if using a different setup
        try:
            if "driver" in item.funcargs:
                driver = item.funcargs["driver"]
            elif hasattr(item.instance, "driver"):
                driver = item.instance.driver
            else:
                return  # No driver found

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"screenshot_on_failure_{item.name}",
                attachment_type=AttachmentType.PNG,
            )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
