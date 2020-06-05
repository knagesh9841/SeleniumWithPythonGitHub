import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from util import Logger, Reporter, WaitUtilities


class ToolTipTextPage:

    # ********* Constructor *********

    def __init__(self, driver):
        self.driver = driver

    # ********** WebElements **********

    obj_hoverme = (By.XPATH, "//div[@class='tooltip']")
    obj_tooltiptext = (By.XPATH, "//span[@class='tooltiptext']")

    # ********* Page Methods *********

    @allure.step("Tool Tip Text Step")
    def verifytooltiptext(self):
        log = Logger.getlogger()
        sflag = False
        try:
            WaitUtilities.waitforpagetitleis(self.driver,
                                             "Selenium Practise: How to automate tooltip in Selenium webdriver", 5)
            hoverme = self.driver.find_element(*ToolTipTextPage.obj_hoverme)
            tooltiptext = self.driver.find_element(*ToolTipTextPage.obj_tooltiptext)

            action = ActionChains(self.driver)

            action.move_to_element(hoverme).click_and_hold().perform()

            WaitUtilities.waitForElementVisible(self.driver, ToolTipTextPage.obj_tooltiptext, 5)

            tooltipmsg = tooltiptext.text

            if tooltipmsg == "Tooltip text":
                Reporter.passed(self.driver, "ToolTip Text should be 'Tooltip text'.::ToolTip Text is 'Tooltip text'.")
            else:
                assert False

        except AssertionError as e:
            Reporter.failed(self.driver, "ToolTip Text should be 'Tooltip text'.::ToolTip Text is not 'Tooltip text'.")

        except Exception as e:
            log.error("Exception Occurred", exc_info=True)