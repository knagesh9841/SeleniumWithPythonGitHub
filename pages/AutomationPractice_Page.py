import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from util import Logger, BrowserFactory, WaitUtilities, Reporter


class AutomationPracticePage:

    # ********* Constructor *********

    def __init__(self, driver):
        self.driver = driver

    # ********** WebElements **********

    obj_radiobtns = (By.CSS_SELECTOR, "input.radioButton")
    obj_dynamicinput = (By.ID, "autocomplete")
    obj_dynamicvalue = (By.XPATH, "//ul[contains(@class,'ui-menu')]/li/div")
    obj_dropdown = (By.NAME, "dropdown-class-example")
    obj_checkbox = (By.XPATH, "//input[@type='checkbox']")
    obj_alertinputbox = (By.CSS_SELECTOR, "#name")
    obj_alertbtn = (By.CSS_SELECTOR, "#alertbtn")
    obj_dispelement = (By.XPATH, "//input[@class='inputs displayed-class']")
    obj_hidebtn = (By.ID, "hide-textbox")
    obj_showbtn = (By.ID, "show-textbox")
    obj_table = (By.XPATH, "//table[@id='product']//tr")
    obj_tabledata = (By.XPATH, "//table[@id='product']//tr/td")
    obj_openwindow = (By.XPATH, "//button[text()='Open Window']")
    obj_homelinkbtn = (By.XPATH, "//a[text()='Home']")
    obj_mousehover = (By.XPATH, "//button[text()='Mouse Hover']")
    obj_tooltiptext = (By.XPATH, "//div[@class='mouse-hover-content']/a")

    # ********* Page Methods *********
    @allure.step("Radio Button Step")
    def verifyradiobtnisselectedornot(self):
        log = Logger.getlogger()
        sflag = False
        try:
            RadioButtons = self.driver.find_elements(*AutomationPracticePage.obj_radiobtns)
            for radiobutton in RadioButtons:
                if radiobutton.get_attribute("value") == "radio2":
                    radiobutton.click()
                    log.info("Radio Button is Selected")
                    sflag = True
                    break

            if not sflag:
                Reporter.passed(self.driver, "Radiobutton should be selected::Radio Button is Selected")
            else:
                assert False
        except AssertionError as e:
            Reporter.failed(self.driver, "Radiobutton should be selected::Radiobutton is not selected.")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)

    @allure.step
    def verifyautosuggestioncheckboxselect(self, name):
        log = Logger.getlogger()
        try:
            AutoSuggest = self.driver.find_element(*AutomationPracticePage.obj_dynamicinput)
            AutoSuggest.clear()
            AutoSuggest.send_keys(name)
            WaitUtilities.waitForElementVisible(self.driver, (By.XPATH, "//ul[contains(@class,'ui-menu')]/li/div[text()='"+name+"']"), 5)
            AutoSuggestValue = self.driver.find_element_by_xpath("//ul[contains(@class,'ui-menu')]/li/div[text()='"+name+"']")
            AutoSuggestValue.click()
            log.info("Value is Entered in Auto Suggestion Input Box")

            select = Select(self.driver.find_element(*AutomationPracticePage.obj_dropdown))

            AllOptions = select.options

            for i in AllOptions:
                log.info(i.text)

            select.select_by_value("option3")

            CheckBoxes = self.driver.find_elements(*AutomationPracticePage.obj_checkbox)

            for checkbox in CheckBoxes:
                checkbox.click()
                log.info(checkbox.text)

            if not False:
                Reporter.passed(self.driver, "CheckBox should be selected::CheckBox Button is Selected")
            else:
                assert False
        except AssertionError as e:
            Reporter.failed(self.driver, "CheckBox should be selected::CheckBox is not selected.")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)

    @allure.step
    def verifyalertshowhidetabledata(self):
        log = Logger.getlogger()
        try:
            AlertInputBox = self.driver.find_element(*AutomationPracticePage.obj_alertinputbox)

            AlertInputBox.clear()
            AlertInputBox.send_keys("Nagesh")

            AlertBtn = self.driver.find_element(*AutomationPracticePage.obj_alertbtn)

            AlertBtn.click()

            WaitUtilities.waitForAlertIsPresent(self.driver, 5)

            Alerts = self.driver.switch_to.alert

            log.info("Alert Text is "+Alerts.text+"")

            Alerts.accept()

            DisplayedElement = self.driver.find_element(*AutomationPracticePage.obj_dispelement)

            log.info("CSS Value "+DisplayedElement.value_of_css_property("font-size")+"")

            HideBtn = self.driver.find_element(*AutomationPracticePage.obj_hidebtn)

            HideBtn.click()

            log.info("Clicked on Hide Button")

            ShowBtn = self.driver.find_element(*AutomationPracticePage.obj_showbtn)

            ShowBtn.click()

            if DisplayedElement.is_displayed():
                Reporter.passed(self.driver, "InputBox should be Displayed when clicked on Show Button::InputBox is Displayed when clicked on Show Button")
            else:
                assert False

            log.info("Clicked on Show Button ")

            TableElement = self.driver.find_element(*AutomationPracticePage.obj_table)

            TableHeader = TableElement.find_elements_by_xpath("th")

            for i in TableHeader:
                log.info("Table header " + i.text)

            TableRow = self.driver.find_elements(*AutomationPracticePage.obj_tabledata)

            for j in TableRow:
                log.info("Table Row data " + j.text)
        except AssertionError as e:
            Reporter.failed(self.driver, "InputBox should be Displayed when clicked on Show Button:InputBox is not Displayed when clicked on Show Button.")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)

    @allure.step
    def verifywindoframewswitchtooltip(self):
        log = Logger.getlogger()
        sflag = False
        try:
            parentwindowhanlde = self.driver.current_window_handle
            openwindowbutton = self.driver.find_element(*AutomationPracticePage.obj_openwindow)
            self.driver.execute_script("arguments[0].click();", openwindowbutton)
            windowhandles = set(self.driver.window_handles)
            WaitUtilities.waitForWindowIsPresent(self.driver, 10)
            for windowhandle in windowhandles:
                self.driver.switch_to.window(windowhandle)
                if self.driver.title == "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy":
                    log.info("Switched to Child Window")
                    sflag = True
                    self.driver.close()
                    break

            self.driver.switch_to.window(parentwindowhanlde)
            log.info("Switched back to Parent Window")

            Reporter.info("Should be Switched to Child Window::Switched to Child Window Successfully.")

            self.driver.switch_to.frame("courses-iframe")
            log.info("Switched to Frame Successfully")
            homelink = self.driver.find_element(*AutomationPracticePage.obj_homelinkbtn)

            self.driver.execute_script("arguments[0].scrollIntoView(false);", homelink)

            self.driver.switch_to.parent_frame()

            log.info("Switched to Parent Frame Successfully")

            action = ActionChains(self.driver)

            mousehoverelement = self.driver.find_element(*AutomationPracticePage.obj_mousehover)

            action.move_to_element(mousehoverelement).click_and_hold(mousehoverelement).perform()

            WaitUtilities.waitForElementVisible(self.driver, AutomationPracticePage.obj_tooltiptext, 5)
            tooltiptexts = self.driver.find_elements(*AutomationPracticePage.obj_tooltiptext)

            for tooltipelement in tooltiptexts:
                log.info("Tooltip Text " + tooltipelement.text)
        except AssertionError as e:
            Reporter.failed(self.driver, "Should be Switched to Child Window::Not Switched to Child Window.")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)



