from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content h1~ul li h2")
    PRODUCT_BRAND_LINK = (By.CSS_SELECTOR, "#content h1+ul li:first-child a")
    PRODUCT_AVAILABILITY = (By.CSS_SELECTOR, "#content h1+ul li:last-child")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")

    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR,
                              "#content .btn-group button[data-original-title='Add to Wish List']")
    ADD_TO_COMPARISON_BUTTON = (By.CSS_SELECTOR,
                                "#content .btn-group button[data-original-title='Compare this Product']")
