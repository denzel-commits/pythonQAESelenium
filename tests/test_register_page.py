from configuration import REGISTER_PATH
from src.pages.register_page import RegisterPage
from src.utils import search_visible_element


class TestRegister:
    def test_register_page_elements(self, driver, base_url):
        driver.get(base_url + REGISTER_PATH)

        search_visible_element(driver, RegisterPage.RIGHT_MENU_ITEMS)
        search_visible_element(driver, RegisterPage.FIRSTNAME_INPUT)
        search_visible_element(driver, RegisterPage.SUBSCRIBE_RADIO)
        search_visible_element(driver, RegisterPage.PRIVACY_POLICY_CHECKBOX)
        search_visible_element(driver, RegisterPage.CONTINUE_BUTTON)
