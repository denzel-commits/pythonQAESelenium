import pytest
from src.page_objects.admin_page import AdminPage
from test_data.admin_user import admin_user


class TestAdminPage:
    def test_admin_page_elements(self, driver, base_url):
        admin_page = AdminPage(driver, base_url)

        admin_page.get_element(AdminPage.USERNAME_INPUT)
        admin_page.get_element(AdminPage.PASSWORD_INPUT)
        admin_page.get_element(AdminPage.LOGIN_BUTTON)
        admin_page.get_element(AdminPage.FORGOTTEN_PASSWORD_LINK)
        admin_page.get_element(AdminPage.HOME_LINK)

    @pytest.mark.parametrize("username, password", [admin_user.values()])
    def test_login2(self, username, password, driver, base_url):
        AdminPage(driver, base_url) \
            .enter_username(username) \
            .enter_password(password) \
            .press_enter() \
            .is_logged_in().click_logout()
