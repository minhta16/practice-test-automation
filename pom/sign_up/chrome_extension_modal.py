from pom._base.base_page import BasePage


class ChromeExtensionModal(BasePage):
    next_btn = "#modal-purchase-successful button.gi-Button"
    chrome_modal = "#modal-purchase-successful"

    def click_next(self):
        self.driver.wait_then_click(self.next_btn)

    def check_modal_visible(self):
        chrome_modal = self.driver.wait_until_visible_and_get_element(self.chrome_modal)
        return chrome_modal is not None
