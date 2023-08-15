from configuration import PRODUCT_HTC_PATH
from src.pages.product_page import ProductPage
from src.utils import search_visible_element


class TestProduct:

    def test_product_page_elements(self, driver, base_url):
        driver.get(base_url + PRODUCT_HTC_PATH)

        search_visible_element(driver, ProductPage.PRODUCT_NAME)
        search_visible_element(driver, ProductPage.PRODUCT_PRICE)
        search_visible_element(driver, ProductPage.PRODUCT_BRAND_LINK)
        search_visible_element(driver, ProductPage.PRODUCT_AVAILABILITY)
        search_visible_element(driver, ProductPage.QUANTITY_INPUT)
        search_visible_element(driver, ProductPage.ADD_TO_CART_BUTTON)
        search_visible_element(driver, ProductPage.ADD_TO_WISHLIST_BUTTON)
        search_visible_element(driver, ProductPage.ADD_TO_COMPARISON_BUTTON)
