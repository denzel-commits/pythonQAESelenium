import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step
    def _do_input(self, element, text):
        self.click(element)
        element.clear()
        self.__send_keys_one_by_one(element, text)

    @allure.step
    def __send_keys_one_by_one(self, element, text, delay=0.1):
        self.logger.info(f"{self.class_name}: Typing text '{text}' key by key")
        for char in text:
            time.sleep(delay)
            element.send_keys(char)

    @allure.step
    def _press_enter(self, locator):
        self.logger.info(f"{self.class_name}: Pressing 'ENTER' key on element {str(locator)}")
        self.simple_click_element(self.get_element(locator))
        self.get_element(locator).send_keys(Keys.RETURN)
        return self

    @allure.step
    def click(self, element):
        self.logger.info(f"{self.class_name}: Clicking element")
        ActionChains(self.browser).move_to_element(element).pause(0.1).click().perform()

    @allure.step
    def verify_element_text(self, element, text):
        self.logger.info(f"{self.class_name}: Compare element text '{element.text}' with '{text}'")
        return element.text == text

    @allure.step
    def is_present(self, locator):
        self.logger.info(f"{self.class_name}: Checking if element is present {str(locator)}")
        return WebDriverWait(self.browser, timeout=self.browser.tolerance) \
            .until(EC.visibility_of_element_located(locator))

    @allure.step
    def is_not_present(self, locator):
        self.logger.info(f"{self.class_name}: Checking if element is not present {str(locator)}")
        try:
            WebDriverWait(self.browser, timeout=self.browser.tolerance).until(EC.visibility_of_element_located(locator))
            return False
        except TimeoutException:
            return True

    @allure.step
    def simple_click_element(self, element):
        self.logger.info(f"{self.class_name}: Do simple click")
        element.click()

    @allure.step
    def get_element(self, locator, timeout=0):
        self.logger.info(f"{self.class_name}: Getting visible element by locator {str(locator)}")
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"{self.class_name}: WebElement {str(locator)} is not visible", exc_info=True)
            raise AssertionError("WebElement is not visible")

    @allure.step
    def get_element_from_element(self, parent_locator, child_locator):
        self.logger.info(f"{self.class_name}: Getting visible element {str(child_locator)} "
                         f"from element {str(parent_locator)}")
        return self.get_element(parent_locator).find_element(*child_locator)

    @allure.step
    def get_elements_from_element(self, parent_locator, child_locator):
        self.logger.info(f"{self.class_name}: Getting all visible elements {str(child_locator)} "
                         f"from element {str(parent_locator)}")
        return self.get_element(parent_locator).find_elements(*child_locator)

    @allure.step
    def get_elements(self, locator, timeout=0):
        self.logger.info(f"{self.class_name}: Getting all visible elements by locator {str(locator)}")
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error(f"{self.class_name}: WebElement {str(locator)} is not visible", exc_info=True)
            raise AssertionError("WebElement is not visible")

    @allure.step
    def get_clickable_element(self, locator, timeout=0):
        self.logger.info(f"{self.class_name}: Getting clickable element by locator {str(locator)}")
        timeout = self.browser.tolerance if not timeout else timeout
        try:
            return WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.error(f"{self.class_name}: WebElement {str(locator)} is not clickable", exc_info=True)
            raise AssertionError("WebElement is not visible or not clickable/disabled")
