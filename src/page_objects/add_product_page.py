from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.base_classes.base_page import BasePage


class AddProductPage(BasePage):
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name1")
    META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title1")

    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    PRICE_INPUT = (By.CSS_SELECTOR, "#input-price")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "#input-quantity")
    STOCK_STATUS_SELECT = (By.CSS_SELECTOR, "#input-stock-status")

    CATEGORIES_INPUT = (By.CSS_SELECTOR, "#input-category")
    FIRST_CATEGORY = (By.CSS_SELECTOR, "#input-category+.dropdown-menu li:first-child")

    IMAGE_INPUT = (By.CSS_SELECTOR, ".note-image-input input[type='file']")

    DATA_TAB = (By.CSS_SELECTOR, "#form-product .nav-tabs a[href='#tab-data']")
    LINKS_TAB = (By.CSS_SELECTOR, "#form-product .nav-tabs a[href='#tab-links']")
    IMAGE_TAB = (By.CSS_SELECTOR, "#form-product .nav-tabs a[href='#tab-image']")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".container-fluid button[data-original-title='Save']")

    def fill_add_product_form_with(self, product):
        self.set_product_name(product["product_name"]) \
            .set_meta_tags(product["meta_tags"]) \
            .click_data_tab() \
            .set_model(product["model"]) \
            .set_price(product["price"]) \
            .set_quantity(product["quantity"]) \
            .set_stock_status(product["stock_status_id"]) \
            .click_links_tab() \
            .set_category(product["category"])
        # .click_image_tab() \
        # .set_image(product["image"]) \

        return self

    def fill_add_product_form_req_fields_with(self, product):
        self.set_product_name(product["product_name"]) \
            .set_meta_tags(product["meta_tags"]) \
            .click_data_tab() \
            .set_model(product["model"]) \

        return self

    def set_product_name(self, name):
        self._do_input(self.get_element(self.PRODUCT_NAME_INPUT), name)
        return self

    def set_meta_tags(self, meta_tags):
        self._do_input(self.get_element(self.META_TAG_INPUT), meta_tags)
        return self

    def set_model(self, model):
        self._do_input(self.get_element(self.MODEL_INPUT), model)
        return self

    def set_quantity(self, quantity):
        self._do_input(self.get_element(self.QUANTITY_INPUT), quantity)
        return self

    def set_price(self, price):
        self._do_input(self.get_element(self.PRICE_INPUT), price)
        return self

    def set_category(self, category):
        self._do_input(self.get_element(self.CATEGORIES_INPUT), category)
        self.click(self.get_element(self.FIRST_CATEGORY))
        return self

    def set_stock_status(self, stock_status):
        stock_status_select = Select(self.get_element(self.STOCK_STATUS_SELECT))
        stock_status_select.select_by_value(stock_status)
        return self

    def set_image(self, image_url):
        WebDriverWait(self.browser, timeout=5) \
            .until(EC.presence_of_element_located(self.IMAGE_INPUT)) \
            .send_keys(image_url)

        # self._do_input(self.get_element(self.IMAGE_INPUT), image_url)
        return self

    def click_data_tab(self):
        self.click(self.get_element(self.DATA_TAB))
        return self

    def click_links_tab(self):
        self.click(self.get_element(self.LINKS_TAB))
        return self

    def click_image_tab(self):
        self.click(self.get_element(self.IMAGE_TAB))
        return self

    def click_save_button(self):
        self.click(self.get_element(self.SAVE_BUTTON))
        return self
