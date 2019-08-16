from pom._base.driver import CreateDriver


class BasePage:
    def __init__(self, driver):
        self.driver = CreateDriver(driver)
