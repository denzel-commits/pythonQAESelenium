import pytest

from src.page_objects.admin_page import AdminPage
from src.page_objects.manage_products_page import ManageProductsPage
from src.page_objects.add_product_page import AddProductPage
from test_data.products import test_products


class TestAdminPage:
    def test_admin_login_elements(self, browser):
        admin_page = AdminPage(browser)

        admin_page.get_element(AdminPage.USERNAME_INPUT)
        admin_page.get_element(AdminPage.PASSWORD_INPUT)
        admin_page.get_element(AdminPage.LOGIN_BUTTON)
        admin_page.get_element(AdminPage.FORGOTTEN_PASSWORD_LINK)
        admin_page.get_element(AdminPage.HOME_LINK)

    def test_admin_login(self, browser, create_admin_user):
        AdminPage(browser) \
            .login_with(*create_admin_user) \
            .verify_is_logged_in() \
            .click_logout()

    @pytest.mark.parametrize("test_product", test_products, indirect=True)
    def test_add_product_from_dashboard(self, browser, create_admin_user, test_product):
        AdminPage(browser) \
            .login_with(*create_admin_user) \
            .click_products_menu_item()

        products_page = ManageProductsPage(browser) \
            .click_add_new_product()

        AddProductPage(browser) \
            .fill_add_product_form_with(test_product) \
            .click_save_button()

        products_page.has_product_in_list(test_product["model"])

    @pytest.mark.parametrize("prepare_product", test_products, indirect=True)
    def test_delete_product_from_dashboard(self, browser, prepare_product):
        model = prepare_product

        products_page = ManageProductsPage(browser) \
            .click_product_checkbox(model) \
            .click_delete_product() \
            .accept_delete_alert()

        products_page.has_no_product_in_list(model)
