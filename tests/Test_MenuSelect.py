import allure

from tests.BaseTest import BaseTest
from util import Logger, BrowserFactory, PropertyManager


class Test_MenuSelection(BaseTest):
    @allure.title("This test has a custom title")
    @allure.story('epic_1')
    @allure.feature('feature_1')
    @allure.suite("First Suite")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description_html("""
        <h1>Verify Radio Button is Selected or Not</h1>
        <table style="width:100%">
          <tr>
            <th>Usecase</th>
            <th>Testcase</th>
            <th>Feature</th>
          </tr>
          <tr align="center">
            <td>Logitics</td>
            <td>12345</td>
            <td>Visibility</td>
          </tr>
        </table>
        """)
    def test_menuselect(self):
        log = Logger.getlogger()
        driver = BrowserFactory.getdriver()
        driver.get(PropertyManager.getconfigdata("menuselectionurl"))
        log.info("-----------Navigating to URL " + PropertyManager.getconfigdata("menuselectionurl") + "-------------")
        driver.implicitly_wait(3)
        log.info("implicitly Wait is set to 3 Sec")
        driver.maximize_window()
        log.info("-----------Window is Maximized.-------------")

        self.MenuSelectionPage_Object.verifymenuselection()


class Test_ToolTipText(BaseTest):
    @allure.title("This test has a custom title")
    @allure.story('epic_1')
    @allure.feature('feature_1')
    @allure.suite("First Suite")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description_html("""
            <h1>Verify Radio Button is Selected or Not</h1>
            <table style="width:100%">
              <tr>
                <th>Usecase</th>
                <th>Testcase</th>
                <th>Feature</th>
              </tr>
              <tr align="center">
                <td>Logitics</td>
                <td>12345</td>
                <td>Visibility</td>
              </tr>
            </table>
            """)
    def test_menuselect(self):
        log = Logger.getlogger()
        driver = BrowserFactory.getdriver()
        driver.get(PropertyManager.getconfigdata("tooltipurl"))
        log.info("-----------Navigating to URL " + PropertyManager.getconfigdata("tooltipurl") + "-------------")
        driver.implicitly_wait(3)
        log.info("implicitly Wait is set to 3 Sec")
        driver.maximize_window()
        log.info("-----------Window is Maximized.-------------")

        self.ToolTipTextPage_object.verifytooltiptext()