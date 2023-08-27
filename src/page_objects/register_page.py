from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class RegisterPage(BasePage):
    PAGE_URL = "/index.php?route=account/register"

    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='checkbox']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-firstname")
    SUBSCRIBE_YES_RADIO = (By.CSS_SELECTOR, ".form-horizontal input[name='newsletter'][value='1']")
    SUBSCRIBE_NO_RADIO = (By.CSS_SELECTOR, ".form-horizontal input[name='newsletter'][value='0']")
    RIGHT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-right .list-group a")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver.get(base_url + self.PAGE_URL)


