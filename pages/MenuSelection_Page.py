import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from util import Logger, Reporter, WaitUtilities


class MenuSelectionPage:

    # ********* Constructor *********

    def __init__(self, driver):
        self.driver = driver

    # ********** WebElements **********

    obj_tutorial = (By.XPATH, "//nav[@class='navigation']//span[text()='Tutorial']")
    obj_backendtesting = (By.XPATH, "//nav[@class='navigation']//span[text()='Back-End Testing Automation']")
    obj_restassured = (By.XPATH, "//nav[@class='navigation']//span[text()='Rest Assured']")
    obj_clientserver = (By.XPATH, "//a[text()='Client Server Architecture and HTTP Protocol']")

    # ********* Page Methods *********

    @allure.step("Menu Selection Step")
    def verifymenuselection(self):
        log = Logger.getlogger()
        sflag = False
        try:
            WaitUtilities.waitforpagetitleis(self.driver, "Free QA Automation Tools Tutorial for Beginners with Examples", 5)
            tutorial = self.driver.find_element(*MenuSelectionPage.obj_tutorial)
            backendtesting = self.driver.find_element(*MenuSelectionPage.obj_backendtesting)
            restassured = self.driver.find_element(*MenuSelectionPage.obj_restassured)

            action = ActionChains(self.driver)

            action.move_to_element(tutorial).perform()
            WaitUtilities.waitForElementVisible(self.driver, MenuSelectionPage.obj_backendtesting, 5)
            action.move_to_element(backendtesting).click_and_hold().perform()
            WaitUtilities.waitForElementVisible(self.driver, MenuSelectionPage.obj_restassured, 5)
            action.move_to_element(restassured).click().perform()
            sflag = WaitUtilities.waitforpagetitleis(self.driver, "Rest Assured Tutorial for REST API Automation Testing", 5)

            if sflag:
                Reporter.passed(self.driver, "RestAssured Menu should be selected::RestAssured Menu is selected.")
            else:
                assert False

        except AssertionError as e:
            Reporter.failed(self.driver, "RestAssured Menu should be selected::RestAssured Menu is not selected.")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)

