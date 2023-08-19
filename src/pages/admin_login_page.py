from selenium.webdriver.common.by import By


class AdminLoginPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[text()=' Login']")
    FORGOTTEN_PASSWORD_LINK = (By.LINK_TEXT, "Forgotten Password")
    HOME_LINK = (By.CSS_SELECTOR, "#header-logo")
