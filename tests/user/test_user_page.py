from src.page_objects.home_page import HomePage
from src.page_objects.user_page import UserPage


class TestUser:
    def test_register_page_elements(self, browser):
        HomePage(browser).click_register()

        user_page = UserPage(browser)
        user_page.get_element(UserPage.RIGHT_MENU_ITEMS)
        user_page.get_element(UserPage.FIRSTNAME_INPUT)
        user_page.get_element(UserPage.SUBSCRIBE_YES_RADIO)
        user_page.get_element(UserPage.SUBSCRIBE_NO_RADIO)
        user_page.get_element(UserPage.PRIVACY_POLICY_CHECKBOX)
        user_page.get_element(UserPage.CONTINUE_BUTTON)

    def test_register_new_user(self, browser, customer_profile):
        HomePage(browser).click_register()

        UserPage(browser) \
            .set_firstname(customer_profile["firstname"]) \
            .set_lastname(customer_profile["lastname"]) \
            .set_email(customer_profile["email"]) \
            .set_telephone(customer_profile["phone"]) \
            .set_password(customer_profile["password"]) \
            .set_password_confirm(customer_profile["password"]) \
            .subscribe() \
            .check_privacy_policy() \
            .click_continue() \
            .verify_account_created()
