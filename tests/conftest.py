import logging.handlers
import os
import random

import allure
import mysql.connector

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from configuration import YANDEX_WEBDRIVER_PATH, \
    MYSQL_DB_NAME, MYSQL_DB_PASSWORD, MYSQL_DB_HOST, MYSQL_DB_USER, MYSQL_DB_PORT, LOGS_PATH
from src.page_objects.elements.products_element import ProductsElement
from src.utilities import create_directory_if_not_exists


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
    parser.addoption("--run_locally", action="store_true")
    parser.addoption("--browser", default="chrome",
                     choices=["chrome", "chrome-mobile", "firefox", "yandex", "edge", "safari", "Chrome", "Firefox",
                              "Yandex", "Edge"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", help="Request URL", default="http://192.168.1.127:8081")
    parser.addoption("--tolerance", type=int, default=3)

    parser.addoption("--executor", default="http://192.168.1.127:4444")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")
    parser.addoption("--bv")

    parser.addoption("--logging_level", default="WARNING")


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def configure_browser_options(request):
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    options = None

    if browser_name == "chrome" or browser_name == "chrome-mobile":
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

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")

        options.log.level = "trace"

    elif browser_name == "yandex":
        options = ChromeOptions()
        options.add_argument("start-maximized")
        if headless:
            options.add_argument("--headless")

    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

    elif browser_name == "safari":
        options = SafariOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

    return options


@pytest.fixture()
def browser(request, base_url, logger, configure_browser_options):
    run_locally = request.config.getoption("--run_locally")
    browser_name = request.config.getoption("--browser").lower()
    tolerance = request.config.getoption("--tolerance")

    executor = request.config.getoption("--executor")
    mobile = request.config.getoption("--mobile")

    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")

    logger.info(f"Test {request.node.name} started")

    if run_locally:
        if browser_name in ["chrome", "edge", "chrome-mobile"]:
            driver = webdriver.Chrome(options=configure_browser_options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=configure_browser_options)
        elif browser_name == "safari":
            driver = webdriver.Safari(options=configure_browser_options)
        elif browser_name == "yandex":
            driver = webdriver.Chrome(service=ChromeService(executable_path=YANDEX_WEBDRIVER_PATH),
                                      options=configure_browser_options)
        else:
            raise NotImplementedError
    else:
        executor_url = f"{executor}"  # /wd/hub
        options = configure_browser_options
        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "enableVNC": vnc,
            "enableLog": logs,
            "enableVideo": video,
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    if not mobile:
        driver.maximize_window()

    location = "locally" if run_locally else "remotely"
    logger.info(f"Browser {browser_name} started {location}")

    @allure.step("Navigate to base_url {path}")
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
        if request.node.rep_call.failed:
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.node.name,
                          attachment_type=allure.attachment_type.PNG)

        driver.close()
        driver.quit()
        logger.info("Test {} is finished".format(request.node.name))

    request.addfinalizer(finalizer)

    return driver


@pytest.fixture()
def logger(request):
    logging_level = request.config.getoption("--logging_level").upper()

    logger = logging.getLogger(request.node.name)

    formatter = logging.Formatter("%(asctime)s | %(name)s |  %(levelname)s: %(message)s")
    logger.setLevel(logging_level)

    create_directory_if_not_exists(LOGS_PATH)

    file_handler = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(LOGS_PATH, request.node.name + ".log"),
                                                             when='midnight', backupCount=30)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
