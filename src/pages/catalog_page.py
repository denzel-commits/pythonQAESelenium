from selenium.webdriver.common.by import By


class CatalogPage:
    LEFT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-left .list-group a")
    SWIPER_SLIDER = (By.CSS_SELECTOR, "#column-left .swiper-viewport")
    SHOW_DROPDOWN = (By.CSS_SELECTOR, "#input-limit")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "#input-sort")
    GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")

    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    EUR_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='EUR']")
    GBP_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='GBP']")
    USD_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-menu button[name='USD']")
