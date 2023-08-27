import pytest

from src.page_objects.elements.header_element import HeaderElement
from src.page_objects.catalog_page import CatalogPage


class TestCatalog:
    def test_catalog_page_elements(self, driver, base_url):
        catalog = CatalogPage(driver, base_url)

        catalog.get_element(CatalogPage.LEFT_MENU_ITEMS)
        catalog.get_element(CatalogPage.SWIPER_SLIDER)

        catalog.get_element(CatalogPage.SHOW_DROPDOWN)
        catalog.get_element(CatalogPage.SORT_DROPDOWN)
        catalog.get_element(CatalogPage.GRID_VIEW)
        catalog.get_element(CatalogPage.LIST_VIEW)

    @pytest.mark.parametrize("currency_code", ["EUR", "GBP"])
    def test_change_currency(self, driver, base_url, currency_code, products_catalog_element):
        CatalogPage(driver, base_url)

        prices = products_catalog_element.get_products_prices()
        HeaderElement(driver).set_currency(currency_code)
        new_prices = products_catalog_element.get_products_prices()

        assert prices != new_prices
