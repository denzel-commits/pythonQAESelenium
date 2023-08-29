import pytest
import socket
import hashlib

from src.page_objects.add_product_page import AddProductPage
from src.page_objects.admin_page import AdminPage
from src.page_objects.manage_products_page import ManageProductsPage


@pytest.fixture()
def prepare_product(browser, create_admin_user, request):
    product = request.param
    AdminPage(browser) \
        .login_with(*create_admin_user) \
        .click_products_menu_item()

    ManageProductsPage(browser).click_add_new_product()

    AddProductPage(browser) \
        .fill_add_product_form_req_fields_with(product) \
        .click_save_button()

    return product["model"]


@pytest.fixture()
def create_admin_user(db_connection, faker):
    query = "INSERT INTO oc_user " \
            "(user_group_id, username, password, salt, firstname, lastname, email, image, code, ip, status," \
            " date_added) " \
            "VALUES (1, %s, %s, %s, %s, %s, %s, '', '', %s, 1, NOW());"

    username = faker.safe_email().split("@")[0]
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
    )
                                   )
    db_connection.commit()

    yield username, test_password

    query = "DELETE FROM oc_user WHERE username=%s"
    db_connection.cursor().execute(query, (username,))
    db_connection.commit()
