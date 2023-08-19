import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import SCREENSHOTS_PATH


def search_visible_element(driver, locator, timeout=3):
    try:
        return WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        make_screenshot(driver, driver.session_id)
        raise AssertionError("WebElement is not visible")


def search_visible_elements(driver, locator, timeout=3):
    try:
        return WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))
    except TimeoutException:
        make_screenshot(driver, driver.session_id)
        raise AssertionError("WebElement is not visible")


def search_present_element(driver, locator, timeout=3):
    try:
        return WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        make_screenshot(driver, driver.session_id)
        raise AssertionError("WebElement is not present ")


def search_clickable_element(driver, locator, timeout=3):
    try:
        return WebDriverWait(driver, timeout=timeout).until(EC.element_to_be_clickable(locator))
    except TimeoutException:
        make_screenshot(driver, driver.session_id)
        raise AssertionError("WebElement is not visible or not clickable/disabled")


def make_screenshot(driver, filename):
    driver.save_screenshot(f"{SCREENSHOTS_PATH}{filename}.png")


def send_keys_by_one(element, text, delay=0.1):
    for char in text:
        time.sleep(delay)
        element.send_keys(char)
