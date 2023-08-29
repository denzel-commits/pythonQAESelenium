import pytest

from src.page_objects.admin_page import AdminPage
from src.page_objects.manage_products_page import ManageProductsPage
from src.page_objects.add_product_page import AddProductPage
from src.page_objects.elements.alert_success import AlertSuccessElement
from test_data.products import test_products


class TestAdminPage:
    def test_admin_login_elements(self, browser):
        admin_page = AdminPage(browser)

        admin_page.get_element(AdminPage.USERNAME_INPUT)
        admin_page.get_element(AdminPage.PASSWORD_INPUT)
        admin_page.get_element(AdminPage.LOGIN_BUTTON)
        admin_page.get_element(AdminPage.FORGOTTEN_PASSWORD_LINK)
        admin_page.get_element(AdminPage.HOME_LINK)

    def test_login(self, browser, create_admin_user):
        AdminPage(browser) \
            .login_with(*create_admin_user) \
            .verify_is_logged_in() \
            .click_logout()

    @pytest.mark.parametrize("product", test_products)
    def test_create_product(self, product, browser, create_admin_user):
        AdminPage(browser) \
            .login_with(*create_admin_user) \
            .click_products_menu_item()

        ManageProductsPage(browser).click_add_new_product()

        AddProductPage(browser) \
            .fill_add_product_form_with(product) \
            .click_save_button()

        AlertSuccessElement(browser).verify_success_message()

    @pytest.mark.parametrize("prepare_product", test_products, indirect=True)
    def test_delete_product(self, browser, prepare_product):
        model = prepare_product
        ManageProductsPage(browser) \
            .set_filter_model(model) \
            .click_filter() \
            .click_checkbox_all() \
            .click_delete_product() \
            .confirm_deletion_alert()

        AlertSuccessElement(browser).verify_success_message()
