from pom._base.base_page import BasePage


class PurchaseSuccessfulModal(BasePage):
    next_btn = "#modal-purchase-successful button.gi-Button"
    purchase_successful_modal = "#modal-purchase-successful"

    def click_next(self):
        self.driver.wait_then_click(self.next_btn)

    def check_modal_visible(self):
        purchase_successful_modal = self.driver.wait_until_visible_and_get_element(self.purchase_successful_modal, timeout=15)
        return purchase_successful_modal is not None
