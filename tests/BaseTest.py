import pytest

from pages.Address_Page import AddressPage
from pages.AutomationPractice_Page import AutomationPracticePage
from pages.Home_Page import HomePage
from pages.Login_Page import LoginPage
from pages.MenuSelection_Page import MenuSelectionPage
from pages.Toltiptext_Page import ToolTipTextPage
from util import BrowserFactory


@pytest.mark.usefixtures("setup")
class BaseTest:

    AutomationPracticePage_Object = None
    MenuSelectionPage_Object = None
    ToolTipTextPage_object = None
    LoginPage_object = None
    Homepage_object = None
    AddressPage_object = None

    @classmethod
    def init_page(cls):
        driver = BrowserFactory.getdriver()
        cls.AutomationPracticePage_Object = AutomationPracticePage(driver)
        cls.MenuSelectionPage_Object = MenuSelectionPage(driver)
        cls.ToolTipTextPage_object = ToolTipTextPage(driver)
        cls.LoginPage_object = LoginPage(driver)
        cls.Homepage_object = HomePage(driver)
        cls.AddressPage_object = AddressPage(driver)
