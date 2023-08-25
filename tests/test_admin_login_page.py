import time

import pytest
from selenium.webdriver.common.by import By
from configuration import ADMIN_PATH
from src.utils import search_visible_element, make_screenshot
from src.page_objects.admin_login_page import AdminLoginPage


class TestAdminLogin:
    def test_admin_login_page_elements(self, driver, base_url):
        driver.get(base_url + ADMIN_PATH)

        search_visible_element(driver, AdminLoginPage.USERNAME_INPUT)
        search_visible_element(driver, AdminLoginPage.PASSWORD_INPUT)
        search_visible_element(driver, AdminLoginPage.LOGIN_BUTTON)
        search_visible_element(driver, AdminLoginPage.FORGOTTEN_PASSWORD_LINK)
        search_visible_element(driver, AdminLoginPage.HOME_LINK)

    @pytest.mark.parametrize("admin_login", [("admin_oc1", "password!23")], indirect=True)
    def test_login(self, driver, admin_login):

        admin_page_header = search_visible_element(driver, (By.CSS_SELECTOR, "H1")).text

        if admin_page_header == "Dashboard":
            search_visible_element(driver, (By.LINK_TEXT, "Logout")).click()
            assert True
        else:
            make_screenshot(driver, "admin_login_test")
            assert False
