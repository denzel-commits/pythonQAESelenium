import time
import pytest

from src.page_objects.catalog_page import CatalogPage
from src.page_objects.home_page import HomePage


class TestCatalog:
    def test_catalog_page_elements(self, driver, base_url):
        catalog = HomePage(driver, base_url).click_menu_item_by_name("Phones & PDAs")

        catalog.get_element(CatalogPage.LEFT_MENU_ITEMS)
        catalog.get_element(CatalogPage.SWIPER_SLIDER)

        catalog.get_element(CatalogPage.SHOW_DROPDOWN)
        catalog.get_element(CatalogPage.SORT_DROPDOWN)
        catalog.get_element(CatalogPage.GRID_VIEW)
        catalog.get_element(CatalogPage.LIST_VIEW)

    @pytest.mark.parametrize("currency_code", ["EUR", "GBP"])
    def test_change_currency(self, driver, base_url, currency_code, products_catalog_element):
        home_page = HomePage(driver, base_url)
        home_page.click_menu_item_by_name("Phones & PDAs")

        prices = products_catalog_element.get_products_prices()
        home_page.set_currency(currency_code)
        new_prices = products_catalog_element.get_products_prices()

        assert prices != new_prices
