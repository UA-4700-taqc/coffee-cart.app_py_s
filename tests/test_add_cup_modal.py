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
