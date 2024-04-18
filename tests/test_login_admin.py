from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_authorization_logout(browser):
    """Вход и выход в админку с проверкой"""
    browser.get(browser.current_url + 'admin/')
    test_check_url = browser.current_url
    if test_check_url != 'http://localhost/admin/':
        raise ValueError(f'Адреса не равны: {test_check_url}')
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-username"]'))).send_keys('admin')
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="input-password"]'))).send_keys('admin')
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-login"]/div[3]/button'))).click()
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-security"]/div/div/div[1]/button'))).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[2]/div/div[1]')))
    WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-logout"]'))).click()
    test_check_url = browser.current_url
    if test_check_url != 'http://localhost/admin/index.php?route=common/login':
        raise ValueError(f'Адреса не равны: {test_check_url}')
    