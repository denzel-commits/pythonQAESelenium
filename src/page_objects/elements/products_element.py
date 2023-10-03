import random

import allure
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage
from src.page_objects.elements.product_item_element import ProductItemElement
from src.page_objects.product_page import ProductPage


class ProductsElement(BasePage):
    PRODUCTS_LOCATOR = (By.CSS_SELECTOR, ".product-layout")

    @allure.step("Get products list")
    def get_products(self) -> list[ProductItemElement]:
        products = self.get_elements(self.PRODUCTS_LOCATOR)
        return [ProductItemElement(self.browser, product) for product in products]

    @allure.step("Get random product")
    def get_random_product(self) -> ProductItemElement:
        # exclude last two products as they cannot be added to the cart
        return random.choice(
            self.get_products()[0:2]
        )

    @allure.step("Get products prices")
    def get_products_prices(self) -> list[str]:
        products = self.get_products()
        return [product.get_price() for product in products]

    @allure.step("Open product")
    def click_on_product_image(self, index) -> ProductPage:
        product = self.get_products()[index]
        self.click(product.get_image_element())
        return ProductPage(self.browser)
