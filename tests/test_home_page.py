from src.utils import search_present_element, search_visible_element
from src.pages.home_page import HomePage
import time


class TestHome:
    def test_home_page_elements(self, driver, base_url):
        driver.get(base_url)
        home_page = HomePage(driver)

        search_visible_element(driver, home_page.SHOPPING_CART_LINK)

        search_visible_element(driver, home_page.CURRENCY_DROPDOWN)
        search_present_element(driver, home_page.EUR_CURRENCY_BUTTON)
        search_present_element(driver, home_page.GBP_CURRENCY_BUTTON)
        search_present_element(driver, home_page.USD_CURRENCY_BUTTON)

        search_visible_element(driver, home_page.SEARCH_INPUT)
        search_visible_element(driver, home_page.SEARCH_BUTTON)
        search_visible_element(driver, home_page.HOME_LINK)
