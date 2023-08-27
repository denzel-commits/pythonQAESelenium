import pytest
from src.utils import make_screenshot
from src.page_objects.admin_login_page import AdminLoginPage


class TestAdminLogin:
    def test_admin_login_page_elements(self, driver, base_url):
        admin_page = AdminLoginPage(driver, base_url)

        admin_page.get_element(AdminLoginPage.USERNAME_INPUT)
        admin_page.get_element(AdminLoginPage.PASSWORD_INPUT)
        admin_page.get_element(AdminLoginPage.LOGIN_BUTTON)
        admin_page.get_element(AdminLoginPage.FORGOTTEN_PASSWORD_LINK)
        admin_page.get_element(AdminLoginPage.HOME_LINK)

    @pytest.mark.parametrize("login, password", [("admin_oc1", "password!23")])
    def test_login(self, login, password, driver, base_url):
        admin_page = AdminLoginPage(driver, base_url).enter_username(login) \
            .enter_password(password) \
            .press_enter()

        if admin_page.is_logged_in():
            admin_page.click_logout()
            assert True
        else:
            make_screenshot(driver, "admin_login_test")
            assert False
