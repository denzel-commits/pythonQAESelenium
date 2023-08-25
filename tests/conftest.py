import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

from configuration import YANDEX_WEBDRIVER_PATH, ADMIN_PATH
from src.page_objects.admin_login_page import AdminLoginPage
from src.utils import search_visible_element, send_keys_by_one


@pytest.fixture()
def admin_login(request, driver, base_url):
    driver.get(base_url + ADMIN_PATH)

    username, password = request.param

    search_visible_element(driver, AdminLoginPage.USERNAME_INPUT).click()
    search_visible_element(driver, AdminLoginPage.USERNAME_INPUT).clear()
    send_keys_by_one(search_visible_element(driver, AdminLoginPage.USERNAME_INPUT),
                     username
                     )

    search_visible_element(driver, AdminLoginPage.PASSWORD_INPUT).click()
    search_visible_element(driver, AdminLoginPage.PASSWORD_INPUT).clear()
    send_keys_by_one(search_visible_element(driver, AdminLoginPage.PASSWORD_INPUT),
                     password
                     )

    search_visible_element(driver, AdminLoginPage.PASSWORD_INPUT).send_keys(Keys.RETURN)


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
        "--base_url", help="Request URL", default="http://192.168.1.128:8081"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

        browser = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("-headless")

        browser = webdriver.Chrome(service=FirefoxService(), options=options)
        browser.maximize_window()

    elif browser_name == "yandex":
        options = ChromeOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

        browser = webdriver.Chrome(service=ChromeService(executable_path=YANDEX_WEBDRIVER_PATH), options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("start-maximized")

        if headless:
            options.add_argument("--headless")

        browser = webdriver.Chrome(service=EdgeService(), options=options)
    else:
        raise NotImplemented()

    request.addfinalizer(browser.quit)

    return browser
