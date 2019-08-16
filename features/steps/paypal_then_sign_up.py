from behave import *
from pom.common.header import Header
from pom.pricing.pricing_page import PricingPage
from pom.pricing.payment_subscription_modal import PaymentSubscriptionModal
from pom.pricing.paypal_popup import PaypalPopup
from pom.sign_up.sign_up_modal import SignUpModal
from pom.sign_up.policy_modal import PolicyModal
from pom.sign_up.chrome_extension_modal import ChromeExtensionModal
from pom.landing.landing_page import LandingPage


@Given('I purchase package 1 personal at pricing tab by Paypal')
def step_impl(context):
    context.browser.get('https://www.got-it.tech/solutions/excel-chat')
    key = "gotit.excel.asker.turnOffExtension"
    context.browser.execute_script(f'localStorage.setItem("{key}", true);')

    Header(context.browser).click_pricing_tab()
    PricingPage(context.browser).click_first_pricing_option()

    payment_modal = PaymentSubscriptionModal(context.browser)
    payment_modal.click_paypal_paying_option()
    payment_modal.click_paypal_frame_button()
    payment_modal.switch_to_paypal_popup()

    paypal_popup = PaypalPopup(context.browser)
    paypal_popup.log_in()
    paypal_popup.click_continue_payment()
    paypal_popup.click_agree_and_continue()

    payment_modal.click_pay_now()


@When('I signup successfully')
def step_impl(context):
    SignUpModal(context.browser).sign_up()
    PolicyModal(context.browser).click_next()


@Then('I should see my balance changed')
def step_impl(context):
    assert LandingPage(context.browser).check_balance_change()


@Then('I should see a chrome extension modal')
def step_impl(context):
    chrome_modal = ChromeExtensionModal(context.browser)
    assert chrome_modal.check_modal_visible()
    chrome_modal.click_next()
