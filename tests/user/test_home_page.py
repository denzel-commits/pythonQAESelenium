import time

import allure
import pytest

from src.page_objects.home_page import HomePage


class TestHome:

    @allure.feature("Home page")
    @allure.title("Verify elements presence")
    def test_home_page_elements(self, browser):
        home_page = HomePage(browser)
        home_page.get_element(HomePage.SHOPPING_CART_LINK)
        home_page.get_element(HomePage.CART_BUTTON)

        home_page.get_element(HomePage.CURRENCY_DROPDOWN)

        home_page.get_element(HomePage.SEARCH_INPUT)
        home_page.get_element(HomePage.SEARCH_BUTTON)
        home_page.get_element(HomePage.HOME_LINK)

    @allure.feature("Add to cart")
    @allure.title("Add random product to cart")
    def test_add_random_product_to_cart(self, browser, products_element):
        home_page = HomePage(browser)

        product = products_element.get_random_product()
        product_name = product.get_name()
        product.add_to_cart()

        home_page.verify_product_is_in_cart(product_name)

    @allure.feature("Currency change")
    @allure.title("Verify changed currency prices")
    @pytest.mark.parametrize("currency_code", ["EUR", "GBP"])
    def test_change_currency_prices(self, browser, currency_code, products_element):
        home_page = HomePage(browser)

        prices = products_element.get_products_prices()
        home_page.set_currency(currency_code)
        new_prices = products_element.get_products_prices()

        home_page.verify_prices_changed_to(currency_code, prices, new_prices)

    @allure.feature("Currency change")
    @allure.title("Change currency")
    @pytest.mark.parametrize("currency_code, expected_currency_symbol", [("EUR", "€"), ("GBP", "£")])
    def test_change_currency(self, browser, currency_code, expected_currency_symbol):
        HomePage(browser) \
            .set_currency(currency_code) \
            .verify_currency_symbol(expected_currency_symbol)
