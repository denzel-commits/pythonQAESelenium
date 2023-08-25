import random

from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage
from src.page_objects.elements.product_item_element import ProductItemElement


class HomePage(BasePage):
    PAGE_URL = ""
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, ".product-layout")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver.get(base_url + self.PAGE_URL)

    def _get_featured_products(self) -> list[ProductItemElement]:
        products = self.get_elements(self.FEATURED_PRODUCTS)
        return [ProductItemElement(self.driver, product) for product in products]

    def get_random_featured_product(self):
        # exclude last two products as they cannot be added to the cart
        return random.choice(
            self._get_featured_products()[0:2]
        )

    def get_featured_products_prices(self):
        products = self._get_featured_products()
        return [product.get_price() for product in products]


    # def click_random_featured_product(self):
    #     products = self._get_featured_products()
    #     random.choice(products).get_image_element().click()
    #     return self
    #
    # def click_featured_product(self, index):
    #     products = self._get_featured_products()
    #     products[index].get_image_element().click()
    #     return self
