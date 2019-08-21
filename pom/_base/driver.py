from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


class CreateDriver:
    def __init__(self, driver):
        self.driver = driver
        self.main_window_handle = self.driver.current_window_handle

    def find_element(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def find_elements(self, selector):
        return self.driver.find_elements(By.CSS_SELECTOR, selector)

    def wait_until_invisible(self, selector, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_until_clickable_and_get_element(self, selector, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_until_visible_and_get_element(self, selector, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def switch_to_frame(self, selector):
        self.driver.switch_to.frame(selector)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, link):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if link in self.driver.current_url:
                break

    def wait_then_click(self, locator, timeout=10):
        self.wait_until_visible_and_get_element(locator, timeout=timeout)
        element = self.wait_until_clickable_and_get_element(locator, timeout=timeout)
        time.sleep(1)
        element.click()
