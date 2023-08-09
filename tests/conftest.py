import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from configuration import YANDEX_WEBDRIVER_PATH


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", choices=["chrome", "firefox", "safari", "yandex", "edge"]
    )
    parser.addoption(
        "--headless", action="store_true"
    )
    parser.addoption(
        "--base_url", required=True, help="Request URL"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
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
    else:
        raise NotImplemented()

    yield browser

    browser.quit()
