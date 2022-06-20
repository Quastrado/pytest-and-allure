from base.selenium_base import SeleniumBase


class YandexSearchPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__input_search_xpath = '//*[@id="text"]' 

    def see_input_search(self):
        return self.is_visiable('xpath', self.__input_search_xpath, 'Search Input')

    def switch_disighn():
        pass

