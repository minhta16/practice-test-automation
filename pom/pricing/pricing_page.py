from pom._base.base_page import BasePage


class PricingPage(BasePage):
    pricing_options = ".gi-pricingItem-Button"

    def click_purchase_option_by_index(self, index):
        self.driver.wait_until_clickable_and_get_element(self.pricing_options)
        self.driver.find_elements(self.pricing_options)[index].click()
