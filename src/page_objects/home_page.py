import random

from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage
from src.page_objects.elements.product_item_element import ProductItemElement
from src.page_objects.product_page import ProductPage


class HomePage(BasePage):
    PAGE_URL = ""

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver.get(base_url + self.PAGE_URL)
