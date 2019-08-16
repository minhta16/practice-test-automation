import time
import os

import allure
from allure_commons.types import AttachmentType

from behave import fixture
from drivers.browser import get_driver


@fixture()
def chrome_browser(context):
    context.browser = get_driver()


def take_screenshot(driver, name=""):
    name = name.replace("/", " ")  # escape invalid character '/'
    file_name = str(int(time.time())) + "_" + name + ".png"
    screenshot_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "screenshots/"
    )
    destination_file = screenshot_dir + file_name

    try:
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG,
        )
        driver.save_screenshot(destination_file)
    except NotADirectoryError:
        print("Not a directory issue")
