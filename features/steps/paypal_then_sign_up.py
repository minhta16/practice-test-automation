from behave import *
from pom.pricing.payment_modal import PaymentModal
from pom.pricing.paypal_popup import PaypalPopup
from pom.sign_up.sign_up_modal import SignUpModal
from pom.sign_up.policy_modal import PolicyModal
from pom.sign_up.purchase_successful_modal import PurchaseSuccessfulModal
from pom.landing.landing_page import LandingPage
from pom.pricing.pricing_page import PricingPage


@step('I am at landing page')
def step_impl(context):
    context.browser.get('https://www.got-it.tech/solutions/excel-chat')

    # Need this key to turn off Chrome Extension modal
    key = "gotit.excel.asker.turnOffExtension"
    context.browser.execute_script(f'localStorage.setItem("{key}", true);')

    LandingPage(context.browser).click_pricing_tab()


@step('I purchase package {index} personal at pricing tab by Paypal')
def step_impl(context, index):
    PricingPage(context.browser).click_purchase_option_by_index(int(index))

    payment_modal = PaymentModal(context.browser)
    payment_modal.click_paypal_paying_option()
    payment_modal.click_paypal_frame_button()
    payment_modal.switch_to_paypal_popup()

    paypal_popup = PaypalPopup(context.browser)
    paypal_popup.log_in()

    paypal_popup.click_continue_payment_button()
    paypal_popup.click_agree_and_continue_button()

    payment_modal.click_pay_now_button()


@step('I signup successfully')
def step_impl(context):
    SignUpModal(context.browser).sign_up()


@step('I confirm all policies')
def step_impl(context):
    PolicyModal(context.browser).click_next_button()


@then('I should see my balance to be {balance}')
def step_impl(context, balance):
    assert LandingPage(context.browser).get_balance() == balance


@then('I should see a sign up successful modal')
def step_impl(context):
    chrome_modal = PurchaseSuccessfulModal(context.browser)
    assert chrome_modal.check_modal_visible()
