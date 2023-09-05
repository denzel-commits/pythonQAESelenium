import os.path

YANDEX_WEBDRIVER_PATH = os.path.expanduser("~/Downloads/yandexdriver-23.7.0.2469-win64/yandexdriver.exe")

PROJECT_ROOT = os.path.dirname(__file__)
SCREENSHOTS_PATH = os.path.join(PROJECT_ROOT, "screenshots")

MYSQL_DB_NAME = "bitnami_opencart"
MYSQL_DB_USER = "bn_opencart"
MYSQL_DB_PASSWORD = ""
MYSQL_DB_HOST = "127.0.0.1"
MYSQL_DB_PORT = "3306"

CURRENCY_SYMBOLS = {"EUR": "€", "GBP": "£", "USD": "$"}

ENVIRONMENT = "DEVELOPMENT"
LOGS_PATH = os.path.join(PROJECT_ROOT, "logs", "selenium")
BROWSER_LOGS_PATH = os.path.join(PROJECT_ROOT, "logs", "browser")
