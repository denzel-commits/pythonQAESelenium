from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage
from src.page_objects.elements.webtable import WebTableElement


class ManageProductsPage(BasePage):
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".container-fluid a[data-original-title='Add New']")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".container-fluid button[data-original-title='Delete']")

    CHECKBOX_ALL = (By.CSS_SELECTOR, "#form-product table thead tr:first-child td:first-child input[type='checkbox']")
    FILTER_MODEL_INPUT = (By.CSS_SELECTOR, "#filter-product #input-model")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#filter-product #button-filter")

    NO_RESULTS = (By.CSS_SELECTOR, "#form-product tbody>tr>td")
    PRODUCT_LIST_TABLE = (By.CSS_SELECTOR, "#form-product table tbody")

    def set_filter_model(self, model):
        self._do_input(self.get_element(self.FILTER_MODEL_INPUT), model)
        return self

    def click_filter_button(self):
        self.click(self.get_element(self.FILTER_BUTTON))
        return self

    def click_checkbox_all(self):
        self.click(self.get_element(self.CHECKBOX_ALL))
        return self

    def click_add_new_product(self):
        self.click(self.get_element(self.ADD_NEW_PRODUCT_BUTTON))
        return self

    def click_delete_product(self):
        self.click(self.get_element(self.DELETE_PRODUCT_BUTTON))
        return self

    def accept_delete_alert(self):
        self.browser.switch_to.alert.accept()
        return self

    def has_filter_results(self):
        return not self.verify_element_text(self.get_element(self.NO_RESULTS), 'No results!')

    def has_product_in_list(self, product_identifier):
        assert self.is_present((By.XPATH, f"//td[text() = '{product_identifier}']"))

    def has_no_product_in_list(self, product_identifier):
        assert self.is_not_present((By.XPATH, f"//td[text() = '{product_identifier}']"))

    def click_product_checkbox(self, product_identifier):
        product_table = WebTableElement(self.browser, self.PRODUCT_LIST_TABLE)
        row_number = product_table.get_row_idx_for(product_identifier)

        self.click(product_table.get_cell_input_element(row_number, 1))
        return self
