import pytest
from utility import utils
import playwright
from playwright.sync_api import sync_playwright
from utility.utils import Variables as V
from utility.custom_utils import move_dir
from utility.logger import custom_logger as cl
import logging
import sys


@pytest.fixture(scope="class")
def OneTimeSetup(url, get_context):
    log = cl(loglevel=logging.DEBUG)
    try:
        if url:
            endpoint_url = url
        else:
            endpoint_url = utils.Variables.ENDPOINT_URL
        if endpoint_url != "https://reqres.in":
            log.error("Invalid url")
            sys.exit()
    except:
        raise Exception
    yield endpoint_url
    

def pytest_addoption(parser):
    parser.addoption("--url")

@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="class")
def get_context():
    with sync_playwright() as p:
        # url = url + V.LIST_USER_ENDPOINT
        request_context = p.request.new_context(extra_http_headers= V.HEADERS)
        yield request_context
        request_context.dispose()