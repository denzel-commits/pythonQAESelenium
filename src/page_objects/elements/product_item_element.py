from selenium.common import NoSuchElementException

from src.base_classes.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductItemElement(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".image")

    OLD_PRICE = (By.CSS_SELECTOR, ".caption .price .price-old")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".caption .price")
    TAX_PRICE = (By.CSS_SELECTOR, ".caption .price .price-tax")

    CART_BUTTON = (By.CSS_SELECTOR, ".button-group button:first-child")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".button-group button[data-original-title='Add to Wish List']")
    COMPARE_BUTTON = (By.CSS_SELECTOR, ".button-group  button[data-original-title='Compare this Product']")

    def __init__(self, driver, root):
        super().__init__(driver)
        self.root = root

    def get_name(self) -> str:
        return self.root.find_element(*self.PRODUCT_NAME).text

    def get_price(self) -> str:
        try:
            old_price = self.root.find_element(*self.OLD_PRICE).text
        except NoSuchElementException:
            old_price = ""

        product_price = self.root.find_element(*self.PRODUCT_PRICE).text
        tax_price = self.root.find_element(*self.TAX_PRICE).text

        return product_price.replace(tax_price, "").replace(old_price, "").strip()

    def add_to_cart(self):
        self.click(self.root.find_element(*self.CART_BUTTON))

    def get_image_element(self):
        return self.root.find_element(*self.PRODUCT_IMAGE)
