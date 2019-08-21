from pom._base.base_page import BasePage
from pom.common.header import Header


class LandingPage(BasePage):
    balance_text = "#test-session-balance-header-button>strong"

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.header = Header(driver)

    def get_balance(self):
        return self.driver.wait_until_visible_and_get_element(self.balance_text).text

    def click_pricing_tab(self):
        self.header.click_pricing_tab()
