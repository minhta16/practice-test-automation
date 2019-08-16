from pom._base.base_page import BasePage


class Header(BasePage):
    pricing_tab = "#pricing-navlink-landing"

    def click_pricing_tab(self):
        self.driver.wait_then_click(self.pricing_tab)
