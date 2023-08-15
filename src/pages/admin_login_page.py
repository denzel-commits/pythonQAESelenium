from selenium.webdriver.common.by import By
from src.utils import search_visible_element


class AdminLoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")

    HOME_LINK = (By.CSS_SELECTOR, "#header-logo")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        search_visible_element(self.driver, self.USERNAME_INPUT).clear()
        search_visible_element(self.driver, self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password):
        search_visible_element(self.driver, self.PASSWORD_INPUT).clear()
        search_visible_element(self.driver, self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        search_visible_element(self.driver, self.LOGIN_BUTTON).click()

    def click_forgotten_password(self):
        search_visible_element(self.driver, self.FORGOTTEN_PASSWORD_LINK).click()
