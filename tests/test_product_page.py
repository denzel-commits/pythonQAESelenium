import pytest
from src.page_objects.product_page import ProductPage
from src.page_objects.home_page import HomePage


class TestProduct:

    @pytest.mark.parametrize("index", [0, 1, 2, 3])
    def test_product_page_elements(self, index, driver, base_url, products_element):
        HomePage(driver, base_url)
        product_page = products_element.click_on_product_image(index)

        product_page.get_element(ProductPage.PRODUCT_NAME)
        product_page.get_element(ProductPage.PRODUCT_PRICE)
        product_page.get_element(ProductPage.PRODUCT_BRAND_LINK)
        product_page.get_element(ProductPage.PRODUCT_AVAILABILITY)
        product_page.get_element(ProductPage.QUANTITY_INPUT)
        product_page.get_element(ProductPage.ADD_TO_CART_BUTTON)
        product_page.get_element(ProductPage.ADD_TO_WISHLIST_BUTTON)
        product_page.get_element(ProductPage.ADD_TO_COMPARISON_BUTTON)
