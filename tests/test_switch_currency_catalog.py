from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_switch_currency(browser: Remote):
    """Меняю валюту и проверяю на главное странице что она изменилась"""
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a'))).click() # Открываю выбор валют
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/a'))).click() # Выбираю доллары

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/a'))).click()
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/a'))).click() # Перехожу на страницу каталога лэптопов

    element = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="product-list"]/div[3]/div/div[2]/div/div/span[1]'))) #Записываем элемент в переменную
    browser.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем к элементу
    if element.text[0] != '$': # Проверяю что цена в долларах
        raise ValueError(f'Цена не изменилась на доллары на товаре: {element.text}')

    element = browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]')
    browser.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем к корзине
    if element.text[0] != '$': # Проверяю что цена в долларах
        raise ValueError(f'Цена не изменилась на доллары на товаре: {element.text}')
    




    