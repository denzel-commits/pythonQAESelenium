from selenium import webdriver


def test_first(driver, base_url):
    driver.get(base_url)
    assert driver.title == "Официальный магазин Алексея и Ольги Валяевых"
