from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage


class CatalogPage(BasePage):
    PAGE_URL = "/smartphone"

    LEFT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-left .list-group a")
    SWIPER_SLIDER = (By.CSS_SELECTOR, "#column-left .swiper-viewport")
    SHOW_DROPDOWN = (By.CSS_SELECTOR, "#input-limit")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver.get(base_url + self.PAGE_URL)


