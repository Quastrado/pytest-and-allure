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
        self.__search_results = search_results_xpath
        self.__switcher_class_name = switcher_class_name
        self.__login_button_xpath = login_button_xpath
    
    
    def send_query_search(self, query):
        central_input_search = self.is_present('xpath', self.__central_input_search_xpath)
        central_input_search.send_keys(query)
        central_input_search.send_keys(Keys.ENTER)
        upper_input_search = self.is_visiable('xpath', self.__upper_input_search_xpath)
        value = upper_input_search.get_attribute(upper_input_search_value)
        results = self.are_present('xpath', search_results_xpath)
        return {'value': value, 'results': results}

    
    def find_element_after_switch(self, xpath):
        try:
            self.is_visiable('xpath', xpath)
            switcher = self.is_visiable('class_name', self.__switcher_class_name)
            switcher.click()
        except TimeoutException:
            print('Page Not Found')
        self.is_visiable('xpath', xpath)
        return True

    
    def following_link(self, xpath, expected_element_xpath):
        try:
            link = self.is_visiable('xpath', xpath)
            link.click()
            self.is_visiable('xpath', expected_element_xpath)
        except TimeoutException as ex:
            print("Exception has been thrown. " + str(ex))

    
    def login_button_click(self):
        login_button = self.is_visiable('xpath', self.__login_button_xpath)
        login_button.click()
        self.is_visiable('xpath', login_form_xpath)

