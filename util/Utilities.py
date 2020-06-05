import os

import autoit

from util import Logger


def killbrowserdriver(browesrname):
    log = Logger.getlogger()
    if browesrname == "Chrome":
        driverprocess = "chromedriver.exe"
    elif browesrname == "Firefox":
        driverprocess = "firefox.exe"
    else:
        log.warn("Entered Wrong Browser name")

    try:
        code = os.system("taskkill /F /T /IM "+driverprocess)
        if code == 0:
            log.info("Driver process "+driverprocess+" is killed successfully.")
        else:
            log.info("Driver process "+driverprocess+" is not exists.")

    except Exception as e:
        log.error("Exception Occurred", exc_info=True)


def uploadfile(filename):
    autoit.win_wait("Open", 4)
    autoit.control_focus("Open", "Edit1")
    autoit.control_set_text("Open", "Edit1", filename)
    autoit.control_click("Open", "Button1")
    autoit.win_wait("Open", 4)

