"""
Base Page Object
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from helpers.constants import TIMEOUTS

class BasePageObject():
    """
    Parent class for all page objects
    """
    def __init__(self, driver_session, page_url):
        self.driver = driver_session
        self.timeouts = TIMEOUTS
        self.url = page_url


    def is_page_opened(self):
        """
        Verify is current URL match to expected
        :return:
        """
        return self.url == self.driver.current_url

    def wait_page_ready(self, timeout=TIMEOUTS['medium']):
        """
        Wait while page loading be completed
        :param timeout:
        :return:
        """

        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == 'complete'
            )
        except TimeoutException:
            raise TimeoutException("Page wasn`t opened for provided time")

    def open_page_and_wait(self, url='', timeout=TIMEOUTS['small']):
        """
        Open page with given or saved url, and wait page ready
        :param url:
        :param timeout:
        :return:
        """
        if not url:
            url = self.url

        self.driver.get(url)
        self.wait_page_ready(timeout)
        assert self.is_page_opened()

    def wait_for_element(self, element, timeout=TIMEOUTS['small']):
        """
        Wait for element to be displayed
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(element)
            )
            return self.driver.find_element(element[0], element[1])
        except TimeoutException:
            raise TimeoutException("Element {} wasn`t found for provided time".format(element))

    def custom_find_element(self, element):
        """
        Сustom find element
        :param element:
        :return:
        """
        return self.driver.find_element(element[0], element[1])

    def custom_find_all_elements(self, elements):
        """
        Custom find all elements
        :param elements:
        :return:
        """
        return self.driver.find_elements(elements[0], elements[1])

    def clear_and_enter_text(self, web_element, text):
        """
        Clear existing text and input new
        :param web_element:
        :param text:
        :return:
        """
        web_element.send_keys(Keys.CONTROL + 'a')
        web_element.send_keys(text)
