import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utilities import make_screenshot


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def _do_input(self, element, text):
        self.click(element)
        element.clear()
        self.__send_keys_one_by_one(element, text)

    def __send_keys_one_by_one(self, element, text, delay=0.1):
        self.logger.info("{}: Typing text '{}' key by key".format(self.class_name, text))
        for char in text:
            time.sleep(delay)
            element.send_keys(char)

    def _press_enter(self, locator):
        self.logger.info("{}: Pressing 'ENTER' key on element {}".format(self.class_name, str(locator)))
        self.get_element(locator).send_keys(Keys.RETURN)
        return self

    def click(self, element):
        self.logger.info("{}: Clicking element".format(self.class_name))
        ActionChains(self.browser).move_to_element(element).pause(0.1).click().perform()

    def verify_element_text(self, element, text):
        self.logger.info("{}: Compare element text '{}' with '{}'".format(self.class_name, element.text, text))
        return element.text == text

    def is_present(self, locator):
        self.logger.info("{}: Checking if element is present {}".format(self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout=self.browser.tolerance) \
            .until(EC.visibility_of_element_located(locator))

    def is_not_present(self, locator):
        self.logger.info("{}: Checking if element is not present {}".format(self.class_name, str(locator)))
        try:
            WebDriverWait(self.browser, timeout=self.browser.tolerance).until(EC.visibility_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    def simple_click_element(self, element):
        self.logger.info("{}: Do simple click".format(self.class_name))
        element.click()

    def get_element(self, locator, timeout=0):
        self.logger.info("{}: Getting visible element by locator {}".format(self.class_name, str(locator)))
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            make_screenshot(self.browser, self.browser.session_id)
            self.logger.error("{}: WebElement {} is not visible".format(self.class_name, str(locator)))
            raise AssertionError("WebElement is not visible")

    def get_element_from_element(self, parent_locator, child_locator):
        self.logger.info("{}: Getting visible element {} from element {}".
                         format(self.class_name, str(child_locator), str(parent_locator)))
        return self.get_element(parent_locator).find_element(*child_locator)

    def get_elements_from_element(self, parent_locator, child_locator):
        self.logger.info("{}: Getting all visible elements {} from element {}".
                         format(self.class_name, str(child_locator), str(parent_locator)))
        return self.get_element(parent_locator).find_elements(*child_locator)

    def get_elements(self, locator, timeout=0):
        self.logger.info("{}: Getting all visible elements by locator {}".format(self.class_name, str(locator)))
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            make_screenshot(self.browser, self.browser.session_id)
            self.logger.error("{}: WebElement {} is not visible".format(self.class_name, str(locator)))
            raise AssertionError("WebElement is not visible")

    def get_clickable_element(self, locator, timeout=0):
        self.logger.info("{}: Getting clickable element by locator {}".format(self.class_name, str(locator)))
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            make_screenshot(self.browser, self.browser.session_id)
            self.logger.error("{}: WebElement {} is not clickable".format(self.class_name, str(locator)))
            raise AssertionError("WebElement is not visible or not clickable/disabled")
