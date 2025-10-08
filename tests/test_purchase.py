from test_data.users import invalid_user_incorrect_email, valid_user


def test_successful_purchase(driver_menu_page):
    """Test purchase with valid_user user's credentials."""
    menu_page = (
        driver_menu_page.click_on_cup_by_name("Cafe Breve")
        .click_on_cup_by_name("Espresso")
        .click_pay_button()
        .fill_credentials(valid_user)
        .click_submit_successfully()
    )
    assert menu_page.get_snackbar_success_we()


def test_purchase_incorrect_credentials(driver_menu_page):
    """Test purchase with invalid_user_incorrect_email user's credentials."""
    payment_modal_page = (
        driver_menu_page.click_on_cup_by_name("Cafe Breve")
        .click_on_cup_by_name("Espresso")
        .click_pay_button()
        .fill_credentials(invalid_user_incorrect_email)
        .click_submit_unsuccessfully()
    )
    assert payment_modal_page.is_open_modal()
