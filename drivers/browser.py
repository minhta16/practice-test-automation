import os
from selenium import webdriver


def get_driver():
    driver_location = "drivers/chromedriver"
    os.environ['webdriver.chrome.driver'] = driver_location
    driver = webdriver.Chrome(executable_path=driver_location)
    driver.maximize_window()
    driver.implicitly_wait(2)
    return driver
