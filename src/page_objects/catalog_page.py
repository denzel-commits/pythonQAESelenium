from selenium.webdriver.common.by import By
from src.base_classes.base_page import BasePage


class CatalogPage(BasePage):
    LEFT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-left .list-group a")
    SWIPER_SLIDER = (By.CSS_SELECTOR, "#column-left .swiper-viewport")
    SHOW_DROPDOWN = (By.CSS_SELECTOR, "#input-limit")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
