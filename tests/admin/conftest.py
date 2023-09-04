import pytest
import socket
import hashlib

from src.page_objects.add_product_page import AddProductPage
from src.page_objects.admin_page import AdminPage
from src.page_objects.elements.alert_success import AlertSuccessElement
from src.page_objects.manage_products_page import ManageProductsPage


@pytest.fixture()
def prepare_product(browser, request, create_admin_user):
    product = request.param

    AdminPage(browser) \
        .login_with(*create_admin_user) \
        .click_products_menu_item()

    ManageProductsPage(browser).click_add_new_product()

    AddProductPage(browser) \
        .fill_add_product_form_with(product) \
        .click_save_button()

    yield product["model"]

    products_page = ManageProductsPage(browser) \
        .set_filter_model(product["model"]) \
        .click_filter_button()

    if products_page.has_filter_results():
        products_page \
            .click_checkbox_all() \
            .click_delete_product() \
            .accept_delete_alert()

        AlertSuccessElement(browser).verify_success_message()


@pytest.fixture()
def test_product(browser, request):
    product = request.param
    yield product

    ManageProductsPage(browser) \
        .set_filter_model(product["model"]) \
        .click_filter_button() \
        .click_checkbox_all() \
        .click_delete_product() \
        .accept_delete_alert()

    AlertSuccessElement(browser).verify_success_message()


@pytest.fixture()
def create_admin_user(db_connection, faker, request):
    def teardown():
        query = "DELETE FROM oc_user WHERE username=%s"
        db_connection.cursor().execute(query, (username,))
        db_connection.commit()
    request.addfinalizer(teardown)

    query = "INSERT INTO oc_user " \
            "(user_group_id, username, password, salt, firstname, lastname, email, image, code, ip, status," \
            " date_added) " \
            "VALUES (1, %s, %s, %s, %s, %s, %s, '', '', %s, 1, NOW());"

    username = faker.profile(fields=["username"])["username"]  # faker.safe_email().split("@")[0]
    test_password = "admin!32"
    salt = "VGNUpQvgV"
    ip = socket.gethostbyname(socket.gethostname())

    db_connection.cursor().execute(query, (
        username,
        hashlib.md5(test_password.encode()).hexdigest(),
        salt,
        faker.first_name(),
        faker.last_name(),
        faker.safe_email(),
        ip
    ))

    db_connection.commit()

    return username, test_password
