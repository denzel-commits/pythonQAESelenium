from selenium.webdriver.common.by import By

from src.base_classes.base_page import BasePage


class UserPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-email")
    PHONE_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-password")
    CONFIRM_INPUT = (By.CSS_SELECTOR, ".form-horizontal #input-confirm")

    SUBSCRIBE_YES_RADIO = (By.CSS_SELECTOR, ".form-horizontal input[name='newsletter'][value='1']")
    SUBSCRIBE_NO_RADIO = (By.CSS_SELECTOR, ".form-horizontal input[name='newsletter'][value='0']")

    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='checkbox']")

    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".form-horizontal .buttons [type='submit']")

    RIGHT_MENU_ITEMS = (By.CSS_SELECTOR, "#column-right .list-group a")

    CREATED_ACCOUNT_HEADER = (By.CSS_SELECTOR, "#content H1")

    def set_firstname(self, firstname):
        self._do_input(self.get_element(self.FIRSTNAME_INPUT),
                       firstname)
        return self

    def set_lastname(self, lastname):
        self._do_input(self.get_element(self.LASTNAME_INPUT),
                       lastname)
        return self

    def set_email(self, email):
        self._do_input(self.get_element(self.EMAIL_INPUT),
                       email)
        return self

    def set_telephone(self, phone):
        self._do_input(self.get_element(self.PHONE_INPUT),
                       phone)
        return self

    def set_password(self, password):
        self._do_input(self.get_element(self.PASSWORD_INPUT),
                       password)
        return self

    def set_password_confirm(self, password):
        self._do_input(self.get_element(self.CONFIRM_INPUT),
                       password)
        return self

    def subscribe(self, choice="No"):
        if choice.lower() == "yes":
            self.click(self.get_element(self.SUBSCRIBE_YES_RADIO))
        else:
            self.click(self.get_element(self.SUBSCRIBE_NO_RADIO))

        return self

    def check_privacy_policy(self):
        self.click(self.get_element(self.PRIVACY_POLICY_CHECKBOX))
        return self

    def click_continue(self):
        self.click(self.get_element(self.CONTINUE_BUTTON))
        return self

    def verify_account_created(self):
        assert "Your Account Has Been Created!" == self.get_element(self.CREATED_ACCOUNT_HEADER).text

