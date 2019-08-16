from pom._base.base_page import BasePage


class PolicyModal(BasePage):
    next_policy_btn = "#modal-terms-and-conditions button.gi-Button.gi-Button--accent"

    def click_next(self):
        self.driver.wait_then_click(self.next_policy_btn)
