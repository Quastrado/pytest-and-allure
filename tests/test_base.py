import pytest
from base.selenium_base import SeleniumBase
from selenium import webdriver

def test_is_visiableble():
    
    driver = webdriver.Chrome()
    driver.get('https://ya.ru')
    sb = SeleniumBase(driver)
    el = sb.is_visiable('xpath', '//*[@id="text"]')
    assert el != None