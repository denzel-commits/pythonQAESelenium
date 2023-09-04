import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities import make_screenshot


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _do_input(self, element, text):
        self.click(element)
        element.clear()
        self.__send_keys_one_by_one(element, text)

    @staticmethod
    def __send_keys_one_by_one(element, text, delay=0.1):
        for char in text:
            time.sleep(delay)
            element.send_keys(char)

    def click(self, element):
        ActionChains(self.browser).move_to_element(element).pause(0.1).click().perform()

    @staticmethod
    def verify_element_text(element, text):
        return element.text == text

    @staticmethod
    def simple_click_element(element):
        element.click()

    def get_element(self, locator, timeout=0):
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            make_screenshot(self.browser, self.browser.session_id)
            raise AssertionError("WebElement is not visible")

    def get_element_from_element(self, parent_locator, child_locator):
        return self.get_element(parent_locator).find_element(*child_locator)

    def get_elements_from_element(self, parent_locator, child_locator):
        return self.get_element(parent_locator).find_elements(*child_locator)

    def get_elements(self, locator, timeout=0):
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            make_screenshot(self.browser, self.browser.session_id)
            raise AssertionError("WebElement is not visible")

    def get_clickable_element(self, locator, timeout=0):
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            make_screenshot(self.browser, self.browser.session_id)
            raise AssertionError("WebElement is not visible or not clickable/disabled")
