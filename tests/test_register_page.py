from src.page_objects.register_page import RegisterPage


class TestRegister:
    def test_register_page_elements(self, driver, base_url):
        register_page = RegisterPage(driver, base_url)

        register_page.get_element(RegisterPage.RIGHT_MENU_ITEMS)
        register_page.get_element(RegisterPage.FIRSTNAME_INPUT)
        register_page.get_element(RegisterPage.SUBSCRIBE_YES_RADIO)
        register_page.get_element(RegisterPage.SUBSCRIBE_NO_RADIO)
        register_page.get_element(RegisterPage.PRIVACY_POLICY_CHECKBOX)
        register_page.get_element(RegisterPage.CONTINUE_BUTTON)
