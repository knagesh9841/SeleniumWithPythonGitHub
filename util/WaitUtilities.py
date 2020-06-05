from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from util import Logger


def waitForElementVisible(driver, element, timeout):
    flag = False
    log = Logger.getlogger()
    try:
        wait = WebDriverWait(driver, timeout)
        Element = wait.until(expected_conditions.visibility_of_element_located(element))
        if Element is not None:
            log.info("-----------Element is Visible.-------------")
            flag = True
    except Exception as e:
        log.error("----------Element is Not Visible.---------")

    return flag


def waitForAlertIsPresent(driver, timeout):
    flag = False
    log = Logger.getlogger()
    try:
        wait = WebDriverWait(driver, timeout)
        Element = wait.until(expected_conditions.alert_is_present())
        log.info("-----------Alert Popup is Visible.-------------")
        flag = True
    except Exception as e:
        log.error("----------Alert Popup is Not Visible.---------")

    return flag


def waitForWindowIsPresent(driver, timeout):
    flag = False
    log = Logger.getlogger()
    try:
        wait = WebDriverWait(driver, timeout)
        Element = wait.until(expected_conditions.number_of_windows_to_be(2))
        log.info("-----------New Window is Opened.-------------")
        flag = True
    except Exception as e:
        log.error("----------New Window is Not Opened.---------")

    return flag


def waitforpagetitleis(driver, title, timeout):
    flag = False
    log = Logger.getlogger()
    try:
        wait = WebDriverWait(driver, timeout)
        flag = wait.until(expected_conditions.title_is(title))
        log.info("-----------Page with Title "+title+" is opened.-------------")
        flag = True
    except Exception as e:
        log.error("----------Page with Title "+title+" is not opened.---------")

    return flag
