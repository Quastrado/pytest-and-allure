from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import allure
import time

@allure.title('Результат поиска - 10')
@allure.severity(Severity.BLOCKER)
def test_yandex_search():
    driver = webdriver.Chrome()
    with allure.step('Открываем страницу поиска'):
        driver.get('https://ya.ru')
    with allure.step('Ищем market.yandex.ru'):
        search_input = driver.find_element(By.XPATH, '//input[@id="text"]')
    # serach_button = driver.find_element(By.XPATH, '/html/body/main/div[2]/form/div[2]/button/svg')
        search_input.send_keys('market.yandex.ru')
        search_input.send_keys(Keys.ENTER)
    with allure.step('Проверяем что количество результатов - 10'):
        time.sleep(10)
        search_results = driver.find_elements(By.XPATH, '//*[@id="search-result"]/li')
        assert len(search_results) == 10

@allure.title('Заголовок страницы первого результата - "Интернет-магазин Яндекс.Маркет — покупки с быстрой доставкой"')
@allure.severity(Severity.BLOCKER)
def test_following_a_link():
        driver = webdriver.Chrome()
        driver.get('https://ya.ru')
        search_input = driver.find_element(By.XPATH, '//input[@id="text"]')
        search_input.send_keys('market.yandex.ru')
        search_input.send_keys(Keys.ENTER)
        with allure.step('Переходим по первой ссылке'):
            link = driver.find_element(By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a')
            link.click()
        with allure.step('Проверяем Title страницы'):
            driver.switch_to_window(driver.window_handles[1])
            assert driver.title == 'Интернет-магазин Яндекс.Маркет — покупки с быстрой доставкой'