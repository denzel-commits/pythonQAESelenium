from configuration import CATALOG_SMARTPHONE_PATH
from src.utils import search_visible_element
from src.pages.catalog_page import CatalogPage


class TestCatalog:
    def test_catalog_page_elements(self, driver, base_url):
        driver.get(base_url + CATALOG_SMARTPHONE_PATH)

        search_visible_element(driver, CatalogPage.LEFT_MENU_ITEMS)

        search_visible_element(driver, CatalogPage.SWIPER_SLIDER)

        search_visible_element(driver, CatalogPage.SHOW_DROPDOWN)
        search_visible_element(driver, CatalogPage.SORT_DROPDOWN)
        search_visible_element(driver, CatalogPage.GRID_VIEW)
        search_visible_element(driver, CatalogPage.LIST_VIEW)
