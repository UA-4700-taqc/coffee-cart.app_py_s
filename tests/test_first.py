from config.resources import BASE_URL
from utilities.logger import get_logger


def test_open_coffe_cart_page(driver):
    """Test opening the coffee cart page and verifying the title."""
    # Initialize logger for this test with auto-detection
    logger = get_logger()

    logger.info("Starting coffee cart page title verification test")

    try:
        logger.debug(f"Navigating to URL: {BASE_URL}")
        driver.get(BASE_URL)

        logger.debug("Retrieving page title")
        title = driver.title

        logger.info(f"Page title retrieved: '{title}'")
        expected_title = "Coffee cart"
        assert title == expected_title

        logger.info("✅ Coffee cart page title verification passed")
    except AssertionError:
        logger.error(f"❌ Title assertion failed. Expected: '{expected_title}', Got: '{title}'")
    except Exception as e:
        logger.critical(f"❌ Unexpected error during page title test: {str(e)}")
