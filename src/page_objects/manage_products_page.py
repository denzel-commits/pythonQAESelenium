from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class ManageProductsPage(BasePage):
    ADD_NEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".container-fluid a[data-original-title='Add New']")
    DELETE_PRODUCT_BUTTON = (By.CSS_SELECTOR, ".container-fluid button[data-original-title='Delete']")

    CHECKBOX_ALL = (By.CSS_SELECTOR, "#form-product table thead tr:first-child td:first-child input[type='checkbox']")
    FILTER_MODEL_INPUT = (By.CSS_SELECTOR, "#filter-product #input-model")
    FILTER_BUTTON = (By.CSS_SELECTOR, "#filter-product #button-filter")

    def set_filter_model(self, model):
        self._do_input(self.get_element(self.FILTER_MODEL_INPUT), model)
        return self

    def click_filter(self):
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

    def confirm_deletion_alert(self):
        self.browser.switch_to.alert.accept()
        return self
