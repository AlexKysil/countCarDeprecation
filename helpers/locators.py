"""
Global locators holfer
"""

from selenium.webdriver.common.by import By

# Main Page
USED_BUTTON = (By.XPATH, "//label[text() = 'Вживані ']")
BRAND_SEARCH = (By.XPATH, "//input[@id='brandTooltipBrandAutocompleteInput-brand']")
BRAND_LIST_VALUE = (By.XPATH, "//a[text()='{}']")
MARK_SEARCH = (By.XPATH, "//input[@id='brandTooltipBrandAutocompleteInput-model']")
SELECT_YEAR_FROM = (By.XPATH, "//select[@id='yearFrom']")
YEAR_FROM_VALUE = (By.XPATH, "//select[@id='yearFrom']//option[@value='{}']")
SELECT_YEAR_TO = (By.XPATH, "//select[@id='yearTo']")
YEAR_TO_VALUE = (By.XPATH, "//select[@id='yearTo']//option[@value='{}']")
OPTION_VALUE = (By.XPATH, "//option[@value='{}']")

SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

