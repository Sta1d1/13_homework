import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_switch_currency(browser: Remote):
    """Меняю валюту и проверяю на главное странице что она изменилась"""
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a'))).click() # Открываю выбор валют
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/a'))).click() # Выбираю доллары
    
    element = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/div/div/span[1]') #Записываем элемент в переменную
    browser.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем к элементу
    time.sleep(2)
    
    if element.text != '$602.00': # Проверяю что цена в долларах
         raise ValueError(f'Цена не изменилась на доллары на товаре: {element.text}')
    browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]').click()

    element = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    browser.execute_script("arguments[0].scrollIntoView(true);", element) # Прокручиваем к корзине
    time.sleep(2)

    element = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    if element.text != '1 item(s) - $602.00': # Проверяю что цена в долларах
         raise ValueError(f'Цена не изменилась на доллары в корзине: {element.text}')
