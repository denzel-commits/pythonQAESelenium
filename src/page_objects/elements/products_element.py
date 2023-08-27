import random

from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage
from src.interfaces.abstract_products_element import AbstractProductsElement
from src.page_objects.elements.product_item_element import ProductItemElement
from src.page_objects.product_page import ProductPage


class ProductsElement(BasePage, AbstractProductsElement):
    PRODUCTS_LOCATOR = (By.CSS_SELECTOR, ".product-layout")

    def get_products(self) -> list[ProductItemElement]:
        products = self.get_elements(self.PRODUCTS_LOCATOR)
        return [ProductItemElement(self.driver, product) for product in products]

    def get_random_product(self) -> ProductItemElement:
        # exclude last two products as they cannot be added to the cart
        return random.choice(
            self.get_products()[0:2]
        )

    def get_products_prices(self) -> list[str]:
        products = self.get_products()
        return [product.get_price() for product in products]

    def click_on_product_image(self, index) -> ProductPage:
        product = self.get_products()[index]
        product.get_image_element().click()
        return ProductPage(self.driver)