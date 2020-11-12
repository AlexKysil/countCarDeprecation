"""
AUTORIA Main Page
"""
from helpers.constants import AUTORIA
from page_objects.base_page_object import BasePageObject

PAGE_URL = AUTORIA

class MainPage(BasePageObject):

    def __init__(self, driver_session):
        super().__init__(driver_session, PAGE_URL)

    def get_used_field(self):
        return self.custom_find_element(self.locators.USED_BUTTON)

    def get_brand_field(self):
        return self.custom_find_element(self.locators.BRAND_SEARCH)

    def get_mark_field(self):
        return self.custom_find_element(self.locators.MARK_SEARCH)

    def select_option_value(self, value):
        locator = self.locators.BRAND_LIST_VALUE
        locator = (locator[0], locator[1].format(value))
        self.wait_for_element(locator)
        self.custom_find_element(locator).click()

    def click_search_butn(self):
        self.wait_for_element(self.locators.SEARCH_BUTTON)
        self.custom_find_element(self.locators.SEARCH_BUTTON).click()

    def get_year_from(self):
        return self.custom_find_element(self.locators.SELECT_YEAR_FROM)

    def get_year_to(self):
        return self.custom_find_element(self.locators.SELECT_YEAR_TO)

    def select_year(self, field, year):
        locator = ''
        if field == 'from':
            locator = self.locators.YEAR_FROM_VALUE
        elif field == 'to':
            locator = self.locators.YEAR_TO_VALUE
        else:
            locator = self.locators.OPTION_VALUE

        locator = (locator[0], locator[1].format(year))
        self.wait_for_element(locator)
        self.custom_find_element(locator).click()
