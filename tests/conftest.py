import pytest

from tests.BaseTest import BaseTest
from util import BrowserFactory, Logger


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    try:
        log = Logger.getlogger()
        browser_name = request.config.getoption("browser_name")
        BrowserFactory.setdriver(browser_name)
        log.info(browser_name+" Browser is invoked.")
        BaseTest.init_page()
        yield
        BrowserFactory.getdriver().quit()
        log.info(browser_name + " Browser is Closed.")
    except Exception as e:
        log.error("Exception Occurred", exc_info=True)


