from base.selenium_base import SeleniumBase
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from .config import *


class YandexSearchPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__central_input_search_xpath = central_input_search_xpath
        self.__upper_input_search_xpath = upper_input_search_xpath
        self.__switcher_class_name = 'footer3__disable-new-design-toggle'
        self.left_logo_xpath = '/html/body/main/div[1]/a'

    
    def send_query_search(self, query):
        central_input_search = self.is_present('xpath', self.__central_input_search_xpath)
        central_input_search.send_keys(query)
        central_input_search.send_keys(Keys.ENTER)
        upper_input_search = self.is_visiable('xpath', self.__upper_input_search_xpath)
        value = upper_input_search.get_attribute(upper_input_search_value)
        return value
        

    def switch_disighn(self, xpath):
        try:
            self.is_visiable('xpath', xpath)
            switcher = self.is_visiable('class_name', self.__switcher_class_name)
            switcher.click()
        except TimeoutException:
            print('Page Not Found')
        self.is_visiable('xpath', xpath)



