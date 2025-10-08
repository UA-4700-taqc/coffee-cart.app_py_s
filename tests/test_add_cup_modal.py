from utilities.logger import Logger

logger = Logger.get_logger("test_add_cup_modal")


def test_add_cup_modal_styles(driver_menu_page):
    """Test to verify styles of Add Cup Modal component."""
    logger.info("Starting test: Verify Add Cup Modal styles")

    menu_page = driver_menu_page

    cup = menu_page.get_cup_by_name("Espresso")
    add_cup_modal = cup.open_add_cup_modal()

    assert add_cup_modal.is_open(), "Add Cup Modal should be open"
    logger.info("Add Cup Modal is open")

    dialog_styles = add_cup_modal.get_dialog_styles()
    logger.info(f"Retrieved dialog styles: {dialog_styles}")

    # Verify position
    assert dialog_styles.get("position") == "fixed", "Dialog should have fixed position"
    logger.info(f"Position verified: {dialog_styles.get('position')}")

    # Verify background color
    background_color = dialog_styles.get("backgroundColor")
    assert background_color, "Dialog should have background color"
    logger.info(f"Background color verified: {background_color}")

    # Verify border style
    assert dialog_styles.get("borderStyle") == "solid", "Dialog should have solid border"
    logger.info(f"Border style verified: {dialog_styles.get('borderStyle')}")

    # Verify border color
    border_color = dialog_styles.get("borderColor")
    assert border_color, "Dialog should have border color"
    logger.info(f"Border color verified: {border_color}")

    # Verify border width (Chrome returns combined value)
    border_width = dialog_styles.get("borderWidth")
    assert border_width in ["1.5px", "3px"], f"Dialog border width should be 1.5px or 3px, got {border_width}"
    logger.info(f"Border width verified: {border_width}")

    # Verify display
    assert dialog_styles.get("display") == "block", "Dialog should be displayed as block"
    logger.info(f"Display verified: {dialog_styles.get('display')}")

    # Verify padding
    assert dialog_styles.get("padding") == "18px", "Dialog should have 18px padding"
    logger.info(f"Padding verified: {dialog_styles.get('padding')}")

    logger.info("Add Cup Modal styles test completed successfully")


def test_add_cup_modal_button_styles(driver_menu_page):
    """Test to verify button styles in Add Cup Modal component."""
    logger.info("Starting test: Verify Add Cup Modal button styles")

    menu_page = driver_menu_page

    cup = menu_page.get_cup_by_name("Espresso")
    add_cup_modal = cup.open_add_cup_modal()

    assert add_cup_modal.is_open(), "Add Cup Modal should be open"
    logger.info("Add Cup Modal is open")

    yes_button_styles = add_cup_modal.get_yes_button_styles()
    logger.info(f"Retrieved Yes button styles: {yes_button_styles}")

    assert yes_button_styles.get("cursor") == "default", "Yes button should have default cursor"
    logger.info(f"Yes button cursor verified: {yes_button_styles.get('cursor')}")

    yes_bg_color = yes_button_styles.get("backgroundColor")
    assert yes_bg_color, "Yes button should have background color"
    logger.info(f"Yes button background color verified: {yes_bg_color}")

    yes_color = yes_button_styles.get("color")
    assert yes_color, "Yes button should have text color"
    logger.info(f"Yes button text color verified: {yes_color}")

    no_button_styles = add_cup_modal.get_no_button_styles()
    logger.info(f"Retrieved No button styles: {no_button_styles}")

    assert no_button_styles.get("cursor") == "default", "No button should have default cursor"
    logger.info(f"No button cursor verified: {no_button_styles.get('cursor')}")

    no_bg_color = no_button_styles.get("backgroundColor")
    assert no_bg_color, "No button should have background color"
    logger.info(f"No button background color verified: {no_bg_color}")

    no_color = no_button_styles.get("color")
    assert no_color, "No button should have text color"
    logger.info(f"No button text color verified: {no_color}")

    logger.info("Add Cup Modal button styles test completed successfully")


def test_add_cup_modal_confirm_and_cancel(driver_menu_page):
    """Test to verify product name display and modal actions."""
    logger.info("Starting test: Verify Add Cup Modal product name and actions")

    menu_page = driver_menu_page

    cup = menu_page.get_cup_by_name("Espresso")
    add_cup_modal = cup.open_add_cup_modal()

    assert add_cup_modal.is_open(), "Add Cup Modal should be open"
    logger.info("Add Cup Modal is open")

    product_name = add_cup_modal.get_product_name()
    assert product_name == "Espresso", f"Product name should be 'Espresso', got '{product_name}'"
    logger.info(f"Product name verified: {product_name}")

    add_cup_modal.confirm()
    logger.info("Confirmed modal")

    cup = menu_page.get_cup_by_name("Espresso")
    add_cup_modal = cup.open_add_cup_modal()

    assert add_cup_modal.is_open(), "Add Cup Modal should be open again"
    logger.info("Add Cup Modal reopened")

    add_cup_modal.cancel()
    logger.info("Canceled modal")

    logger.info("Add Cup Modal product name and actions test completed successfully")
