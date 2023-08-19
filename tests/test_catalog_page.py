import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from configuration import CATALOG_SMARTPHONE_PATH
from src.utils import search_visible_element, search_visible_elements
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

    @pytest.mark.parametrize("currency", ["EUR", "GBP"])
    def test_change_currency(self, driver, base_url, currency):
        driver.get(base_url)

        products = search_visible_elements(driver, (By.CSS_SELECTOR, ".product-layout"))

        product_prices = []
        for product in products:
            try:
                old_price = product.find_element(By.CSS_SELECTOR, ".price .price-old").text
            except NoSuchElementException:
                old_price = ""

            product_price = product.find_element(By.CSS_SELECTOR, ".price").text
            tax_price = product.find_element(By.CSS_SELECTOR, ".price .price-tax").text

            product_prices.append(product_price.replace(tax_price, "").replace(old_price, "").strip())

        search_visible_element(driver, CatalogPage.CURRENCY_DROPDOWN).click()

        currencies = {
            "EUR": search_visible_element(driver, CatalogPage.EUR_CURRENCY_BUTTON).click,
            "GBP": search_visible_element(driver, CatalogPage.GBP_CURRENCY_BUTTON).click,
            "USD": search_visible_element(driver, CatalogPage.USD_CURRENCY_BUTTON).click,
        }
        currencies[currency]()

        products = search_visible_elements(driver, (By.CSS_SELECTOR, ".product-layout"))

        new_product_prices = []
        for product in products:
            product_price = product.find_element(By.CSS_SELECTOR, ".price").text
            tax_price = product.find_element(By.CSS_SELECTOR, ".price .price-tax").text

            try:
                old_price = product.find_element(By.CSS_SELECTOR, ".price .price-old").text
            except NoSuchElementException:
                old_price = ""

            new_product_prices.append(product_price.replace(tax_price, "").replace(old_price, "").strip())

        assert product_prices != new_product_prices

        print(product_prices, "!=", new_product_prices)
