import allure
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


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

    @allure.step("Set username {username}")
    def set_username(self, username):
        self._do_input(self.get_element(self.USERNAME_INPUT),
                       username)
        return self

    @allure.step("Set password {password}")
    def set_password(self, password):
        self._do_input(self.get_element(self.PASSWORD_INPUT),
                       password)
        return self

    @allure.step("Click login button")
    def click_login(self):
        self.click(self.get_element(self.LOGIN_BUTTON))
        return self

    @allure.step("Login with credentials {username} and {password}")
    def login_with(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self._press_enter(self.PASSWORD_INPUT)
        # self.click_login()
        return self

    @allure.step("Click logout button")
    def click_logout(self):
        self.click(self.get_element(self.LOGOUT_LINK))
        return self

    @allure.step("Verify is logged in")
    def verify_is_logged_in(self):
        if self.verify_element_text(self.get_element(self.ADMIN_PAGE_HEADER_H1), "Dashboard"):
            return self
        else:
            raise AssertionError("Admin login failed")

    @allure.step("Click on 'Product' menu")
    def click_products_menu_item(self):
        self.click(self.get_element(self.CATALOG_MENU_ITEM))
        self.click(self.get_element(self.PRODUCTS_MENU_ITEM))
        return self
