import pytest
import pytest_html
from pytest import Config
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture()
def setup():
    driver: WebDriver = webdriver.Chrome()
    driver.maximize_window()
    return driver






