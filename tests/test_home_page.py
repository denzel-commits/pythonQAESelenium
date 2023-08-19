import random

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from src.pages.home_page import HomePage
from src.utils import search_present_element, search_visible_element, search_visible_elements, make_screenshot


class TestHome:

    def test_home_page_elements(self, driver, base_url):
        driver.get(base_url)

        search_visible_element(driver, HomePage.SHOPPING_CART_LINK)
        search_visible_element(driver, HomePage.CART_BUTTON)

        search_visible_element(driver, HomePage.CURRENCY_DROPDOWN)
        search_present_element(driver, HomePage.EUR_CURRENCY_BUTTON)
        search_present_element(driver, HomePage.GBP_CURRENCY_BUTTON)
        search_present_element(driver, HomePage.USD_CURRENCY_BUTTON)

        search_visible_element(driver, HomePage.SEARCH_INPUT)
        search_visible_element(driver, HomePage.SEARCH_BUTTON)
        search_visible_element(driver, HomePage.HOME_LINK)

    def test_add_to_cart_rnd(self, driver, base_url):
        driver.get(base_url)

        # exclude last two products as they do not add to cart
        products = search_visible_elements(driver, (By.CSS_SELECTOR, ".product-layout"))[0:2]
        product_rnd = products[random.randrange(0, len(products))]
        product_rnd_title = product_rnd.find_element(By.CSS_SELECTOR, "h4 a").text
        product_rnd.find_element(By.CSS_SELECTOR, ".button-group button:first-child").click()

        search_visible_element(driver, HomePage.CART_BUTTON).click()
        cart_items = search_visible_elements(driver, (By.CSS_SELECTOR, "#cart .dropdown-menu li:first-child table tr"))

        product_rnd_is_in_cart = False
        for cart_item in cart_items:
            cart_item_title = cart_item.find_element(By.CSS_SELECTOR, "td:nth-of-type(2) a").text
            if cart_item_title == product_rnd_title:
                product_rnd_is_in_cart = True

        if product_rnd_is_in_cart:
            assert True
        else:
            make_screenshot(driver, "test_add_to_cart_rnd")
            assert False

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

        search_visible_element(driver, HomePage.CURRENCY_DROPDOWN).click()

        currencies = {
            "EUR": search_visible_element(driver, HomePage.EUR_CURRENCY_BUTTON).click,
            "GBP": search_visible_element(driver, HomePage.GBP_CURRENCY_BUTTON).click,
            "USD": search_visible_element(driver, HomePage.USD_CURRENCY_BUTTON).click,
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
