import random
import string
import os.path

from configuration import SCREENSHOTS_PATH


def make_screenshot(driver, filename):
    driver.save_screenshot(os.path.join(SCREENSHOTS_PATH, f"{filename}.png"))


def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_phone():
    return "".join([random.choice(string.digits) for _ in range(10)])


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])

