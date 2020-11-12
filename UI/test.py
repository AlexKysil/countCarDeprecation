from selenium.webdriver.common.keys import Keys

from page_objects.main_page import MainPage


def test_test_run(driver_session):
    autoria_page = MainPage(driver_session)

    autoria_page.open_page_and_wait()

    autoria_page.get_used_field().click()

    brand_field = autoria_page.get_brand_field()
    autoria_page.clear_and_enter_text(brand_field, "Kia")
    brand_field.send_keys(Keys.ENTER)
    autoria_page.select_option_value("Kia")

    mark_field = autoria_page.get_mark_field()
    autoria_page.clear_and_enter_text(mark_field, "Sportage")
    mark_field.send_keys(Keys.ENTER)
    autoria_page.select_option_value("Sportage")

    autoria_page.get_year_from().click()
    autoria_page.select_year('from', '2015')

    autoria_page.get_year_to().click()
    autoria_page.select_year('to', '2015')

    autoria_page.click_search_butn()
    autoria_page.wait_page_ready()
