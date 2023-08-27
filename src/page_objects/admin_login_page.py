from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class AdminLoginPage(BasePage):
    PAGE_URL = "/admin"

    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    HOME_LINK = (By.CSS_SELECTOR, "#header-logo")

    ADMIN_PAGE_HEADER_H1 = (By.CSS_SELECTOR, "H1")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver.get(base_url + self.PAGE_URL)

    def enter_username(self, username):
        self._do_input(self.get_element(AdminLoginPage.USERNAME_INPUT),
                       username
                       )
        return self

    def enter_password(self, password):
        self._do_input(self.get_element(AdminLoginPage.PASSWORD_INPUT),
                       password
                       )
        return self

    def click_login(self):
        self.get_element(self.LOGIN_BUTTON).click()
        return self

    def press_enter(self):
        self.get_element(AdminLoginPage.PASSWORD_INPUT).send_keys(Keys.RETURN)
        return self

    def is_logged_in(self):
        return self.get_element(self.ADMIN_PAGE_HEADER_H1).text == "Dashboard"

    def click_logout(self):
        self.get_element(self.LOGOUT_LINK).click()
        return self
