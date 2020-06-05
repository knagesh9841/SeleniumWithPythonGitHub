from time import sleep

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from util import Logger, Reporter, ExcelUtils, WaitUtilities, Utilities


class AddressPage:
    # ********* Constructor *********

    def __init__(self, driver):
        self.driver = driver

    # ********** WebElements **********

    obj_addressbtn = (By.XPATH, "//a[text()='Addresses']")
    obj_newaddressbtn = (By.XPATH, "//a[text()='New Address']")
    obj_fname = (By.ID, "address_first_name")
    obj_lname = (By.ID, "address_last_name")
    obj_streetaddrs = (By.ID, "address_street_address")
    obj_secondaddrs = (By.ID, "address_secondary_address")
    obj_city = (By.NAME, "address[city]")
    obj_state = (By.ID, "address_state")
    obj_zipcode = (By.ID, "address_zip_code")
    obj_country = (By.ID, "address_country_us")
    obj_age = (By.ID, "address_age")
    obj_website = (By.ID, "address_website")
    obj_upload = (By.ID, "address_picture")
    obj_phone = (By.ID, "address_phone")
    obj_interest = (By.ID, "address_interest_climb")
    obj_note = (By.ID, "address_note")
    obj_submitbtn = (By.XPATH, "//input[@name='commit']")
    obj_successmsg = (By.XPATH, "//div[@class='alert alert-notice']")
    obj_tablerow = (By.XPATH, "//table[@class='table']//tbody/tr")
    obj_deletebtn = (By.XPATH, "//a[text()='Destroy']")

    # ********* Page Methods *********

    @allure.step("Fill Up Address Details.")
    def fillAddressDetails(self):
        log = Logger.getlogger()
        try:

            addressbtn = self.driver.find_element(*AddressPage.obj_addressbtn)
            addressbtn.click()

            WaitUtilities.waitForElementVisible(self.driver, AddressPage.obj_newaddressbtn, 5)

            newaddressbtn = self.driver.find_element(*AddressPage.obj_newaddressbtn)

            newaddressbtn.click()

            WaitUtilities.waitForElementVisible(self.driver, AddressPage.obj_fname, 5)

            addressdata = ExcelUtils.readdata("Testdata.xlsx", "Address", 2)

            testdataholder = ExcelUtils.getdata(addressdata, "First Name")

            fname = self.driver.find_element(*AddressPage.obj_fname)

            fname.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "Last Name")

            lname = self.driver.find_element(*AddressPage.obj_lname)

            lname.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "Street")

            streetaddrs = self.driver.find_element(*AddressPage.obj_streetaddrs)

            streetaddrs.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "Secondary Address")

            secondaddrs = self.driver.find_element(*AddressPage.obj_secondaddrs)

            secondaddrs.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "City")

            city = self.driver.find_element(*AddressPage.obj_city)

            city.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "State")

            state = Select(self.driver.find_element(*AddressPage.obj_state))

            state.select_by_value(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "ZipCode")

            zipcode = self.driver.find_element(*AddressPage.obj_zipcode)

            zipcode.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "Country")

            country = self.driver.find_element(*AddressPage.obj_country)

            country.click()

            testdataholder = ExcelUtils.getdata(addressdata, "Age")

            age = self.driver.find_element(*AddressPage.obj_age)

            age.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "Website")

            website = self.driver.find_element(*AddressPage.obj_website)

            website.send_keys(testdataholder)

            uploadbtn = self.driver.find_element(*AddressPage.obj_upload)

            action = ActionChains(self.driver)

            action.move_to_element(uploadbtn).click().perform()

            Utilities.uploadfile("E:\\CodeWorkspace\\SeleniumWithPythonPractice\\SeleniumWithPythonGitHub\\resources\\testdata\\abc.txt")

            testdataholder = ExcelUtils.getdata(addressdata, "Phone")

            phone = self.driver.find_element(*AddressPage.obj_phone)

            phone.send_keys(testdataholder)

            testdataholder = ExcelUtils.getdata(addressdata, "Interest")

            interest = self.driver.find_element(*AddressPage.obj_interest)

            interest.click()

            testdataholder = ExcelUtils.getdata(addressdata, "Note")

            note = self.driver.find_element(*AddressPage.obj_note)

            note.send_keys(testdataholder)

            submitbtn = self.driver.find_element(*AddressPage.obj_submitbtn)

            submitbtn.click()

            WaitUtilities.waitForElementVisible(self.driver, AddressPage.obj_successmsg, 5)

            successmsg = self.driver.find_element(*AddressPage.obj_successmsg)

            actualmsg = successmsg.text

            if actualmsg == "Address was successfully created.":
                Reporter.passed(self.driver, "Address should be successfully created.::Address is successfully created.")
                log.info("Address is successfully created.")
            else:
                assert False

        except AssertionError as e:
            Reporter.failed(self.driver, "Address should be successfully created.::Address is not successfully created.")
            log.error("Address is not successfully created.")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)

    @allure.step("Verify Address Details.")
    def verifyAddressDetails(self):
        log = Logger.getlogger()
        try:
            addressbtn = self.driver.find_element(*AddressPage.obj_addressbtn)
            addressbtn.click()

            WaitUtilities.waitForElementVisible(self.driver, AddressPage.obj_newaddressbtn, 5)

            tablerow = self.driver.find_element(*AddressPage.obj_tablerow)

            tabledata = tablerow.find_elements_by_xpath("td")

            fname = tabledata[0].text

            if fname == "Nagesh":
                Reporter.passed(self.driver, "Address Details should be verified successfully.::Address Details is verified successfully.")
                log.info("Address Details is verified successfully")
            else:
                assert False

        except AssertionError as e:
            Reporter.failed(self.driver, "Address should be verified.::Address is not verified.")
            log.error("Address Details is not verified successfully")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)

    @allure.step("Delete Address Details.")
    def deleteAddressDetails(self):
        log = Logger.getlogger()
        try:
            deletebtn = self.driver.find_element(*AddressPage.obj_deletebtn)
            deletebtn.click()
            WaitUtilities.waitForAlertIsPresent(self.driver, 5)

            Alerts = self.driver.switch_to.alert
            Alerts.accept()
            WaitUtilities.waitForElementVisible(self.driver, AddressPage.obj_successmsg, 5)

            successmsg = self.driver.find_element(*AddressPage.obj_successmsg)

            actualmsg = successmsg.text

            if actualmsg == "Address was successfully destroyed.":
                Reporter.passed(self.driver,
                                "Address should be successfully Deleted.::Address is successfully Deleted.")
                log.info("Address Details is Deleted successfully")
            else:
                assert False

        except AssertionError as e:
            Reporter.failed(self.driver, "Address should be Deleted.::Address is not Deleted.")
            log.info("Address Details is not deleted successfully")
        except Exception as e:
            log.error("Exception Occurred", exc_info=True)