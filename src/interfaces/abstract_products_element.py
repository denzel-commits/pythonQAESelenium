from abc import ABC, abstractmethod

from src.page_objects.elements.product_item_element import ProductItemElement
from src.page_objects.product_page import ProductPage


class AbstractProductsElement(ABC):

    @abstractmethod
    def get_products(self) -> list[ProductItemElement]:
        pass

    @abstractmethod
    def get_random_product(self) -> ProductItemElement:
        pass

    @abstractmethod
    def get_products_prices(self) -> list[str]:
        pass

    @abstractmethod
    def click_on_product_image(self, index) -> ProductPage:
        pass
