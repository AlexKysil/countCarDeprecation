"""
Global locators holfer
"""

from selenium.webdriver.common.by import By

# Main Page
USED_BUTTON = (By.XPATH, "//label[text() = 'Вживані ']")
BRAND_SEARCH = (By.XPATH, "//*[@data-text='Марка']")
BRAND_LIST_VALUE = (By.XPATH, "//a[@class='item' and text()='{}']")
MARK_SEARCH = (By.XPATH, "//*[@data-text='Модель']")
SELECT_YEAR_FROM = (By.XPATH, "//select[@id='yearFrom']")
SELECT_YEAR_TO = (By.XPATH, "//select[@id='yearTo']")
OPTION_VALUE = (By.XPATH, "//option[@value='{}']")

SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

