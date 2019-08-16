from pom._base.base_page import BasePage
from constants.paypal import PaypalConstants
import time


class PaypalPopup(BasePage):
    email_text_field = "#email[name='login_email']"
    password_text_field = "#password[name='login_password']"
    next_to_password = "button.button.actionContinue[name='btnNext']"
    login_btn = "#btnLogin"
    continue_payment_btn = "#button"
    agree_continue_btn = "#confirmButtonTop"

    def _enter_email(self):
        email_field = self.driver.wait_until_visible_and_get_element(self.email_text_field)
        email_field.send_keys(PaypalConstants.PAYPAL_EMAIL)

    def _click_next_to_password(self):
        self.driver.wait_then_click(self.next_to_password)

    def _enter_password(self):
        password_field = self.driver.wait_until_visible_and_get_element(self.password_text_field)
        password_field.send_keys(PaypalConstants.PAYPAL_PASSWORD)

    def _click_login(self):
        self.driver.wait_then_click(self.login_btn)

    def log_in(self):
        self._enter_email()
        self._click_next_to_password()
        self._enter_password()
        self._click_login()

    def click_continue_payment(self):
        time.sleep(2)
        self.driver.wait_then_click(self.continue_payment_btn)

    def click_agree_and_continue(self):
        self.driver.wait_then_click(self.agree_continue_btn)
