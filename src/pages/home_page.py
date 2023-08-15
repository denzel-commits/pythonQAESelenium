from selenium.webdriver.common.by import By
from src.utils import search_visible_element


class HomePage:
    SHOPPING_CART_LINK = (By.LINK_TEXT, "Shopping Cart")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart")

    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    EUR_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='EUR']")
    GBP_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='GBP']")
    USD_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='USD']")

    SEARCH_INPUT = (By.CSS_SELECTOR, "#search input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    HOME_LINK = (By.CSS_SELECTOR, "#logo")

    def __init__(self, driver):
        self.driver = driver

    def change_currency_to(self, currency):
        search_visible_element(self.driver, self.CURRENCY_DROPDOWN).click()

        currencies = {
            "EUR": search_visible_element(self.driver, self.EUR_CURRENCY_BUTTON).click,
            "GBP": search_visible_element(self.driver, self.GBP_CURRENCY_BUTTON).click,
            "USD": search_visible_element(self.driver, self.USD_CURRENCY_BUTTON).click,
        }
        currencies[currency]()
