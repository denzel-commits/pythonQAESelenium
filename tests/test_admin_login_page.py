from configuration import ADMIN_PATH
from src.utils import search_visible_element
from src.pages.admin_login_page import AdminLoginPage


class TestHome:
    def test_admin_login_page_elements(self, driver, base_url):
        driver.get(base_url + ADMIN_PATH)
        admin_login_page = AdminLoginPage(driver)

        search_visible_element(driver, admin_login_page.USERNAME_INPUT)
        search_visible_element(driver, admin_login_page.PASSWORD_INPUT)
        search_visible_element(driver, admin_login_page.LOGIN_BUTTON)
        search_visible_element(driver, admin_login_page.FORGOTTEN_PASSWORD_LINK)
        search_visible_element(driver, admin_login_page.HOME_LINK)
