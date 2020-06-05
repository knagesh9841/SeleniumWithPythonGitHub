from selenium.webdriver import firefox
from selenium.webdriver.chrome.options import Options

from util import Logger


def getchromeoptions():
    log = Logger.getlogger()
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {"download.default_directory": "E:\Export"})
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--disable-notifications')
        return chrome_options
    except Exception as e:
        log.exception("Exception Occurred", exc_info=True)


def getfirefoxoptions():
    log = Logger.getlogger()
    try:
        firefox_options = firefox.options.Options()
        #firefox_options.add_argument('-headless')
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.dir", "E:\Export")
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel,image/jpeg")
        return firefox_options
    except Exception as e:
        log.exception("Exception Occurred", exc_info=True)
