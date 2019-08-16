from selenium.webdriver.common.by import By
from selenium import webdriver
from constants.paypal import PaypalConstants
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import os
import time


class PracticeAsker():

    def __init__(self):
        driver_location = "drivers/chromedriver"
        os.environ['webdriver.chrome.driver'] = driver_location
        self.driver = webdriver.Chrome(executable_path=driver_location)
        self.driver.maximize_window()

        # Implicit wait until 10 then raise, NOT wait until 10th sec to find element
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.got-it.tech/solutions/excel-chat')

        key = "gotit.excel.asker.turnOffExtension"
        self.driver.execute_script(f'localStorage.setItem("{key}", true);')

        self.main_window_handle = self.driver.current_window_handle

        # After finish, raise timeout exception if element not found
        self.wait = WebDriverWait(driver=self.driver, timeout=15, poll_frequency=1)

    # STEP 1: User purchase package 1 personal at pricing tab by Paypal
    def purchase_paypal(self):
        driver = self.driver

        # Click on pricing tab
        driver.find_element_by_css_selector("#pricing-navlink-landing").click()

        # Click the first pricing option
        driver.find_elements_by_css_selector("div.gi-pricingItem-Button")[0].click()

        # Choose Paypal option
        self.wait_until_clickable_and_get_element("div.braintree-option.braintree-option__paypal").click()

        # Click Paypal button
        paypal_frame = self.wait_until_clickable_and_get_element(".zoid-component-frame.zoid-visible")
        self.driver.switch_to.frame(paypal_frame)
        self.wait_until_clickable_and_get_element(".paypal-button.paypal-button-shape-pill").click()
        self.driver.switch_to.default_content()

        # Switch to Paypal popup
        driver.switch_to.window(self.get_popup_handle())

        # Enter Paypal credential

        # Enter email
        email_field = self.wait_until_visible_and_get_element("#email[name='login_email']")
        email_field.send_keys(PaypalConstants.PAYPAL_EMAIL)

        # Click Next button
        driver.find_element_by_css_selector("button.button.actionContinue[name='btnNext']").click()

        # Enter password
        password_field = self.wait_until_visible_and_get_element("#password[name='login_password']")
        password_field.send_keys(PaypalConstants.PAYPAL_PASSWORD)

        # Click Login
        driver.find_element_by_css_selector("#btnLogin").click()

        # Click Continue Payment
        # Need to sleep because there is a temporary loading overlay which prevents clicking the button
        continue_btn = self.wait_until_clickable_and_get_element("#button")
        time.sleep(4)
        continue_btn.click()

        # Click Agree & Continue
        agree_btn = self.wait_until_clickable_and_get_element("#confirmButtonTop")
        time.sleep(4)
        agree_btn.click()

        # Switch back to main window
        driver.switch_to.window(self.main_window_handle)

        # Wait until Paypal overlay disappears, Paypal check appears, then click Pay now
        time.sleep(2)
        self.wait_until_invisible_and_get_element("div.paypal-checkout-sandbox")
        # Wait until paypal check appears
        time.sleep(2)
        self.wait_until_clickable_and_get_element("#modal-payment-subscription-engine button.gi-Button").click()

    # STEP 2: User enter email/password -> signup success
    def sign_up(self):
        driver = self.driver

        # Enter email, append with random number behind it
        self.wait_until_visible_and_get_element("input.gi-Input[name='email']").send_keys('mta+{}@gotitapp.co'.format(time.time()))

        # Enter password and confirm password
        driver.find_element_by_css_selector("input.gi-Input[name='password']").send_keys('1ConVit!')
        driver.find_element_by_css_selector("input.gi-Input[name='confirmPassword']").send_keys('1ConVit!')

        # Click Sign Up button
        self.wait_until_clickable_and_get_element("#modal-signup #sign-up-button").click()

        # Click Next
        self.wait_until_clickable_and_get_element("#modal-terms-and-conditions button.gi-Button.gi-Button--accent").click()

    def confirm_modal_and_session_balance(self):
        initial_balance = self.wait_until_visible_and_get_element("#test-session-balance-header-button>strong").text
        print('Initial Balance:', initial_balance)

        # STEP 3: verify purchase success modal presented at home page
        self.wait_until_clickable_and_get_element("#modal-purchase-successful button.gi-Button").click()

        # STEP 4: User session balance should be an increase at home page
        current_balance = self.driver.find_element_by_css_selector("#test-session-balance-header-button>strong").text
        print('Updated Balance:', current_balance)

        if initial_balance != current_balance:
            print('Balance is updated!')
        else:
            raise Exception('Balance fails to update.')

    def start_test(self):
        self.purchase_paypal()
        self.sign_up()
        self.confirm_modal_and_session_balance()
        print('Test completed!')
        self.driver.close()

    def get_popup_handle(self):
        # verify link
        window_handle = None
        while not window_handle:
            for handle in self.driver.window_handles:
                if handle != self.main_window_handle:
                    window_handle = handle
        return window_handle

    def wait_until_invisible_and_get_element(self, selector):
        return self.wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_until_clickable_and_get_element(self, selector):
        return self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_until_visible_and_get_element(self, selector):
        return self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def javascript_click(self, selector):
        element = self.wait_until_clickable_and_get_element(selector)
        self.driver.execute_script("arguments[0].click();", element)


test_case = PracticeAsker()
test_case.start_test()
