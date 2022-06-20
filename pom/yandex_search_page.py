from base.selenium_base import SeleniumBase
from selenium.webdriver.common.keys import Keys


class YandexSearchPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__central_input_search_xpath = '//*[@id="text"]'
        self.__upper_input_search_xpath = '//*[@id="uniq16547008090681"]'

    
    def send_query_search(self, query):
        central_input_search = self.is_present('xpath', self.__central_input_search_xpath)
        central_input_search.send_keys(query)
        central_input_search.send_keys(Keys.ENTER)
        upper_input_search = self.is_visiable('xpath', self.__upper_input_search_xpath)
        atr = upper_input_search.get_attribute('value')
        return atr
        

    def switch_disighn():
        pass

