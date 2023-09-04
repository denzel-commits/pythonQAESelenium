from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage
from src.utilities import make_screenshot


class AdminPage(BasePage):
    PAGE_URL = "/admin"

    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    HOME_LINK = (By.CSS_SELECTOR, "#header-logo")

    ADMIN_PAGE_HEADER_H1 = (By.CSS_SELECTOR, "H1")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    CATALOG_MENU_ITEM = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS_MENU_ITEM = (By.XPATH, "//nav[@id='column-left']//ul[@id='menu']//li//a[text()='Products']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser.open(self.PAGE_URL)

    def set_username(self, username):
        self._do_input(self.get_element(self.USERNAME_INPUT),
                       username)
        return self

    def set_password(self, password):
        self._do_input(self.get_element(self.PASSWORD_INPUT),
                       password)
        return self

    def click_login(self):
        self.click(self.get_element(self.LOGIN_BUTTON))
        return self

    def press_enter(self):
        self.get_element(self.PASSWORD_INPUT).send_keys(Keys.RETURN)
        return self

    def login_with(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.press_enter()
        return self

    def click_logout(self):
        self.click(self.get_element(self.LOGOUT_LINK))
        return self

    def verify_is_logged_in(self):
        if self.verify_element_text(self.get_element(self.ADMIN_PAGE_HEADER_H1), "Dashboard"):
            return self
        else:
            make_screenshot(self.browser, "admin_login_test")
            assert False

    def click_products_menu_item(self):
        self.click(self.get_element(self.CATALOG_MENU_ITEM))
        self.click(self.get_element(self.PRODUCTS_MENU_ITEM))
        return self
