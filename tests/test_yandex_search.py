import pytest
from pom.yandex_search_page import YandexSearchPage


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_input_search_visibility(self):
        yandex_search_page = YandexSearchPage(self.driver)
        a = yandex_search_page.see_input_search() # for debug
        assert a != None



