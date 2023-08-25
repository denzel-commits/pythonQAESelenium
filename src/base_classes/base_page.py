from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.utils import make_screenshot


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def click(self, element):
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def get_element(self, locator, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            make_screenshot(self.driver, self.driver.session_id)
            raise AssertionError("WebElement is not visible")

    def find_element_from_element(self, parent_locator, child_locator, timeout=3):
        return self.get_element(parent_locator).get_element(child_locator)

    def get_elements(self, locator, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            make_screenshot(self.driver, self.driver.session_id)
            raise AssertionError("WebElement is not visible")
