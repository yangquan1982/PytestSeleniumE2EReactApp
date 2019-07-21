#!/usr/bin/python3
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost:3000", help="url")


@pytest.fixture(scope="module", autouse=True)
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(options=options)
    return browser

@pytest.fixture(scope="module")
def url(request):
    return request.config.getoption("--url")
