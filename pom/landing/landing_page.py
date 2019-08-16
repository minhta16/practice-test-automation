from pom._base.base_page import BasePage


class LandingPage(BasePage):
    balance_text = "#test-session-balance-header-button>strong"
    next_btn = "#modal-purchase-successful button.gi-Button"

    def check_balance_change(self):
        initial_balance = self.driver.wait_until_visible_and_get_element(self.balance_text).text
        self.driver.wait_until_clickable_and_get_element(self.next_btn)
        current_balance = self.driver.find_element(self.balance_text).text
        return initial_balance != current_balance
