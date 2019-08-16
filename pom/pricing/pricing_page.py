from pom._base.base_page import BasePage


class PricingPage(BasePage):
    pricing_options = "div.gi-pricingItem-Button"

    def click_first_pricing_option(self):
        self.driver.wait_until_clickable_and_get_element(self.pricing_options)
        self.driver.find_elements(self.pricing_options)[0].click()
