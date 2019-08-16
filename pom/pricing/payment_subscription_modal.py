from pom._base.base_page import BasePage
import time


class PaymentSubscriptionModal(BasePage):
    paypal_paying_option = "div.braintree-option.braintree-option__paypal"
    paypal_frame = ".zoid-component-frame.zoid-visible"
    paypal_button_in_frame = ".paypal-button-logo.paypal-button-logo-paypal.paypal-button-logo-gold"
    pay_now_btn = "#modal-payment-subscription-engine button.gi-Button"
    paypal_dark_overlay = "div.paypal-checkout-sandbox"

    def click_paypal_paying_option(self):
        self.driver.wait_then_click(self.paypal_paying_option)

    def click_paypal_frame_button(self):
        paypal_frame = self.driver.wait_until_clickable_and_get_element(self.paypal_frame)
        self.driver.switch_to_frame(paypal_frame)
        time.sleep(2)
        self.driver.wait_then_click(self.paypal_button_in_frame)
        self.driver.switch_to_default()

    def switch_to_paypal_popup(self):
        self.driver.switch_to_next_window()

    def click_pay_now(self):
        self.driver.switch_to_main_window()
        self.driver.wait_until_invisible_and_get_element(self.paypal_dark_overlay)
        time.sleep(2)
        self.driver.wait_then_click(self.pay_now_btn)
