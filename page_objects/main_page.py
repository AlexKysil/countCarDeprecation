"""
AUTORIA Main Page
"""
from helpers.constants import AUTORIA
from page_objects.base_page_object import BasePageObject

PAGE_URL = AUTORIA

class MainPage(BasePageObject):

   def __init__(self, driver_session):
        super().__init__(driver_session, PAGE_URL)
