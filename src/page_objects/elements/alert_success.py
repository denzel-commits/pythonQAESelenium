import allure
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class AlertSuccessElement(BasePage):
    SELF = (By.CSS_SELECTOR, ".alert-success")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".alert-success .close")

    @allure.step
    def verify_success_message(self, message="Success: You have modified products!"):
        close_text = self.get_element(self.CLOSE_BUTTON).text
        self.logger.info("{}: Alert message: '{}'".format(self.class_name,
                                                          self.get_element(self.SELF).text.replace(close_text,
                                                                                                   "").strip()))

        assert message == self.get_element(self.SELF).text.replace(close_text, "").strip()
