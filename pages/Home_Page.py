import allure
from selenium.webdriver.common.by import By

from util import Logger, Reporter, WaitUtilities


class HomePage:

    # ********* Constructor *********

    def __init__(self, driver):
        self.driver = driver

    # ********** WebElements **********

    obj_signout = (By.XPATH, "//a[text()='Sign out']")

    @allure.step("Login To Application")
    def logoutfromapplication(self):
        log = Logger.getlogger()
        try:
            logoutbtn = self.driver.find_element(*HomePage.obj_signout)
            logoutbtn.click()

            flag = WaitUtilities.waitforpagetitleis(self.driver, "Address Book - Sign In", 5)

            if flag:
                Reporter.passed(self.driver, "should be Logout from Application.::Successfully Logout from Application.")
                log.info("Successfully Logout from Application.")
            else:
                assert False

        except AssertionError as e:
            Reporter.failed(self.driver, "should be Logout from Application.::Failed to Logout from Application.")
            log.error("Failed to Logout from Application.")

        except Exception as e:
            log.error("Exception Occurred", exc_info=True)
