import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(browser: Remote):
    """Добавляю случайный товар в корзину и проверяю что он появился в корзине"""
    span_elem = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    if span_elem.text != '0 item(s) - $0.00':
        raise ValueError(f'Корзина уже заполнена: {span_elem.text}')
    
    elem = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]') #Записываем элемент в переменную
    browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к элементу
    time.sleep(2)
    elem.click()

    elem = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button') #Записываем элемент в переменную
    browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к элементу
    time.sleep(2)

    span_elem = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    if span_elem.text != '1 item(s) - 472.33€':
        raise ValueError(f'Корзина уже заполнена: {span_elem.text}')
    
    
    