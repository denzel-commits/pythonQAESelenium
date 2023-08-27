import os.path

from configuration import SCREENSHOTS_PATH


def make_screenshot(driver, filename):
    driver.save_screenshot(os.path.join(SCREENSHOTS_PATH, f"{filename}.png"))
