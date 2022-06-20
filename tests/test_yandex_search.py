import pytest
from pom.yandex_search_page import YandexSearchPage
from .config import send_query_search_data
import allure

@pytest.mark.usefixtures('setup')
class TestHomepage:

    @allure.feature('First test')
    @allure.story('Go to results page')
    @pytest.mark.parametrize('query', send_query_search_data)
    def test_send_query_search(self, query):
        with allure.step('Search page opening'):
            yandex_search_page = YandexSearchPage(self.driver)
        with allure.step('The page with the results for the query was opened'):
            assert yandex_search_page.send_query_search(query) == query

