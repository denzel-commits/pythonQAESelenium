from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage
from src.page_objects.catalog_page import CatalogPage
from src.utilities import convert_currency, sanitize_price


class HomePage(BasePage):
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    CURRENCY_CURRENT = (By.CSS_SELECTOR, "#form-currency strong")
    EUR_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='EUR']")
    GBP_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='GBP']")
    USD_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='USD']")

    SEARCH_INPUT = (By.CSS_SELECTOR, "#search input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")

    HOME_LINK = (By.CSS_SELECTOR, "#logo")

    SHOPPING_CART_LINK = (By.LINK_TEXT, "Shopping Cart")
    CART_BUTTON = (By.CSS_SELECTOR, "#cart-total")
    CART_ITEMS = (By.CSS_SELECTOR, "#cart .dropdown-menu li:first-child table tr")
    CART_ITEM_NAME = (By.CSS_SELECTOR, "td:nth-of-type(2) a")

    TOP_MENU_ITEMS = (By.CSS_SELECTOR, "#menu .navbar-nav>li>a")

    TOP_RIGHT_LINKS = (By.CSS_SELECTOR, "#top-links .dropdown a[title='My Account']")
    REGISTER_MENU_ITEM = (By.XPATH, "//a[text()='Register']")

    def set_currency(self, currency_code):
        self.click(self.get_element(self.CURRENCY_DROPDOWN))

        if currency_code == "EUR":
            self.click(self.get_element(self.EUR_CURRENCY_BUTTON))
        elif currency_code == "GBP":
            self.click(self.get_element(self.GBP_CURRENCY_BUTTON))
        elif currency_code == "USD":
            self.click(self.get_element(self.USD_CURRENCY_BUTTON))

        return self

    def click_cart_button(self):
        self._simple_click_element(
            self.get_element(self.CART_BUTTON)
        )
        return self

    def verify_product_is_in_cart(self, product_name):
        self.click_cart_button()

        cart_product_names = [cart_item.find_element(*self.CART_ITEM_NAME).text
                              for cart_item in self.get_elements(self.CART_ITEMS)
                              ]

        assert product_name in cart_product_names

    @staticmethod
    def verify_prices_changed_to(currency_code, initial_prices, new_prices):
        converted_prices = [convert_currency(price, "USD", currency_code) for price in initial_prices]
        sanitized_new_prices = [sanitize_price(price, currency_code) for price in new_prices]
        print(converted_prices, "==", sanitized_new_prices)
        assert converted_prices == sanitized_new_prices

    def verify_currency_symbol(self, currency_symbol):
        assert currency_symbol == self.get_element(self.CURRENCY_CURRENT).text

    def click_menu_item_by_name(self, target_name):
        for item in self.get_elements(self.TOP_MENU_ITEMS):
            if item.text == target_name:
                self.click(item)
                break

        return CatalogPage(self.browser)

    def click_register(self):
        self.click(self.get_element(self.TOP_RIGHT_LINKS))
        self.click(self.get_element(self.REGISTER_MENU_ITEM))
