from selenium.webdriver.common.by import By

def test_on1(browser):
    browser.get("https://google.com")
    assert browser.title == "Google"

def test_on2(browser):
    browser.get("https://google.com")
    assert browser.title == "Goo1gle"

def test_on3(browser):
    browser.get("https://google.com")
    assert browser.title != "Google"

def test_on4(browser):
    browser.get("https://google.com")
    assert browser.title != "1Google"

def test_on5(browser):
    browser.get("https://yandex.ru")
    assert browser.title == "Дзен"
    browser.refresh
    browser.find_element(By.XPATH, '//button')
