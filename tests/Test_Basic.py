import os

import allure
import pytest

from tests.BaseTest import BaseTest
from util import BrowserFactory, PropertyManager, Logger


class Test_Firsts(BaseTest):

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
        <td>Scheduling</td>
      </tr>
    </table>
    """)
    def test_first(self):
        log = Logger.getlogger()
        driver = BrowserFactory.getdriver()
        driver.get(PropertyManager.getconfigdata("url"))
        log.info("-----------Navigating to URL "+PropertyManager.getconfigdata("url")+"-------------")
        driver.implicitly_wait(3)
        log.info("implicitly Wait is set to 3 Sec")
        driver.maximize_window()
        log.info("-----------Window is Maximized.-------------")

        self.AutomationPracticePage_Object.verifyradiobtnisselectedornot()

    @pytest.mark.usefixtures("dataload")
    @allure.suite("First Suite")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("This will verify Checkbox is selected or not")
    def test_second(self, dataload):
        self.AutomationPracticePage_Object.verifyautosuggestioncheckboxselect(dataload[0])

    @allure.suite("Third Suite")
    @allure.story('epic_1')
    @allure.feature('feature_2')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_third(self):
        self.AutomationPracticePage_Object.verifyalertshowhidetabledata()

    @allure.suite("Fourth Suite")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fourth(self):
        self.AutomationPracticePage_Object.verifywindoframewswitchtooltip()


@pytest.fixture()
def dataload():
    return ["Gabon"]

