from os import link
from time import time
import pytest
from pom.yandex_search_page import YandexSearchPage
from .test_data import *
import allure

@pytest.mark.usefixtures('setup')
class TestHomepage:

    @allure.feature('Check value in top input')
    @allure.story('Go to results page')
    @pytest.mark.parametrize('query', get_upper_input_search_value)
    def test_get_upper_input_search_value(self, query):
        yandex_search_page = YandexSearchPage(self.driver)
        with allure.step('The page with the results for the query was opened'):
            assert yandex_search_page.get_upper_input_search_value(query) == query


    @allure.feature('Checking for automatic whitespace removal')
    @allure.story('Go to results page')
    @pytest.mark.parametrize('query, query_after_input', check_whitespace_removal_data)
    def test_get_upper_input_search_value(self, query, query_after_input):
        yandex_search_page = YandexSearchPage(self.driver)
        with allure.step('The page with the results for the query was opened'):
            assert yandex_search_page.get_upper_input_search_value(query) == query_after_input
            
    
    @allure.feature('Checking for elements on the page when changing the design')
    @allure.story('Change of design to the old one and try to find element')
    @pytest.mark.parametrize('expected_exception, element_name, xpath', check_for_links_data)
    def test_find_element_after_switch(self, expected_exception, element_name, xpath):
        yandex_search_page = YandexSearchPage(self.driver)
        try:
            with allure.step(f'Checking for the absence of an element: {element_name}'):
                yandex_search_page.find_element_after_switch(xpath) == True
                not_found = False
        except expected_exception:
            not_found = True
        assert not_found

    
    @allure.feature('NEGATIVE Checking for elements on the page when changing the design')
    @allure.story('Change of design to the old one and try to find element')
    @pytest.mark.parametrize('expected_exception, element_name, xpath', check_for_links_data)
    def test_find_element_after_switch_negative(self, expected_exception, element_name, xpath):
        with pytest.raises(expected_exception):
            yandex_search_page = YandexSearchPage(self.driver)
            with allure.step(f'Checking for the absence of an element: {element_name}'):
                yandex_search_page.find_element_after_switch(xpath) == True

    
    @allure.feature('Verification of the transition on the link on the page')
    @allure.story('Following links on the page')
    @pytest.mark.parametrize('link, link_xpath, expected_element_xpath', following_link_data)
    def test_following_links(self, link, link_xpath, expected_element_xpath):
        yandex_search_page = YandexSearchPage(self.driver)
        with allure.step(f'Following a link: {link}'):
            yandex_search_page.following_link(link_xpath, expected_element_xpath)


    @allure.feature('Login button test')
    @allure.story('Following links on the page')
    def test_login_button(self):
        yandex_search_page = YandexSearchPage(self.driver)
        yandex_search_page.login_button_click()
