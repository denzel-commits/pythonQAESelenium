import random

from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage
from src.page_objects.catalog_page import CatalogPage
from src.page_objects.elements.product_item_element import ProductItemElement
from src.page_objects.product_page import ProductPage


class HomePage(BasePage):
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
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

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver.get(base_url)

    def set_currency(self, currency_code):
        self.get_element(self.CURRENCY_DROPDOWN).click()

        currencies = {
            "EUR": self.get_element(self.EUR_CURRENCY_BUTTON).click,
            "GBP": self.get_element(self.GBP_CURRENCY_BUTTON).click,
            "USD": self.get_element(self.USD_CURRENCY_BUTTON).click,
        }
        currencies[currency_code]()

        return self

    def click_cart_button(self):
        self.get_element(self.CART_BUTTON).click()
        return self

    def product_is_in_cart(self, product_name):
        self.click_cart_button()

        cart_product_names = [cart_item.find_element(*self.CART_ITEM_NAME).text
                              for cart_item in self.get_elements(self.CART_ITEMS)
                              ]

        return product_name in cart_product_names

    def click_menu_item_by_name(self, target_name):
        for item in self.get_elements(self.TOP_MENU_ITEMS):
            if item.text == target_name:
                item.click()
                break

        return CatalogPage(self.driver)
