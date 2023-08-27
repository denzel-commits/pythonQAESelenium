import pytest

from src.page_objects.home_page import HomePage
from src.page_objects.elements.header_element import HeaderElement


class TestHome:

    def test_home_page_elements(self, driver, base_url):
        home_page = HomePage(driver, base_url)
        home_page.get_element(HeaderElement.SHOPPING_CART_LINK)
        home_page.get_element(HeaderElement.CART_BUTTON)

        home_page.get_element(HeaderElement.CURRENCY_DROPDOWN)

        home_page.get_element(HeaderElement.SEARCH_INPUT)
        home_page.get_element(HeaderElement.SEARCH_BUTTON)
        home_page.get_element(HeaderElement.HOME_LINK)

    def test_add_random_product_to_cart(self, driver, base_url, products_featured_element):
        HomePage(driver, base_url)

        product = products_featured_element.get_random_product()
        product_name = product.get_name()
        product.add_to_cart()

        assert HeaderElement(driver).product_is_in_cart(product_name)

    @pytest.mark.parametrize("currency_code", ["EUR", "GBP"])
    def test_change_currency(self, driver, base_url, currency_code, products_featured_element):
        HomePage(driver, base_url)

        prices = products_featured_element.get_products_prices()
        HeaderElement(driver).set_currency(currency_code)
        new_prices = products_featured_element.get_products_prices()

        assert prices != new_prices
