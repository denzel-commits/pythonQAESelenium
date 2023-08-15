from selenium.webdriver.common.by import By


class RegisterPage:
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='checkbox']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-firstname")
    SUBSCRIBE_RADIO = (By.CSS_SELECTOR, ".form-horizontal [name='newsletter']")
    RIGHT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-right .list-group a")
