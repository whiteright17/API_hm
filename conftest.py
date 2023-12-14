import pytest
from selenium import webdriver

from api.api_client import MyApi


@pytest.fixture
def my_api():
    return MyApi(url="https://httpbin.org", headers={}, payload={})


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
