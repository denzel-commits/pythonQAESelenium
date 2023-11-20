import os.path

YANDEX_WEBDRIVER_PATH = os.path.expanduser("~/Downloads/yandexdriver-23.7.0.2469-win64/yandexdriver.exe")

PROJECT_ROOT = os.path.dirname(__file__)
SCREENSHOTS_PATH = os.path.join(PROJECT_ROOT, "screenshots")

MYSQL_DB_NAME = "bitnami_opencart"
MYSQL_DB_USER = "bn_opencart"
MYSQL_DB_PASSWORD = ""
MYSQL_DB_HOST = "192.168.1.127"
MYSQL_DB_PORT = "3306"

CURRENCY_SYMBOLS = {"EUR": "€", "GBP": "£", "USD": "$"}

ENVIRONMENT = "DEVELOPMENT"
LOGS_PATH = os.path.join(PROJECT_ROOT, "logs", "selenium")
BROWSER_LOGS_PATH = os.path.join(PROJECT_ROOT, "logs", "browser")

SAUCE_URL = "https://ondemand.eu-central-1.saucelabs.com:443"
SAUCE_ACCESS_KEY = "a983bd96-5ea4-40a7-89da-3bb213f958cf"
SAUCE_USERNAME = "oauth-dguchinsky-0012a"
SAUCE_TESTNAME = "OTUS_OPENCART"
