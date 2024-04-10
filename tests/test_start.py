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