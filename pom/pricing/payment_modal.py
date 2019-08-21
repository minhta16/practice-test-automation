from pom._base.base_page import BasePage
import time


class PaymentModal(BasePage):
    paypal_paying_option = ".braintree-option.braintree-option__paypal"
    paypal_frame = ".zoid-component-frame.zoid-visible"
    paypal_button_in_frame = ".paypal-button-logo.paypal-button-logo-paypal.paypal-button-logo-gold"
    pay_now_btn = "#modal-payment-subscription-engine button.gi-Button"
    paypal_dark_overlay = ".paypal-checkout-sandbox"

    def click_paypal_paying_option(self):
        self.driver.wait_then_click(self.paypal_paying_option)

    def click_paypal_frame_button(self):
        paypal_frame = self.driver.wait_until_clickable_and_get_element(self.paypal_frame)
        self.driver.switch_to_frame(paypal_frame)
        # Wait until paypal button finished loading
        time.sleep(1)
        self.driver.wait_then_click(self.paypal_button_in_frame)
        self.driver.switch_to_default()

    def switch_to_paypal_popup(self):
        self.driver.switch_to_window('sandbox.paypal.com')

    def click_pay_now_button(self):
        self.driver.switch_to_window('got-it.tech')
        self.driver.wait_until_invisible(self.paypal_dark_overlay)

        # Wait until Pay Now button is ready to click
        time.sleep(2)
        self.driver.wait_then_click(self.pay_now_btn)
