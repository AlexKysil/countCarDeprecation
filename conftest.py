import pytest
from selenium import webdriver

from chromedriver_py import binary_path as chrome_path
from helpers.constants import TIMEOUTS


@pytest.fixture(scope='module')
def driver_session():
    """
    Init chromedriver session
    :return:
    """

    driver_session = webdriver.Chrome(executable_path=chrome_path)
    driver_session.maximize_window()
    driver_session.implicitly_wait(TIMEOUTS['small'])

    yield driver_session

    driver_session.quit()


@pytest.fixture(scope='function')
def data_storage():
    """
    Hold data during test
    :return:
    """

    data_storage = {}
    yield data_storage