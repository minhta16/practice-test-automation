from pom._base.base_page import BasePage
import time


class SignUpModal(BasePage):
    email_field = "input.gi-Input[name='email']"
    sample_email = 'mta+{}@gotitapp.co'.format(time.time())
    password_field = "input.gi-Input[name='password']"
    confirm_password_field = "input.gi-Input[name='confirmPassword']"
    sample_password = '1ConVit!'
    sign_up_btn = "#modal-signup #sign-up-button"

    def _enter_email(self):
        self.driver.wait_until_visible_and_get_element(self.email_field).send_keys(self.sample_email)

    def _enter_password_and_confirm(self):
        self.driver.find_element(self.password_field).send_keys(self.sample_password)
        self.driver.find_element(self.confirm_password_field).send_keys(self.sample_password)

    def _click_sign_up(self):
        self.driver.wait_then_click(self.sign_up_btn)

    def sign_up(self):
        self._enter_email()
        self._enter_password_and_confirm()
        self._click_sign_up()