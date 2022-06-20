import pytest
from selenium import webdriver
from pom.yandex_search_page import YandexSearchPage

def test_see_input():
    ysp = YandexSearchPage(self.driver)
    el = ysp.see_input_search()
    assert el !=None