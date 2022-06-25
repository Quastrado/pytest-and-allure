import time
from selenium.webdriver.support.events import AbstractEventListener

from base.selenium_base import SeleniumBase


class MyListener(AbstractEventListener):

    def before_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ak_bmsc')

    def after_click(self, element, driver):
        SeleniumBase(driver).delete_cookie('ak_bmsc')

    def after_change_value_of(self, element, driver) -> None:
        time.sleep(3)
