import allure
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
    CART_BUTTON = (By.CSS_SELECTOR, "#cart>button")
    CART_ITEMS = (By.CSS_SELECTOR, "#cart .dropdown-menu li:first-child table tr")
    CART_ITEM_NAME = (By.CSS_SELECTOR, "td:nth-of-type(2) a")

    TOP_MENU_ITEMS = (By.CSS_SELECTOR, "#menu .navbar-nav>li>a")

    TOP_RIGHT_LINKS = (By.CSS_SELECTOR, "#top-links .dropdown a[title='My Account']")
    REGISTER_MENU_ITEM = (By.XPATH, "//a[text()='Register']")

    @allure.feature("Home page")
    @allure.step("Change currency to {currency_code}")
    def set_currency(self, currency_code):
        self.click(self.get_element(self.CURRENCY_DROPDOWN))

        if currency_code == "EUR":
            self.click(self.get_element(self.EUR_CURRENCY_BUTTON))
        elif currency_code == "GBP":
            self.click(self.get_element(self.GBP_CURRENCY_BUTTON))
        elif currency_code == "USD":
            self.click(self.get_element(self.USD_CURRENCY_BUTTON))

        return self

    @allure.step("Click 'Cart' button")
    def click_cart_button(self):
        self.simple_click_element(
            self.get_element(self.CART_BUTTON)
        )
        return self

    @allure.step("Verify {product_name} product is in cart")
    def verify_product_is_in_cart(self, product_name):
        self.click_cart_button()

        cart_product_names = [cart_item.find_element(*self.CART_ITEM_NAME).text
                              for cart_item in self.get_elements(self.CART_ITEMS)]

        assert product_name in cart_product_names

    @allure.step("Verify prices changed to {currency_code} currency")
    def verify_prices_changed_to(self, currency_code, initial_prices, new_prices):
        converted_prices = [convert_currency(price, "USD", currency_code) for price in initial_prices]
        sanitized_new_prices = [sanitize_price(price, currency_code) for price in new_prices]

        self.logger.info("{}: Compare prices: {} == {}"
                         .format(self.class_name, str(converted_prices), str(sanitized_new_prices)))

        assert converted_prices == sanitized_new_prices

    @allure.step("Verify currency symbol changed to {currency_symbol}")
    def verify_currency_symbol(self, currency_symbol):
        assert self.verify_element_text(self.get_element(self.CURRENCY_CURRENT), currency_symbol)

    @allure.step("Click {target_name} menu item")
    def click_menu_item_by_name(self, target_name):
        for item in self.get_elements(self.TOP_MENU_ITEMS):
            if item.text == target_name:
                self.click(item)
                break

        return CatalogPage(self.browser)

    @allure.step("Click 'Register' menu item")
    def click_register(self):
        self.click(self.get_element(self.TOP_RIGHT_LINKS))
        self.click(self.get_element(self.REGISTER_MENU_ITEM))
