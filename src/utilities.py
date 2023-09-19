import random
import string

from configuration import CURRENCY_SYMBOLS


def random_string(length=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])


def random_phone():
    return "".join([random.choice(string.digits) for _ in range(10)])


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])


def get_currency_rates():
    return {"EUR": 0.78460002, "GBP": 0.61250001}


def convert_currency(price, convert_from, convert_to):
    return round(sanitize_price(price, convert_from) * get_currency_rates()[convert_to], 2)


def sanitize_price(price, currency_code):
    return float(price.replace(CURRENCY_SYMBOLS[currency_code], ""))
