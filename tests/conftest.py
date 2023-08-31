import random
import mysql.connector

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from configuration import YANDEX_WEBDRIVER_PATH, \
    MYSQL_DB_NAME, MYSQL_DB_PASSWORD, MYSQL_DB_HOST, MYSQL_DB_USER, MYSQL_DB_PORT
from src.page_objects.elements.products_element import ProductsElement


@pytest.fixture()
def db_connection(request):
    connection = mysql.connector.connect(
        user=MYSQL_DB_USER,
        password=MYSQL_DB_PASSWORD,
        host=MYSQL_DB_HOST,
        database=MYSQL_DB_NAME,
        port=MYSQL_DB_PORT
    )
    request.addfinalizer(connection.close)
    return connection


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return random.randint(1, 1000)


@pytest.fixture()
def products_element(browser):
    return ProductsElement(browser)


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "yandex", "edge", "Chrome", "Firefox", "Yandex", "Edge"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--base_url", help="Request URL", default="http://192.168.1.127:8081"
    )
    parser.addoption(
        "--tolerance", type=int, default=3
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def browser(request, base_url):
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    tolerance = request.config.getoption("--tolerance")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("start-maximized")

        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("-headless")

        driver = webdriver.Firefox(service=FirefoxService(), options=options)
        driver.maximize_window()

    elif browser_name == "yandex":
        options = ChromeOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(service=ChromeService(executable_path=YANDEX_WEBDRIVER_PATH), options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Chrome(service=EdgeService(), options=options)
    else:
        raise NotImplemented()

    request.addfinalizer(driver.quit)

    def go_to(path=""):
        driver.get(base_url + path)

    driver.open = go_to
    driver.open()
    driver.t = tolerance

    return driver
