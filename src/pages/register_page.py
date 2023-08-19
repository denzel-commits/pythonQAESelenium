from selenium.webdriver.common.by import By


class RegisterPage:
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='submit']")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='checkbox']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-firstname")
    SUBSCRIBE_YES_RADIO = (By.CSS_SELECTOR, ".form-horizontal input[name='newsletter'][value='1']")
    SUBSCRIBE_NO_RADIO = (By.CSS_SELECTOR, ".form-horizontal input[name='newsletter'][value='0']")
    RIGHT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-right .list-group a")
