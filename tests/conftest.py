import logging.handlers
import os
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
    MYSQL_DB_NAME, MYSQL_DB_PASSWORD, MYSQL_DB_HOST, MYSQL_DB_USER, MYSQL_DB_PORT, ENVIRONMENT, LOGS_PATH
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
    parser.addoption("--browser", default="chrome",
                     choices=["chrome", "firefox", "yandex", "edge", "Chrome", "Firefox", "Yandex", "Edge"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", help="Request URL", default="http://192.168.1.127:8081")
    parser.addoption("--tolerance", type=int, default=3)

    if ENVIRONMENT == "DEVELOPMENT":
        parser.addoption("--log_level_threshold", default="INFO")
    else:
        parser.addoption("--log_level_threshold", default="ERROR")


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def browser(request, base_url, logger):
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")
    tolerance = request.config.getoption("--tolerance")

    logger.info("Test {} started".format(request.node.name))
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if headless:
            options.add_argument("--headless")

        options.set_capability('goog:loggingPrefs', {
            'browser': 'ALL',
            'performance': 'ALL',
            'driver': 'ALL'
        })

        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")

        options.log.level = "trace"

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

    logger.info("Browser {} started".format(browser_name))

    def navigate_to(path=""):
        logger.info("{}: Navigate to url {}".format(request.node.name, base_url + path))
        driver.get(base_url + path)

    driver.open = navigate_to
    driver.open()
    driver.tolerance = tolerance

    driver.log_level = logging.getLevelName(logger.level)
    driver.logger = logger
    driver.test_name = request.node.name

    def finalizer():
        driver.quit()
        logger.info("Test {} is finished".format(request.node.name))

    request.addfinalizer(finalizer)

    return driver


@pytest.fixture()
def logger(request):
    log_level_threshold = request.config.getoption("--log_level_threshold").upper()

    logger = logging.getLogger(request.node.name)

    formatter = logging.Formatter("%(asctime)s | %(name)s |  %(levelname)s: %(message)s")
    logger.setLevel(log_level_threshold)

    file_handler = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(LOGS_PATH, request.node.name+".log"),
                                                             when='midnight', backupCount=30)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
