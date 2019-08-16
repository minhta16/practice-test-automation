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

    def wait_until_invisible_and_get_element(self, selector, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_until_clickable_and_get_element(self, selector, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def wait_until_visible_and_get_element(self, selector, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def javascript_click(self, selector):
        element = self.wait_until_clickable_and_get_element(selector)
        self.driver.execute_script("arguments[0].click();", element)

    def switch_to_frame(self, selector):
        self.driver.switch_to.frame(selector)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def switch_to_next_window(self):
        # verify link
        window_handle = None
        while not window_handle:
            for handle in self.driver.window_handles:
                if handle != self.main_window_handle:
                    window_handle = handle
        self.driver.switch_to.window(window_handle)

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.main_window_handle)

    def wait_then_click(self, locator, timeout=10):
        self.wait_until_visible_and_get_element(locator, timeout=timeout)
        element = self.wait_until_clickable_and_get_element(locator, timeout=timeout)
        time.sleep(1)
        element.click()
