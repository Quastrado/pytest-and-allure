import pytest
from pom.yandex_search_page import YandexSearchPage
from abstract.not_found_exception_raiser import check_url
from .config import *
import allure

@pytest.mark.usefixtures('setup')
class TestHomepage:

    @allure.feature('Test 1')
    @allure.story('Go to results page')
    @pytest.mark.parametrize('query', send_query_search_data)
    def test_send_query_search(self, query):
        with allure.step('Search page opening'):
            yandex_search_page = YandexSearchPage(self.driver)
        with allure.step('The page with the results for the query was opened'):
            assert yandex_search_page.send_query_search(query) == query

    @allure.feature('Test 2')
    @allure.story('Change of design to the old one')
    @pytest.mark.parametrize('expected_exception, element_name, xpath', switch_desighn_data)
    def test_switch_design(self, expected_exception, element_name, xpath):
        check_url(url)
        with allure.step('Search page opening'):
            with pytest.raises(expected_exception):
                yandex_search_page = YandexSearchPage(self.driver)
                with allure.step(f'Checking for the absence of an element: {element_name}'):
                    yandex_search_page.switch_disighn(xpath) == True