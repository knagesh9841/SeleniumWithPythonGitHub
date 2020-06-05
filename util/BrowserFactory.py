import pytest
from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from util import OptionsManager, Utilities, Logger

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


def setdriver(browser_name):
    try:
        log = Logger.getlogger()
        global driver
        Utilities.killbrowserdriver(browser_name)
        if browser_name == "Chrome":
            log.info(browser_name+" Browser option is selected")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=OptionsManager.getchromeoptions())
        elif browser_name == "Firefox":
            log.info(browser_name + " Browser option is selected")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=OptionsManager.getfirefoxoptions())
        else:
            log.warn("Entered Wrong Browser name")

    except Exception as e:
        log.error("Exception Occurred", exc_info=True)


def getdriver():
    return driver

